from flask import flask

app=Flask(__name__)

@app.route("/")
def intro():
    return"This is my first flask application"
