from app.db.database import engine, Base
from app.db.models import Book

Base.metadata.create_all(bind=engine)
