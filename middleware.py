from fastapi import Request
from fastapi.responses import JSONResponse
from utils import token

async def login_times_middlware(request:Request, call_next):
    # use this middleware only on verify api
    if request.url.path != "/api/account/verify":
        return await call_next(request)
    
    session = request.session
    
    # check login attempts times and ban times
    if token.forbidden_login(session):
        body = {"success": False,
                "reason": "Too many failed login attempts try again later."}
        return JSONResponse(status_code=429, content=body) 
    
    response = await call_next(request)

    # reset login attempts times
    if response.status_code == 200:
        session["attempt_times"] = 0

    # update session
    if session:
        response.set_cookie(key='session', value=request.cookies.get('session'), httponly=True)
    
    return response