from src.plugins.core.module.BaseBFbanPackage import BaseBFbanPackage, BaseApiList
from src.plugins.core.module.statistics.index import statistics, activities

"""
公共接口类，无需鉴权
"""

class PublicApi(BaseBFbanPackage):
    def __init__(self):
        self.API.statistics = statistics
        self.API.activities = activities
