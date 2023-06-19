from fastapi import APIRouter
from app import crud

router = APIRouter()

@router.get(f'/api/hello')
async def hello():
    return crud.hello_world()
