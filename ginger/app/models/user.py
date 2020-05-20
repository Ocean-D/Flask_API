import datetime

from sqlalchemy import Column, String, Integer,SmallInteger
from werkzeug.security import generate_password_hash, check_password_hash

from app.libs.error_code import NotFound, AuthFailed
from app.models.base import db
from app.models.base import Base


class User(Base):
    id = Column(Integer,primary_key=True)
    nickname = Column(String(24),unique=True,nullable=False)
    email = Column(String(20),unique=True)
    auth = Column(SmallInteger,default=1)
    _password = Column('password',String(100))


    def keys(self):
        return ['id','nickname','email','auth']




    @property
    def password(self):
        return self._password


    @password.setter
    def password(self,raw):
        self._password = generate_password_hash(raw)


    #注册用户
    @staticmethod
    def register_by_email(nickname,account,secret):
        with db.auto_commit():
            user = User()
            user.nickname = nickname
            user.email = account
            user.password = secret
            db.session.add(user)



   #登录验证
    @staticmethod
    def verify(email,password):
        user = User.query.filter_by(email=email).first_or_404()
        # if not user:
        #     raise NotFound(msg='not found user')
        if not user.check_password(password):
            return AuthFailed()
        scope = 'AdminScope' if user.auth == 2 else 'UserScope'
        return {'uid':user.id,'scope':scope}


    def check_password(self,raw):
        if not self._password:
            return False
        return check_password_hash(self._password,raw)