"""
接口信息
"""


class InterfaceInfo:
    baseLocal = "https://bfban.gametool.network"
    url = ""

    def __init__(self, name):
        self.url = name

    # 取得完整地址
    def address(self):
        _baseLocal = self.baseLocal
        _url = self.url
        return "{_baseLocal}/{_url}"
