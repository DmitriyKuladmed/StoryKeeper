from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from typing import List
from datetime import datetime

from .. import models, schemas, crud
from ..database import SessionLocal
from ..tasks import cancel_reservation


router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.Reservation)
def create_reservation(reservation: schemas.ReservationCreate, db: Session = Depends(get_db)):
    # Проверяем, что книга доступна для бронирования
    existing_reservation = crud.get_reservations_for_book(
        db, book_id=reservation.book_id, start_date=reservation.start_date, end_date=reservation.end_date
    )
    if existing_reservation:
        raise HTTPException(status_code=400, detail="Book is already reserved for the selected dates")

    reservation = crud.create_reservation(db=db, reservation=reservation)

    # Планируем задачу по отмене бронирования
    cancel_reservation.apply_async((reservation.id,), eta=reservation.end_date)

    return reservation


@router.get("/{reservation_id}", response_model=schemas.Reservation)
def read_reservation(reservation_id: int, db: Session = Depends(get_db)):
    db_reservation = crud.get_reservation(db, reservation_id=reservation_id)
    if db_reservation is None:
        raise HTTPException(status_code=404, detail="Reservation not found")
    return db_reservation


@router.delete("/{reservation_id}", response_model=schemas.Reservation)
def delete_reservation(reservation_id: int, db: Session = Depends(get_db)):
    return crud.cancel_reservation(db=db, reservation_id=reservation_id)


@router.get("/", response_model=List[schemas.Reservation])
def get_reservations(db: Session = Depends(get_db)):
    return crud.get_reservations(db=db)
