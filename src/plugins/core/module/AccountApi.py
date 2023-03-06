from src.plugins.core.module.BaseBFbanPackage import BaseBFbanPackage, BaseApiList
from src.plugins.core.module.user.login import login, logout

"""
账户接口，需权限
"""


class AccountApi(BaseBFbanPackage):
    def __init__(self):
        self.API.user.login = login
        self.API.user.logout = logout
