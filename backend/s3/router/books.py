# use soemthing we call API Router
from fastapi import APIRouter

router = APIRouter()

# unlike the way we do @app.HTTP_METHOD(get, post, put,patch)

# if it is successful, tell teh client we had an error

@router.get("/books", status_code=500)
async def get_books():
    return {"message": "Fetching books..."}