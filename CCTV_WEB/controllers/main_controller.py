from flask import render_template, request, Response, redirect, url_for 
from CCTV_WEB.controllers import bp_main as main

# 환경변수의 시크릿 키 획득을 위해서 Flask 객체 획득 : /CCTV_WEB/__init__.py 
from flask import current_app

# jwt
import jwt

# 시간 관련 클래스
import time
from datetime import datetime

# ~/main/
@main.route("/")
def home():
    return render_template("main/index.html")