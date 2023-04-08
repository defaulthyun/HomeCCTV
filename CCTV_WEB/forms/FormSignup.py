from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

# 시간 정보 획득, 시간차를 계산하는 함수
from datetime import datetime, timedelta
class UserCreateForm(FlaskForm):
    id = StringField('아이디', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('비밀번호', validators=[DataRequired(), EqualTo('password_ok', '비밀번호가 일치하지 않습니다')])
    password_ok = PasswordField('비밀번호확인', validators=[DataRequired()])
    email = EmailField('이메일', validators=[DataRequired(), Email()])