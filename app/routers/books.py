from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy.orm import Session

from typing import List, Optional

from .. import crud, schemas
from ..database import SessionLocal

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/", response_model=schemas.Book)
def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):
    db_book = crud.create_book(db=db, book=book)
    return db_book


@router.get("/{book_id}", response_model=schemas.Book)
def read_book(book_id: int, db: Session = Depends(get_db)):
    db_book = crud.get_book(db, book_id)
    if db_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return db_book


@router.get("/", response_model=List[schemas.Book])
def get_books(
    db: Session = Depends(get_db),
    author_id: Optional[int] = Query(None, description="Filter books by author ID"),
    genre_ids: Optional[List[int]] = Query(None, description="Filter books by genre IDs"),
    min_cost: Optional[int] = Query(None, description="Minimum cost for filtering"),
    max_cost: Optional[int] = Query(None, description="Maximum cost for filtering")
):
    books = crud.filter_books(db, author_id=author_id, genre_ids=genre_ids, min_cost=min_cost, max_cost=max_cost)
    return books
