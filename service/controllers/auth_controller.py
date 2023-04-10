from flask import render_template, request, session, Response, redirect, url_for, g
from service.controllers import bp_auth as auth

# 시간 정보 획득, 시간차를 계산하는 함수
from datetime import datetime, timedelta

# Flask 객체 획득
from flask import current_app

# 암호화 관련
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.utils import redirect

# DB 객체 연동
from service import db
from service.forms import UserCreateForm, UserLoginForm
from service.model.models import User

# ~/auth
@auth.route("/", methods=('GET', 'POST'))
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

@auth.route("/signup/", methods=('GET', 'POST'))
def signup():
    form = UserCreateForm()
    if request.method == 'POST' and form.validate_on_submit():
        user = User.query.filter_by(username= form.username.data).first()
        if not user:
            user = User(username=form.username.data,
                        password=generate_password_hash(form.password.data),
                        email=form.email.data,
                        reg_date = datetime.now())
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth_bp.login'))
        else:
            flash('이미 존재하는 사용자입니다.')
    return render_template('auth/signup.html', form=form)

# request 변수와 마찬가지로 [요청 → 응답] 과정 처리 부분
@auth.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')
    if user_id is None:
        g.user = None # g.user에는 User 객체가 저장
    else:
        g.user = User.query.get(user_id)

@auth.route("/logout/")
def logout():
    session.clear()
    return redirect(url_for('auth_bp.login'))

@auth.route("/delete")
def delete():
    return "auth delete"