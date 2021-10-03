from sqlalchemy.orm import relationship, backref

from src.lib.extensions import Base
from src.model.mixin.base_mixin import BaseMixin
from sqlalchemy import Column, String, Integer


class User(Base, BaseMixin):
    __tablename__='user'
    first_name=Column(String(255),nullable=False)
    last_name=Column(String(255),nullable=False)
    identity_number=Column(Integer,nullable=False, unique=True)
    borrowed_books = relationship('Book', secondary='borrowed_book', backref=backref('users', lazy='dynamic'))

    @property
    def full_name(cls):
        return cls.first_name + " " + cls.last_name
