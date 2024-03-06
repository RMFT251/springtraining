from flask import Flask # From the flask module import flask class

app = Flask(__name__) # Create an instance of Flask into app (now an object)

@app.get("/") # Flask decorator that maps routes to view functions
def index(): # In Flask, "wrapped" functions are referred to as "view functions"
    me = {   # python dictionary (key value pairs)
        "first_name": "Big Meech",
        "last_name": "Larry Hoover",
        "hobbies": "RTR"
        "online": True 
    }
    return me # In flask, when you return a dictionary, it is automatically converted to JSON