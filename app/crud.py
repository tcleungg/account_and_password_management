from sqlalchemy.orm import Session
import re

from app import models, schemas

class AccountCrud:
    def __init__(self, db: Session):
        self.db = db

    def username_exist(self, username):
         if self.db.query(models.Account).filter(models.Account.username == username).first():
             return "Username already exists"
         return None

    def valid_username(self, username):
        length = len(username)
        if length < 3 or length > 32:
            return "The Username should be minimum 3, maximum 32."
        return None
    
    def valid_password(self, password):
        length = len(password)
        if length < 8 or length > 32:
            return "The Password should be minimum 8, maximum 32."
        elif re.search('[0-9]',password) is None:
            return "The Password should contain at least 1 digit (0-9)."
        elif re.search('[a-z]',password) is None: 
            return "The Password should contain at least 1 lowercase letter (a-z)."
        elif re.search('[A-Z]',password) is None:
            return "The Password should contain at least 1 uppercase letter (A-Z)."

    def create(self, data: schemas.AccountBase):
        account = models.Account(
                            username=data.username,
                            password=data.password)
        self.db.add(account)
        self.db.commit()
        self.db.refresh(account)

    def get(self, username):
        return self.db.query(models.Account).filter(models.Account.username == username).first()
