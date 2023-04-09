import os
from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO, emit

# ORM을 위한 추가
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

# ORM 전역 변수 선언
db = SQLAlchemy()
migrate = Migrate()

# 접속 URL 설정
def create_app():
    # Flask 객체 생성 
    app = Flask(__name__)

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

    # 앞에서 작성한 모델을 플라스크의 migrate 기능이 인식 하도록 
    from .model import models

def init_environment(app):

    # py 모듈가져오기 해서 객체를 세팅해서 처리
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
    app.register_blueprint(bp_auth)
    app.register_blueprint(bp_main)
    app.register_blueprint(bp_upload)

    pass