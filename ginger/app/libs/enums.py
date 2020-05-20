

from enum import Enum

class ClientTypeEnum(Enum):
    USER_EMAIL = 100
    USER_MOBILE = 101

    #小程序
    USER_MAIN = 200
    #Wechat公众号
    USER_WX = 201