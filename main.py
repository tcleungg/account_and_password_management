from fastapi import FastAPI

from app import models
from app.db import engine
from route import router

models.Base.metadata.create_all(bind=engine, checkfirst=True)

app = FastAPI()
app.include_router(router)
