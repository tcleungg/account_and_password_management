from fastapi import APIRouter
from fastapi import Depends
from sqlalchemy.orm import Session

from app.crud import AccountCrud
from app.schemas import AccountBase
from app.db import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post(f'/api/account/register', status_code=200)
async def register(account_data: AccountBase, db: Session = Depends(get_db)):
    curd = AccountCrud(db)
    
    curd.create(account_data)
    return {"success": True}
