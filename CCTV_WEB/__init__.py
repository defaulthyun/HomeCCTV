import os
from flask import Flask, render_template, jsonify, request

## Flask 객체 생성
app = Flask(__name__)

# 접속 URL 설정
def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return "main pages"
    
    return app
