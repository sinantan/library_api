from pydantic.main import BaseModel

class UserResponse(BaseModel):
    first_name: str
    last_name: str
    identity_number: int

class BookResponse(BaseModel):
    name: str
    author: str
    page_number: int

class BorrowResponse(BaseModel):
    user_id: int
    book_id: int
    expire_date: str #'18/09/21' şeklinde olmalı.