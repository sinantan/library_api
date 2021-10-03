import datetime

from fastapi import APIRouter, HTTPException

from src.helper.response_helper import Response
from src.model.book import BorrowedBook
from src.routes.base_models.basemodels import BorrowResponse

borrow_router = APIRouter()

@borrow_router.post("/create_borrow")
async def create_borrow(data: BorrowResponse, status_code=201):
    book = BorrowedBook.filter(BorrowedBook.book_id == data.book_id, BorrowedBook.active == True).first()
    if len(book) > 0:
        raise HTTPException(status_code=400, detail="This book has been borrowed!")
    expire_date = data.expire_date
    expire_date = datetime.strptime(expire_date, '%d/%m/%y') #'12/08/21' şeklinde aldığımız inputu dbye yazmak için datetime formatına çeviriyoruz.
    book = BorrowedBook.create(user_id = data.user_id, book_id = data.book_id, expire_date = expire_date)
    return Response(book,"Borrowed succesfully.",201)

@borrow_router.put("/cancel_borrow")
async def cancel_borrow(data: BorrowResponse, status_code=200):
    borrowed_book = BorrowedBook.filter(BorrowedBook.user_id == data.user_id, BorrowedBook.book_id == data.book_id, BorrowedBook.active == True).first()
    if len(borrowed_book) > 0:
        borrowed_book.toggle_active()
        borrowed_book.updated_at = datetime.datetime.now() #Cancel durumuna geçen ödünç alımlar db'den silinmek yerine pasife alınır.
        return Response(borrowed_book, "Borrowed book cancelled succesfully", 201)
    raise HTTPException(status_code=400, detail="Borrow records not are matching.")