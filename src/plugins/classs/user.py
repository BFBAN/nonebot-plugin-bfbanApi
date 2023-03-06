class BaseUserData:
    """
    基本用户类
    """

    id = 0
    userAvatar = ""
    username = ""


class UserData(BaseUserData):
    """
    网站用户类
    """

    attr = {}
    joinTime = ""
    lastOnlineTime = ""
    origin = {}
    privilege = []


class PlayerData(BaseUserData):
    """
    案件玩家
    """

    avatarLink = ""
    games = []
    cheatMethods = []
    history = []
    originName = ""
    originPersonaId = ""
    originUserId = ""
    commentsNum = 0
    viewNum = 0
    status = 0
    createTime = ""
    updateTime = ""
