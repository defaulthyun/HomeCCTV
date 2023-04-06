import os
from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO, emit

## Flask 객체 생성
app = Flask(__name__)

# 접속 URL 설정
@app.route("/login")
def home():
    return render_template('login.html')

@app.route("/main")
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
