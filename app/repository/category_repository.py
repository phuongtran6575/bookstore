from sqlmodel import Session, select
from models.category_model import Category

async def get_category_by_id(id: int, session: Session):
    statement = select(Category).where(Category.id == id)
    category_db = session.exec(statement).first()
    return category_db

async def create_category(category: Category, session: Session):
    session.add(category)
    session.commit()
    session.refresh(category)
    return category

async def delete_category(id: int, session: Session):
    statement = select(Category).where(Category.id == id)
    category_db = session.exec(statement).first()
    session.delete(category_db)
    session.commit()
    return {"status": "deleted", "id": id}

async def update_category(category: Category, session: Session):
    statement = select(Category).where(Category.id == category.id)
    category_db = session.exec(statement).first()
    category_db.name = category.name
    session.add(category_db)
    session.commit()
    session.refresh(category_db)
    return {"status": "update", "id": category.id}

async def get_all_categories(session: Session):
    statement = select(Category)
    categories_db = session.exec(statement).all()
    return categories_db