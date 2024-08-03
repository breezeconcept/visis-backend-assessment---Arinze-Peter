from sqlalchemy import Column, String, Text
from app.db.database import Base
import uuid

class Book(Base):
    __tablename__ = 'books'
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String, index=True)
    publisher = Column(String, index=True)
    text = Column(Text)
    summary = Column(Text)

    def __repr__(self):
        return f"Book Title({self.title}, with Publisher {self.publisher})"
