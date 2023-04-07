from flask import render_template, request, Response, redirect, url_for
from CCTV_WEB.controllers import bp_auth as auth

# 시간 정보 획득, 시간차를 계산하는 함수
from datetime import datetime, timedelta

# Flask 객체 획득
from flask import current_app

# 암호화 관련
import jwt
import bcrypt

# ~/auth
@auth.route("/")
def home():
    return "인증 페이지"

@auth.route("/login", methods=('GET', 'POST'))
def login():
    return render_template('/auth/login.html')

@auth.route("/logout")
def logout():
    return "auth logout"

@auth.route("/signup", methods=('GET', 'POST'))
def signup():
    form = UserCreateForm()
    return render_template('/auth/signup.html')

@auth.route("/delete")
def delete():
    return "auth delete"