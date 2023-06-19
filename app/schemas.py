from pydantic import BaseModel, Field

class AccountBase(BaseModel):
    username: str = Field(title='帳號名稱')
    password: str = Field(title='帳號密碼')

class ResponseBase(BaseModel):
    success: bool

class AccountErrorBase(BaseModel):
    success: bool
    reason: str

    class Config:
        schema_extra = {
            "example": {"success": "false",
                        "reason": "Username already exists."},
        }