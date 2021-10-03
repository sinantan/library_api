library_api
-

Simple library api powered by <b>Fastapi</b>, <b>Postgresql</b>, <b>Celery</b> & <b>Redis</b>

Installing requirements:

`pip install -r requirements.txt`

Running:

`python app.py` for vanilla start
 
 or

`docker run -p 8080:8080 --name my-api test/library_api:0.1` run with docker

Routes:
-
### Book Routes

Params -->  name: str
            author: str
            page_number: int

`/create_book <POST>`

`/list_books <GET>`

`/update_book/{id} <PUT>`

`/delete_book/{id} <DELETE>`

### BorrowBook Routes

Params -->  user_id: int
            book_id: int
            expire_date: str

`/create_borrow <POST>`

`/cancel_borrow <PUT>`

### User Routes

Params -->  first_name: str
            last_name: str
            identity_number: int

`/create_user <POST>`

`/list_users <GET>`

`/update_user/{id} <PUT>`

`/delete_user/{id} <DELETE>`