from src.plugins.core.BaseBFbanPackage import BaseBFbanPackage

"""
账户接口，需权限
"""


class AccountApi(BaseBFbanPackage):
    accountApi = {}

    def __init__(self):
        self.API.update(self.accountApi)
