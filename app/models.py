from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, Date
from app.db import Base

class Account(Base):
    __tablename__ = "accounts"
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String, unique=True, nullable=False, index = True)
    password = Column(String, nullable=False)
    create_time = Column(Date(), server_default=func.now())
    update_time = Column(Date(), server_default=func.now(), onupdate=func.now())
