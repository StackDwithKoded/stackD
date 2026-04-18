# First learnt a little about python

name = "Koded" # data types: strings, integers, floats, bool(true/false)
age = 90
height = 18.9
isRaining = False
isLight = True

# talk conditions
# IF, ELIF, ELSE

if ( 5 > 10):
    print("5 is greater than 10")
else:
    print("5 is not greater than 10")

if (isRaining & isLight):
    print("Netflix and Chill")
elif (isRaining and not isLight):
    print("Chill")
else:
    print("No Netflix and chill")


# OPERATORS: AND, OR, XOR, 
# AND as true when both inputs are true represented with & ==> *
# OR as true if at least one input is True represented with | ==> +


# Functions
def greetKoded():
    print("Hello Koded")

greetKoded() # FastAPI: can only call a function when an endpoint is triggered

# ARguments/ parameters and VALUES

def greet(name: str):
    print(f"Hello {name}")

greet("Koded")


# CREATE OUR SERVER
# create our virtual environment
# python -m venv <nameofvenv>
# install our tools
# pip install fastapi uvicorn

# create your main.py

# run your server with uvicorn