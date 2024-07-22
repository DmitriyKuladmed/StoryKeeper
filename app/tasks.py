from celery import Celery

from . import crud
from .database import SessionLocal

celery = Celery(__name__)
celery.conf.broker_url = 'redis://localhost:6379/0'


@celery.task
def cancel_reservation(reservation_id: int):
    db = SessionLocal()
    try:
        crud.cancel_reservation(db, reservation_id)
    finally:
        db.close()
