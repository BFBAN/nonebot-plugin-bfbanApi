class BaseApiUserList:
    login = None
    logout = None
    me = None
    info = None
    reports = None

class BaseApiList:
    statistics = None
    activities = None
    user = BaseApiUserList()


class BaseBFbanPackage:
    API = BaseApiList()

    # def clearAllApi(self):
    # self.API.clear()
