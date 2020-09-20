from flask import Flask
from datetime import datetime
import re
from flask import render_template

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask!"

@app.route("/hello/")
@app.route("/hello/<name>")
def hello_there(name = None):
    return render_template(
        "hello_there.html",
        name=name,
        date=datetime.now()
    )

print('http://127.0.0.1:5000/hello/pal')