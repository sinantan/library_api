
from sqlalchemy.orm import backref, relationship

from src.lib.extensions import Base
from src.model.mixin.base_mixin import BaseMixin
from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, DateTime


class Book(Base, BaseMixin):
    __tablename__='book'
    name=Column(String(255),nullable=False)
    author=Column(String(255),nullable=True, default="unspecified")
    page_number=Column(Integer, nullable=True, default=0)


class BorrowedBook(Base, BaseMixin):
    user_id = Column(Integer(), ForeignKey('user.id'), index=True)
    book_id = Column(Integer(), ForeignKey('book.id'), index=True)
    book = relationship('Book', backref=backref('borrowed_by'))
    is_expired = Column(Boolean(), nullable=False, server_default='0', index=True) #Ödünç alınan kitabın bekleme süresinin geçip geçmediğinin set edildiği yer
    borrowed_by = relationship('User', backref=backref('borrowed_books'))
    expire_date = Column(DateTime(), index=True, nullable=False) #Expire date, user kitabı aldıktan sonra geri vermesi için gereken son tarihi gösterir.


    def toggle_active(self): #Bir kullanıcı kitabı kütüphaneye geri bıraktığında "active" durumu False olur.
        self.active = not self.active
        self.save()