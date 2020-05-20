from flask_sqlalchemy import SQLAlchemy as _SQLAlchemy, BaseQuery
from sqlalchemy import Column,SmallInteger,Integer
from contextlib import contextmanager
from datetime import datetime

from app.libs.error_code import NotFound


class SQLAlchemy(_SQLAlchemy):
    @contextmanager
    def auto_commit(self):
        try:
            yield
            self.session.commit()
        except Exception as e:
            db.session.rollback()
            raise e

class Query(BaseQuery):
    def filter_by(self,**kwargs):
        if 'status' not in kwargs.keys():
            kwargs['status'] = 1
        return super(Query,self).filter_by(**kwargs)

    def first_or_404(self):
        rv = self.first()
        if not rv:
            raise NotFound()
        return rv

    def get_or_404(self, ident):
        rv = self.get(ident)
        if not rv:
            return NotFound()
        return rv
db = SQLAlchemy(query_class=Query)


class Base(db.Model):
    __abstract__ = True
    create_time = Column('create_time',Integer)
    status = Column(SmallInteger,default=1)
    def __init__(self):
        self.create_time = int(datetime.now().timestamp())

    def __getitem__(self, item):
        return getattr(self, item)

    def keys(self):
        return self.fields

    def hide(self,*keys):
        for key in keys:
            self.fields.remove(key)
        return self
    def append(self,*keys):
        for key in keys:
            self.fields.append(key)
        return self



    @property
    def create_datetime(self):
        if self.create_time:
            return datetime.fromtimestamp(self.create_time)
        else:
            return None

    def delete(self):
        self.status = 0