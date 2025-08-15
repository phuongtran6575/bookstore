from sqlmodel import Session, select
from models.book_model import Book


async def get_book_by_id(id: int, session: Session):
    statement = select(Book).where(Book.id == id)
    book_db = session.exec(statement).first()
    return book_db

async def create_book(book: Book, session: Session):
    session.add(book)
    session.commit()
    session.refresh(book)
    return book

async def delete_book(id: int, session: Session):
    statement = select(Book).where(Book.id == id)
    book_db = session.exec(statement).first()
    session.delete(book_db)
    session.commit()
    return {"status": "deleted", "id": id}

async def update_book(book: Book, session: Session):
    statement = select(Book).where(Book.id == book.id)
    book_db = session.exec(statement).first()
    book_db.name = book.name
    session.add(book_db)
    session.commit()
    session.refresh(book_db)
    return {"status": "update", "id": book.id}

async def get_all_books(session: Session):
    statement = select(Book)
    books_db = session.exec(statement).all()
    return books_db