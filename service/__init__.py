import os, sys, time, random, json
from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO, emit

# ORM을 위한 추가
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# ORM 전역 변수 선언
db = SQLAlchemy()
migrate = Migrate()

# AWS S3 - Boto3 패키지 사용
import boto3
from botocore.client import Config

# # 아마존 생태꼐 바깥쪽에서 아마존 엑세스 처리로 사용 할 설정된 키값 로드 (깃허브 업로드 X - AWS 직접 연락옴)
with open("./key.json") as f:
    keys = json.load(f)

SQS = boto3.client(
    "sqs",
    aws_access_key_id=keys["ACCESS_KEY_ID"],
    aws_secret_access_key=keys["ACCESS_SECRET_KEY"],
    config=Config(signature_version="s3v4"),
    region_name="ap-southeast-2", # 각자 설정된 지역 다름
)
S3 = boto3.resource(
    "s3",
    aws_access_key_id=keys["ACCESS_KEY_ID"],
    aws_secret_access_key=keys["ACCESS_SECRET_KEY"],
    config=Config(signature_version="s3v4"),
    region_name="ap-southeast-2",
)

BUCKET_NAME = "homecctv-bk"

# 접속 URL 설정
def create_app():
    # Flask 객체 생성 
    app = Flask(__name__)
    
    # Socketio 사용
    socketio = SocketIO(app)

    # 환경 변수 초기화
    init_environment(app)

    # DB 초기화
    init_database(app)
    
    # 블루프린트 초기화
    init_blueprint(app)

    return app

def init_database(app):
    # ORM을 위한 Flask 객체 - SQL 객체 - Migr 객체 연결
    db.init_app(app)
    migrate.init_app(app, db)

    # 앞에서 작성한 모델을 플라스크의 migrate 기능이 인식 하도록 작성
    from .model import models

def init_environment(app):

    # config >> __init__.py에 선언된 객체들을 세팅해서 처리
    import service.config as config
    app.config.from_object(config)    
    
    #환경변수(OS레벨, 플라스크레벨, 사용자정의레벨) 모두 출력
    # for k,v in app.config.items():
    #     print(k,v)

def init_blueprint(app):

    # 불루프린트로 정의된 개별 페이지 관련 내용 로드
    from .controllers import auth_controller
    from .controllers import main_controller
    from .controllers import upload_controller

    # 컨트롤러 __init__.py 에서 선언된 객체 불러오기
    from .controllers import bp_main, bp_auth, bp_upload

    # 플라스크 객체에 블루 프린트 등록
    auth_app = app.register_blueprint(bp_auth)
    main_app = app.register_blueprint(bp_main)  
    upload_app = app.register_blueprint(bp_upload)

    return auth_app, main_app, upload_app
