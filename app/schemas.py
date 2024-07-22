from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional


class UserBase(BaseModel):
    first_name: str
    last_name: str
    avatar: Optional[str] = None


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int

    class Config:
        orm_mode = True


class GenreBase(BaseModel):
    name: str


class GenreCreate(GenreBase):
    pass


class Genre(GenreBase):
    id: int

    class Config:
        orm_mode = True


class BookBase(BaseModel):
    title: str
    cost: int
    pages: int
    author_id: int


class BookCreate(BaseModel):
    title: str
    cost: int
    pages: int
    author_id: int
    genre_ids: Optional[List[int]] = None


class BookUpdate(BookBase):
    genre_ids: List[int] = []


class Book(BookBase):
    id: int
    author: User
    genres: List[Genre] = []

    class Config:
        orm_mode = True


class ReservationBase(BaseModel):
    book_id: int
    user_id: int
    start_date: datetime
    end_date: datetime


class ReservationCreate(ReservationBase):
    pass


class Reservation(ReservationBase):
    id: int
    active: bool

    class Config:
        orm_mode = True
