import datetime

from sqlalchemy import Column, DateTime, Boolean, Integer
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import session



'''
Tüm modellerimizde ortak olan mixinimiz.
'''
class BaseMixin(object):
    id = Column(Integer, primary_key=True, index=True)
    created_at = Column(DateTime(), index=True, nullable=False, default=datetime.datetime.now())
    active = Column('is_active', Boolean(), nullable=False, server_default='1', index=True)
    updated_at = Column(DateTime(), index=True, nullable=True, default=datetime.datetime.now(), onupdate=datetime.datetime.now())

    def __repr__(self):
        return f"{self.__class__.__name__}<{self.id}>"

    def save(self):
        try:
            session.add(self)
            session.flush()
            session.commit()
            return self
        except IntegrityError:
            session.rollback()
        except Exception as e:
            session.rollback()

    @classmethod
    def create(cls, **kw):
        return cls(**kw).save()

    @classmethod
    def all(cls, *arg):
        return cls.query.filter(*arg).order_by(cls.updated_at.desc()).all()

    @classmethod
    def filter(cls, *arg):
        return cls.query.filter(*arg)

    def delete(self):
        session.delete(self)
        session.commit()

    @classmethod
    def get_pk(cls, id_):
        try:
            return cls.get(cls.id == id_)
        except Exception as e:
            session.rollback()

