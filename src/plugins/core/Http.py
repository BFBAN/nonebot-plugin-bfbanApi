from src.plugins.core.BaseResult import BaseResult
from src.plugins.core.InterfaceInfo import InterfaceInfo


class Http:
    @staticmethod
    def request(name) -> BaseResult:
        url_info = InterfaceInfo()
        url_info.url = name

        print(url_info.address())

        return BaseResult({
            "code": "back.error",
            "error": 1
        })

    def post(self, name) -> BaseResult:
        return self.request(name)

    def get(self, name) -> BaseResult:
        return self.request(name)
