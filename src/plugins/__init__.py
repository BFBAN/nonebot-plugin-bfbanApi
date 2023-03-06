from src.plugins.core.module.PublicApi import PublicApi
from src.plugins.core.module.AccountApi import AccountApi

from src.plugins.classs.user import UserData


class AuthAccount:
    token = ""
    userData = UserData()


class BfbanInit(PublicApi, AccountApi):
    __account = AuthAccount()
    __debug = False

    def __init__(self):
        return None

    def token(self, value) -> bool:
        """
        设置身份\n
        在一些权限接口需要token来获取用户数据，如果没有仅能调用公共接口, 如果需要获取本地配置，使用`get_account`来获取\n
        如果需要获取永久token时间，前往开发组社区给账户申请机器人\n

        :param value: bfban Account token
        :return: bool
        """
        if value != "":
            self.__account.token = str(value).strip()
            return True
        return False

    # 获取账户配置
    def get_account(self) -> AuthAccount:
        """
        包含配置信息
        :return AuthAccount: 身份配置
        """
        return self.__account

    def debug(self, value):
        self.__debug = value
