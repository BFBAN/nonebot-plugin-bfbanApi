"""
接口信息
"""
import json
from string import Template


class InterfaceInfo:
    __dictionary_path = "src/plugins/config/api.json"
    __baseLocal = "https://bfban.gametools.network/api"

    dictionary = None
    url = ""

    def __init__(self, name):
        if name != "":
            self.url = name
        with open(self.__dictionary_path, 'r', encoding='utf8') as fp:
            self.dictionary = json.load(fp)

    # 取得完整地址
    def address(self):
        _baseLocal = self.__baseLocal
        _url = self.dictionary.get(self.url)
        if _url is None:
            _url = ""
            print(f"""
没有找到字典对应地址\n
可以访问`https://github.com/BFBAN/bfban-website/blob/master/front/src/assets/js/api.js`来克隆内部地址，把它放到 {self.__dictionary_path}
            """)
        return Template("${s1}/${s2}").safe_substitute(s1=_baseLocal, s2=_url)
