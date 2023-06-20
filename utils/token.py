from datetime import datetime, timedelta

SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
ALGORITHM = "HS256"
TOKEN_EXPIRE_HOURS = 24
LOGIN_ATTEMPT_LIMIT = 5
LOGIN_BAN_MINS = 1

def forbidden_login(session):
    if "attempt_times" not in session.keys():
        return False
    
    if "ban_expires" in session.keys():
        expire = datetime.strptime(session["ban_expires"], "%Y-%m-%d %H:%M:%S")
        return True if expire > datetime.now() else False
        
def record_attempt_times(request):
    if "attempt_times" not in request.session.keys():
        request.session["attempt_times"] = 1
    else:
        request.session["attempt_times"] += 1

    if request.session["attempt_times"] % LOGIN_ATTEMPT_LIMIT == 0:
        ban_expires = datetime.now() + timedelta(minutes=LOGIN_BAN_MINS)
        request.session["ban_expires"] = ban_expires.strftime("%Y-%m-%d %H:%M:%S")

    
