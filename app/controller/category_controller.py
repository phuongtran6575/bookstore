from fastapi import APIRouter
from service import category_service
from database.sqlite_database import SessionDepends
from models.category_model import Category
from service.category_service import get_all_categories, get_category_by_id, delete_category, update_category, create_category

router = APIRouter(prefix="/category", tags= ["category"])

@router.get("catgory/{category_id}")
async def get_category_by_id(category_id: int, session: SessionDepends):
    return await category_service.get_category_by_id(category_id, session)

@router.get("/categories")
async def get_all_categories(session: SessionDepends):
    return await category_service.get_all_categories(session)

@router.post("/category")
async def create_category(category:Category,session: SessionDepends):
    return await category_service.create_category(category, session)

@router.put("/category")
async def update_category(session: SessionDepends):
    return await category_service.update_category(category, session)

@router.delete("/category")
async def delete_Category(category_id: int, session: SessionDepends):
    return await category_service.delete_category(category_id, session)
