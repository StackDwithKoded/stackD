from fastapi import FastAPI

from router import users, books

from fastapi .middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"]
)

app.include_router(users.router)

app.include_router(books.router)

@app.get("/")
async def root():
    return {"message": "Server is Live!"}

