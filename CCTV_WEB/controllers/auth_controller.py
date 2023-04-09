from flask import render_template, request, session, Response, redirect, url_for
from CCTV_WEB.controllers import bp_auth as auth

# 시간 정보 획득, 시간차를 계산하는 함수
from datetime import datetime, timedelta

# Flask 객체 획득
from flask import current_app

# 암호화 관련
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

# DB 객체 연동
from CCTV_WEB import db
from CCTV_WEB.forms.FormSignup import UserCreateForm
from CCTV_WEB.forms.FormLogin import UserLoginForm
from CCTV_WEB.model.models import User


# ~/auth
@auth.route("/")
def home():
    return "인증 페이지"

@auth.route("/login", methods=('GET', 'POST'))
def login():
    form = UserLoginForm()
    if request.method == 'POST' and form.validate_on_submit():
        error = None
        user = User.query.filter_by(username=form.username.data).first()
        if not user:
            error = "존재하지 않는 사용자입니다."
        elif not check_password_hash(user.password, form.password.data):
            error = "비밀번호가 올바르지 않습니다."
        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('main_bp.home'))
        flash(error)
    return render_template('auth/login.html', form=form)

@auth.route("/logout")
def logout():
    return "auth logout"

@auth.route("/signup", methods=('GET', 'POST'))
def signup():
    form = UserCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username= form.username.data).first()
        if not user:
            user = User(username=form.username.data,
                        password=generate_password_hash(form.password1.data),
                        email=form.email.data)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth_bp.login'))
        else:
            flash('이미 존재하는 유저입니다.')
    return render_template('auth/signup.html', form=form)

@auth.route("/delete")
def delete():
    return "auth delete"