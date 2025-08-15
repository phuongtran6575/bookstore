from fastapi import APIRouter
from service import book_service
from database.sqlite_database import SessionDepends
from models.book_model import Book
from service.book_service import get_all_books, get_book_by_id, create_book, delete_book, update_book
router = APIRouter(prefix="/book", tags=["book"])

@router.get("/book/{book_id}")
async def get_book_by_id(book_id: int, session: SessionDepends):
    return await book_service.get_book_by_id(book_id, session)


@router.get("/books")
async def get_all_books(session: SessionDepends):
    return await book_service.get_all_books(session)

@router.post("/book")
async def create_book(book: Book, session: SessionDepends):
    return await book_service.create_book(book, session)

@router.put("/book")
async def update_book(book:Book, session: SessionDepends):
    return await book_service.update_book(book, session)

@router.delete("/book/{book_id}")
async def delete_book(book_id: int, session: SessionDepends):
    return await book_service.delete_book(book_id, session)

