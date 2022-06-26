from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/problem")
def problem():
    return render_template("problem.html")

@app.route("/solution")
def solution():
    return render_template("Goals of solution.html")

@app.route("/prototype")
def prototype():
    return render_template("prototype.html")

if __name__ == "__main__":
    app.run()