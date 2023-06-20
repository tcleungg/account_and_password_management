from sqlalchemy.orm import Session
from passlib.context import CryptContext

from app import models, schemas

class AccountCrud:
    def __init__(self, db: Session):
        self.db = db
        self.ctx = CryptContext(schemes=["sha256_crypt"])

    def create(self, data: schemas.AccountBase):
        hashed_password = self.ctx.hash(data.password)
        account = models.Account(
                            username=data.username,
                            password=hashed_password)
        self.db.add(account)
        self.db.commit()
        self.db.refresh(account)

    def get(self, username):
        return self.db.query(models.Account).filter(models.Account.username == username).first()
