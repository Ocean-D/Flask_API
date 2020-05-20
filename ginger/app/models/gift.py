from app.models.base import Base
from sqlalchemy import Column,Integer,ForeignKey,String,SmallInteger
from sqlalchemy.orm import relationship

class Gift(Base):
    id  = Column(Integer,primary_key=True)
    user = relationship('User')
    uid = Column(Integer,ForeignKey('user.id'))
    isbn = Column(String(18),nullable=False)
    launched = Column(SmallInteger,default=1)


