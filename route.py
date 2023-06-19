from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.crud import AccountCrud
from app.schemas import AccountBase, ResponseBase, AccountErrorBase
from app.exception import AccountException
from app.db import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post(f'/api/account/register', responses={
                                                    200: {"model": ResponseBase},
                                                    403: {"model": AccountErrorBase},
                                                })
async def register(account_data: AccountBase, db: Session = Depends(get_db)):
    curd = AccountCrud(db)
    username = account_data.username
    check_name_result = curd.username_exist(username)
    if check_name_result:
        raise AccountException(403, reason=check_name_result)
    curd.create(account_data)
    return ResponseBase(success = True)
