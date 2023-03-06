from src.plugins.core.Http import Http

http = Http()

def statistics():
    return http.post("statistics")


def activities():
    return http.post("activities")
