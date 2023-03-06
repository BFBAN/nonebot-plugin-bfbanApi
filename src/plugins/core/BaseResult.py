class BaseResult(object):
    """
    返回联ban返回的code
    """
    code = 0

    """
    如果失败则1
    """
    error = 0

    """
    如果成功则1
    """
    susses = 0

    """
    对应结果消息
    """
    message = ""

    def __init__(self, data):
        self.code = data.code
        self.error = data.error
        self.susses = data.susses
        self.message = data.message
