from repository import category_repository
from repository.category_repository import get_all_categories, get_category_by_id, delete_category, update_category, create_category
from sqlmodel import Session
from models.category_model import Category

async def get_category_by_id(category_id: int, session: Session):
    return await category_repository.get_category_by_id(category_id, session)

async def create_category(category: Category, session: Session):
    return await category_repository.create_category(category, session)

async def delete_category(category_id: int, session: Session):
    return await category_repository.delete_category(category_id, session)

async def update_category(category: Category, session: Session):
    return await category_repository.update_category(category, session)

async def get_all_categories(session: Session):
    return await category_repository.get_all_categories(session)