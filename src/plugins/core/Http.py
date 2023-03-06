import httpx as httpx

from src.plugins.core.BaseResult import BaseResult
from src.plugins.core.InterfaceInfo import InterfaceInfo

class Http:
    def post(self, name, data = {}) -> BaseResult:
        url_info = InterfaceInfo(name)
        result = httpx.post(url_info.address(), data=data).json()
        return BaseResult(code=result.code, susses=result.susses)

    def get(self, name, params) -> BaseResult:
        url_info = InterfaceInfo(name)
        result = httpx.get(url_info.address(), params=params).json()
        return BaseResult(code=result.code, susses=result.susses)
