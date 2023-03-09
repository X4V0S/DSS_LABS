from flask import Flask

app = Flask(__name__)
@app.route("/")

def hola():
    return "<h1>hola, mundo!</h1>"
