from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class UserCreateForm(FlaskForm):
    username = StringField('username', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('password', validators=[DataRequired(), EqualTo('password_ok', '비밀번호가 일치하지 않습니다')])
    password_ok = PasswordField('password_ok', validators=[DataRequired()])
    email = EmailField('email', validators=[DataRequired(), Email()])

class UserLoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=3, max=25)])
    password = PasswordField('Password', validators=[DataRequired()])