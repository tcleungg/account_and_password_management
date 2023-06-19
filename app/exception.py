
class AccountException(Exception):
    def __init__(self, status_code: int, reason:str):
        self.success = False
        self.status_code = status_code
        self.reason = reason

class VerifyException(Exception):
    def __init__(self, status_code: int = 400, reason: str = "Incorrect username or password."):
        self.success = False
        self.status_code = status_code
        self.reason = reason