from fastapi import FastAPI

app = FastAPI() # created kitchen

@app.post("/") #if someone requests at / with POST, GET
def root():

    # Process 
    return {"message": "Mama Put is open"}

@app.get("/rice")
def getRice():
    return {"message": "Rice is available"}

@app.get("/beans")
def getBeans():
    return {"message": "Beans is available"}


# => Web runs on Javascript { JSON :: Javascript Object Notation }