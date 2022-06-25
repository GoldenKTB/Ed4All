from flask import Flask

## Basic local website.

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World!"