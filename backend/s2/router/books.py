from fastapi import APIRouter, HTTPException, status

from pydantic import BaseModel

router = APIRouter()

books = []

class BookSchema(BaseModel):
    title: str
    author: str
    price: float

@router.get("/books")
async def getBooks():
    return books


@router.post("/books", status_code=201)
async def createBook(book: BookSchema):
    books.append(book.model_dump())

    return book

@router.get("/books/{book_id}")
def get_book(book_id: int):
    if book_id >= len(books):
        raise HTTPException(status_code=404, detail="Book not found")
    return books[book_id]

@router.delete("/books/{book_id}", status_code=204)
def delete_book(book_id: int):
    if book_id >= len(books):
        raise HTTPException(status_code=404, detail="Book not found")
    books.pop(book_id)

