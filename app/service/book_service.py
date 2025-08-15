from repository import book_repository
from repository.book_repository import get_all_books, get_book_by_id, create_book, delete_book, update_book
from sqlmodel import Session
from models.book_model import Book

async def get_book_by_id(book_id: int, session: Session):
    return await book_repository.get_book_by_id(book_id, session)

async def create_book(book: Book, session: Session):
    return await book_repository.create_book(book, session)

async def delete_book(book_id: int, session: Session):
    return await book_repository.delete_book(book_id, session)

async def update_book(book: Book, session: Session):
    return await book_repository.update_book(book, session)

async def get_all_books(session: Session):
    return await book_repository.get_all_books(session)