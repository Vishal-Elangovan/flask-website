from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, this is Vishal's dynamic website!"
