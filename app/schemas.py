from pydantic import BaseModel, Field

class AccountBase(BaseModel):
    username: str = Field(title='帳號名稱')
    password: str = Field(title='帳號密碼')