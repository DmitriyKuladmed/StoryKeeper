from fastapi import FastAPI

from . import models
from .database import engine
from .routers import books, reservations, genres, users

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(books.router, prefix="/books", tags=["books"])
app.include_router(reservations.router, prefix="/reservations", tags=["reservations"])
app.include_router(users.router, prefix="/users", tags=["users"])
app.include_router(genres.router, prefix="/genres", tags=["genres"])
