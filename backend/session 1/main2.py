from fastapi import FastAPI

app = FastAPI() #creating the kitchen

# decorator POST, GET, DELETE, PATCH, PUT, ...
@app.get("/")
def root():
    return {
        "message": "Server is Live!"
    }

# food
@app.post("/food/{food}")
def foodies(food:str):

    return {
        "message": "I love " + food
    }


# ==> dictionary to a JSON format 

# route for name
# root route
# route for class/level/grade etc