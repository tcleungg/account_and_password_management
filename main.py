from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app import models
from app.db import engine
from app.exception import AccountException, VerifyException
from route import router
from utils import token
import middleware 

models.Base.metadata.create_all(bind=engine, checkfirst=True)

app = FastAPI()
app.include_router(router)

# midleware
from starlette.middleware.sessions import SessionMiddleware
app.middleware("http")(middleware.login_times_middlware)
app.add_middleware(SessionMiddleware, secret_key='sessionKey', max_age=84600)

# expection_handler
@app.exception_handler(AccountException)
async def account_exception_handler(request: Request, exc: AccountException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"success": exc.success,
                "reason": exc.reason},
    )

@app.exception_handler(VerifyException)
async def verify_exception_handler(request: Request, exc: VerifyException):
    response = JSONResponse(
                            status_code=exc.status_code,
                            content={"success": exc.success,
                                    "reason": exc.reason},
                        )
    token.record_attempt_times(request)
    return response