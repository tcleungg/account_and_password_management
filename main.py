from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse

from app import models
from app.db import engine
from app.exception import AccountException
from route import router
models.Base.metadata.create_all(bind=engine, checkfirst=True)

app = FastAPI()
app.include_router(router)

@app.exception_handler(AccountException)
async def account_exception_handler(request: Request, exc: AccountException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"success": exc.success,
                "reason": exc.reason},
    )
