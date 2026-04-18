from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from router import books

app = FastAPI()

# Create our middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["localhost", "youtube.com"]
)

app.include_router(books.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}


# SEPARATION OF CONCERNS 

# each file only handles that function, users.py should only handle evrythtign relating to users