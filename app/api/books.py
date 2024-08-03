from fastapi import APIRouter, HTTPException, Depends
from typing import List
from sqlalchemy.future import select
from sqlalchemy.orm import sessionmaker, Session
from app.db import models, schemas, database
from app.core.openai_client import generate_summary

router = APIRouter()

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=database.engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/books", response_model=schemas.Book)
async def create_book(book: schemas.BookCreate, db: Session = Depends(get_db)):

    summary = generate_summary(f"Title: {book.title}\nPublisher: {book.publisher}\nText: {book.text}")
    

    new_book = models.Book(
        title=book.title,
        publisher=book.publisher,
        text=book.text,
        summary=summary
    )
    

    db.add(new_book)
    db.commit()
    db.refresh(new_book)
    
    return new_book



@router.get("/books", response_model=List[schemas.Book])
async def read_books(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    query = select(models.Book).offset(skip).limit(limit)
    result = db.execute(query)
    books = result.scalars().all()
    return books



@router.get("/books/{book_id}", response_model=schemas.Book)
async def read_book(book_id: str, db: Session = Depends(get_db)):
    query = select(models.Book).where(models.Book.id == book_id)
    result = db.execute(query)
    book = result.scalar_one_or_none()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    return book



@router.put("/books/{book_id}", response_model=schemas.Book)
async def update_book(book_id: str, book: schemas.BookUpdate, db: Session = Depends(get_db)):
    query = select(models.Book).where(models.Book.id == book_id)
    result = db.execute(query)
    existing_book = result.scalar_one_or_none()
    if existing_book is None:
        raise HTTPException(status_code=404, detail="Book not found")
    

    summary = generate_summary(f"Title: {book.title}\nPublisher: {book.publisher}\nText: {book.text}")
    

    existing_book.title = book.title
    existing_book.publisher = book.publisher
    existing_book.text = book.text
    existing_book.summary = summary
    
    db.commit()
    db.refresh(existing_book)
    
    return existing_book



@router.delete("/books/{book_id}", response_model=schemas.Book)
async def delete_book(book_id: str, db: Session = Depends(get_db)):
    query = select(models.Book).where(models.Book.id == book_id)
    result = db.execute(query)
    book = result.scalar_one_or_none()
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    db.delete(book)
    db.commit()
    
    return book