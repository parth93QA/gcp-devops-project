from flask import Flask
app = Flask(__name__)

#New Route
@app.route('/')
def hello_world():
    return 'Hello, Simple Flask Application'