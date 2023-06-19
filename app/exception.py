from fastapi import FastAPI
from fastapi.exceptions import HTTPException
from pydantic import BaseModel

class AccountException(Exception):
    def __init__(self, status_code: int, reason:str):
        self.success = False
        self.status_code = status_code
        self.reason = reason