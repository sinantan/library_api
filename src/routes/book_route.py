from fastapi import APIRouter, Depends, HTTPException
from fastapi_limiter.depends import RateLimiter

from src.helper.response_helper import Response
from src.model.book import Book
from src.routes.base_models.basemodels import BookResponse

book_router = APIRouter()


'''
RateLimiter ile yeni kitap eklenirken 5 saniyede sadece 2 isteğe izin vermesini sağlıyoruz.
'''
@book_router.post("/create_book")
async def create_book(book: BookResponse, dependencies=[Depends(RateLimiter(times=2, seconds=5))], status_code=201):
    book = Book.create(name = book.name, author = book.author, page_number = book.page_number)
    return Response(book,"New book created.",201)

@book_router.get("/list_books")
async def list_books(status_code=200):
    books = Book.all()
    return Response(books,"All books fetched.")

@book_router.put("/update_book/{id}", status_code=200)
async def update_book_data(id: int, book: BookResponse):
    b = Book.get_pk(id)
    if b is None:
        raise HTTPException(status_code=400, detail="Book not found!")
    b.name = book.name
    b.author = book.author
    b.page_number = book.page_number
    b.save()
    return Response(b, "Book updated succesfully.")

@book_router.delete("/delete_book/{id}")
async def delete_book(id:int):
    book = Book.get_pk(id)
    if book is not None:
        book.delete()
        return Response([],"Book deleted succesfully.")
    raise HTTPException(status_code=400, detail="Book not found!")



