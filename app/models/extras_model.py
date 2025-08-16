from sqlmodel import SQLModel, Field

class Authors(SQLModel):
    id: int = Field(default= None, primary_key=True)
    name: str
    bio: str

class Publisher(SQLModel):
    id: int = Field(default= None, primary_key=True)
    name: str
    address: str

class BookImage(SQLModel):
    id: int = Field(default= None, primary_key=True)
    image_url: str
    is_thumbnail: bool


class Review(SQLModel):
    id: int = Field(default= None, primary_key=True)
    book_id: int
    user_id: int
    rating: int
    comment: str