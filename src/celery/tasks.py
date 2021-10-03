import datetime

from src.celery.celery_worker import celery
from src.model.book import BorrowedBook


'''
Kütüphaneden kitap alındığında 14 gün içerisinde geri götürmesi gerekiyor. Eğer 14 gün içerisinde götürmezse ilgili
kayıt pasif duruma geçiyor ve kitap başkaları tarafından alınabiliyor. bu task düzenli olarak her akşam 11'de çalışıyor.
'''
@celery.task
def check_expire_date():
    start_date = datetime.datetime.now().date() - datetime.timedelta(days=15)
    end_date = datetime.datetime.now().date() - datetime.timedelta(days=14)
    borrow_records = BorrowedBook.filter(BorrowedBook.created_at.between(start_date, end_date), BorrowedBook.active == True).all()
    for borrow_record in borrow_records:
        borrow_record.active = False
        borrow_record.is_expired = True
        borrow_record.save()
    return "check_expire_date task succeed."