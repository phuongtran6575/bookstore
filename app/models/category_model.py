from sqlmodel import SQLModel, Field
class Category(SQLModel, table = True):
    id: int = Field(default = None, primary_key= True)
    name: str
    
    
class BookCategory(SQLModel):
    book_id: int
    category_id: int