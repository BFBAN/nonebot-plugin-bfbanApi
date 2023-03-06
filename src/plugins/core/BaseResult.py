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

    def __init__(self, data=None):
        if data:
            if data.code:
                self.code = data.code
            if data.error:
                self.error = data.error
            if data.susses:
                self.susses = data.susses
            if data.message:
                self.message = data.message
