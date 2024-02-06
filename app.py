from flask import Flask
import os

app = Flask(__name__)

 
port = int(os.environ.get("PORT", 5000))
app.run(host='https://bored-gray-magpie.cyclic.app/', port=port)

@app.route('/')
def hello_world():
    return 'Hello, world!'