from fastapi import FastAPI
from app.db.database import database
from app.api import books
import logging

logging.basicConfig(level=logging.INFO)

app = FastAPI()

app.include_router(books.router, prefix="/api")

@app.get('/')
def status():
    return {"message": "Welcome to Text Summarizer API"}

@app.on_event("startup")
async def startup():
    try:
        await database.connect()
        logging.info("Database connected successfully.")
    except Exception as e:
        logging.error(f"Error connecting to the database: {e}")

@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, log_level="info")
