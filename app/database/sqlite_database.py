from sqlmodel import Session, create_engine, SQLModel
from typing import Annotated
from fastapi import Depends
from models.book_model import Book
from models.category_model import Category
from models.user_model import User

engine = create_engine("sqlite:///bookstore.db", echo=True)
SQLModel.metadata.create_all(engine)
def get_session():
    with Session(engine) as session:
        yield session

SessionDepends = Annotated[Session, Depends(get_session)] 
#SessionDepends: Session = Depends(get_session)