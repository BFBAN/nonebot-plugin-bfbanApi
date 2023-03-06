from src.plugins.core.BaseBFbanPackage import BaseBFbanPackage

"""
公共接口类，无需鉴权
"""


class PublicApi(BaseBFbanPackage):
    publicApi = {
        'statistics': 1
    }

    def __init__(self):
        self.API.update(self.publicApi)
