from sqlalchemy.orm import Session
from sqlalchemy import and_

from datetime import date
from typing import List, Optional

from . import models, schemas


def get_book(db: Session, book_id: int):
    return db.query(models.Book).filter(models.Book.id == book_id).first()


def create_book(db: Session, book: schemas.BookCreate):
    db_book = models.Book(
        title=book.title,
        cost=book.cost,
        pages=book.pages,
        author_id=book.author_id
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)

    for genre_id in book.genre_ids:
        genre = db.query(models.Genre).filter(models.Genre.id == genre_id).first()
        if genre:
            db_book.genres.append(genre)

    db.commit()
    db.refresh(db_book)
    return db_book


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_genre(db: Session, genre_id: int):
    return db.query(models.Genre).filter(models.Genre.id == genre_id).first()


def create_genre(db: Session, genre: schemas.GenreCreate):
    db_genre = models.Genre(**genre.dict())
    db.add(db_genre)
    db.commit()
    db.refresh(db_genre)
    return db_genre


def create_reservation(db: Session, reservation: schemas.ReservationCreate):
    db_reservation = models.Reservation(**reservation.dict())
    db.add(db_reservation)
    db.commit()
    db.refresh(db_reservation)
    return db_reservation


def get_reservations_for_book(db: Session, book_id: int, start_date: date, end_date: date):
    return db.query(models.Reservation).filter(
        models.Reservation.book_id == book_id,
        models.Reservation.start_date <= end_date,
        models.Reservation.end_date >= start_date
    ).all()


def get_books(db: Session):
    return db.query(models.Book).all()


def get_users(db: Session):
    return db.query(models.User).all()


def get_genres(db: Session):
    return db.query(models.Genre).all()


def get_reservations(db: Session):
    return db.query(models.Reservation).all()


def filter_books_by_author(db: Session, author_id: int):
    return db.query(models.Book).filter(models.Book.author_id == author_id).all()


def filter_books_by_genre(db: Session, genre_ids: List[int]):
    return db.query(models.Book).join(models.book_genre_association).filter(
        models.book_genre_association.c.genre_id.in_(genre_ids)).all()


def filter_books_by_cost(db: Session, min_cost: int, max_cost: int):
    return db.query(models.Book).filter(and_(models.Book.cost >= min_cost, models.Book.cost <= max_cost)).all()


def filter_books(db: Session, author_id: Optional[int] = None, genre_ids: Optional[List[int]] = None,
                 min_cost: Optional[int] = None, max_cost: Optional[int] = None):
    query = db.query(models.Book)

    if author_id:
        query = query.filter(models.Book.author_id == author_id)

    if genre_ids:
        query = query.join(models.book_genre_association).filter(
            models.book_genre_association.c.genre_id.in_(genre_ids))

    if min_cost is not None and max_cost is not None:
        query = query.filter(and_(models.Book.cost >= min_cost, models.Book.cost <= max_cost))

    return query.all()