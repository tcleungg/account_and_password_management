from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.crud import AccountCrud
from app.schemas import AccountBase, ResponseBase, AccountErrorBase, VerifyErrorBase
from app.exception import AccountException, VerifyException
from app.db import SessionLocal
from utils import account

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
async def register(data: AccountBase, db: Session = Depends(get_db)):
    curd = AccountCrud(db)
    username = data.username
    password = data.password

    check_name_result = account.username_exist(db, username)
    if check_name_result:
        raise AccountException(403, reason=check_name_result)
    
    valid_name_result = account.valid_username(username)
    if valid_name_result:
        raise AccountException(403, reason=valid_name_result)

    valid_pw_result = account.valid_password(password)
    if valid_pw_result:
        raise AccountException(403, reason=valid_pw_result)
       
    curd.create(data)
    return ResponseBase(success = True)

@router.post("/api/account/verify", responses={
                                                    200: {"model": ResponseBase},
                                                    400: {"model": VerifyErrorBase},
                                                })
async def login(data: AccountBase, db: Session = Depends(get_db)):
    curd = AccountCrud(db)
    exist = curd.get(data.username)
    if not exist:
        raise VerifyException()
    
    is_valid = account.verify(data.password, exist.password)
    if is_valid == False:
        raise VerifyException()
        
    return ResponseBase(success = True)