import re
from passlib.context import CryptContext

from app.crud import AccountCrud

def username_exist(db, username):
    curd = AccountCrud(db)
    if curd.get(username):
        return "Username already exists"
    return None

def verify(input_password, password):
    ctx = CryptContext(schemes=["sha256_crypt"])
    return ctx.verify(input_password, password)

def valid_username(username):
    length = len(username)
    if length < 3 or length > 32:
        return "The Username should be minimum 3, maximum 32."
    return None

def valid_password(password):
    length = len(password)
    if length < 8 or length > 32:
        return "The Password should be minimum 8, maximum 32."
    elif re.search('[0-9]',password) is None:
        return "The Password should contain at least 1 digit (0-9)."
    elif re.search('[a-z]',password) is None: 
        return "The Password should contain at least 1 lowercase letter (a-z)."
    elif re.search('[A-Z]',password) is None:
        return "The Password should contain at least 1 uppercase letter (A-Z)."