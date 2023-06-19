from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.crud import AccountCrud
from app.schemas import AccountBase, ResponseBase, AccountErrorBase, VerifyErrorBase
from app.exception import AccountException, VerifyException
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
    password = account_data.password

    check_name_result = curd.username_exist(username)
    if check_name_result:
        raise AccountException(403, reason=check_name_result)
    
    valid_name_result = curd.valid_username(username)
    if valid_name_result:
        raise AccountException(403, reason=valid_name_result)

    valid_pw_result = curd.valid_password(password)
    if valid_pw_result:
        raise AccountException(403, reason=valid_pw_result)
       
    curd.create(account_data)
    return ResponseBase(success = True)

@router.post("/api/account/verify", responses={
                                                    200: {"model": ResponseBase},
                                                    400: {"model": VerifyErrorBase},
                                                })
async def login(input_account: AccountBase, db: Session = Depends(get_db)):
    curd = AccountCrud(db)
    account = curd.get(input_account.username)
    if not account:
        raise VerifyException()
    
    is_valid = curd.verify(input_account.password, account.password)
    if is_valid == False:
        raise VerifyException()
        
    return ResponseBase(success = True)