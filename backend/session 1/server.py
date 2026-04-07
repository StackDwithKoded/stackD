from fastapi import FastAPI
import uvicorn

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Mama Put is open"}

@app.get("/rice")
def getRice():
    return {"message": "Rice is available"}

@app.get("/beans")
def getBeans():
    return {"message": "Beans is available"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)