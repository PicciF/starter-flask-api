from flask import Flask
import os

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'ciao'