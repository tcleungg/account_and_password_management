from sqlalchemy.orm import Session

from app import models, schemas

class AccountCrud:
    def __init__(self, db: Session):
        self.db = db

    def username_exist(self, username):
         if self.db.query(models.Account).filter(models.Account.username == username).all():
             return "Username already exists"
         return None

    def valid_username(self, username):
        length = len(username)
        if length < 3 or length > 32:
            return "The Username should be minimum 3, maximum 32."
        return None

    def create(self, data: schemas.AccountBase):
        account = models.Account(
                            username=data.username,
                            password=data.password)
        self.db.add(account)
        self.db.commit()
        self.db.refresh(account)
