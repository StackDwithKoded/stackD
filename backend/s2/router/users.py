from fastapi import APIRouter
from fastapi import HTTPException, status

router = APIRouter()

@router.post("/create-user/{name}") # instead of @app
async def createUser(name: str):
    return {"message": "Create User"}

@router.get("/users", status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
async def getUsers():
    if HTTPException:
        return {"error": "Something went wrong"}
    return {"message": "Get Users"}