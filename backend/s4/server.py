from fastapi import FastAPI

app = FastAPI()

#http methods ==> GET, POST, DELETE
@app.get("/")
async def root():
    return {"message": "Server is Live!"}

