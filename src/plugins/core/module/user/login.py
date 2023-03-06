from src.plugins.core.module.statistics.index import http

def signin(data={}):
    return http.post("account_signin", {
        "data": {
            "username": data.username,
            "password": data.password
        },
        "encryptCaptcha": data.captcha.hash,
        "captcha.py": data.captcha.value
    })


def signup(token=""):
    """
    如果不提供，则使用注册的token
    """
    return http.post("account_signup")
