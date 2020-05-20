


class Scope:
    def add(self,other):
        self.allow_api = self.allow_api + other.allow_api

class AdminScope(Scope):
    allow_api = ['v1.super_get_user']
    def __init__(self):
        self.add(UserScope())





class UserScope(Scope):
    allow_api = ['v1.A','v1.B','v1.super_get_user']









def is_in_scope(scope,endpoint):
    #反射
    #scope是个字符串
    gl = globals()
    # scope = globals()[scope]()
    if endpoint in scope.allow_api:
        return True
    else:
        return False
