from pydantic import BaseModel

class BookBase(BaseModel):
    title: str
    publisher: str
    text: str

class BookCreate(BookBase):
    pass

class BookUpdate(BookBase):
    summary: str

class Book(BookBase):
    id: str
    summary: str

    class Config:
        orm_mode = True

class BookText(BaseModel):
    text: str
