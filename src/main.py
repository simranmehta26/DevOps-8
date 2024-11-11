# src/main.py
from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello Everyone, Jenkins CD for my python project IT_40!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
