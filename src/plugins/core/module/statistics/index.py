from nonebot_plugin_bfbanApi.core.Http import Http

http = Http()

def statistics():
    return http.post("a")


def activities():
    return http.post("b")
