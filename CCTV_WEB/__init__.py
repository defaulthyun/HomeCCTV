import os
from flask import Flask, render_template, jsonify, request
from flask_socketio import SocketIO, emit

# 접속 URL 설정
def create_app():
    app = Flask(__name__)
    # 블루프린트 초기화
    init_blueprint(app)

    # py 모듈가져오기 해서 객체를 세팅해서 처리
    import CCTV_WEB.config as config
    app.config.from_object(config)    
    
    # 환경변수(OS레벨, 플라스크레벨, 사용자정의레벨) 모두 출력
    # for k,v in app.config.items():
    #     print(k,v)

    return app

def init_blueprint(app):

    # 불루프린트로 정의된 개별 페이지 관련 내용 로드
    from .controllers import main_controller
    from .controllers import auth_controller
    from .controllers import upload_controller

    # 블루프린트 init에서 선언된 객체 불러오기
    from .controllers import bp_main, bp_auth, bp_upload

    # 플라스크 객체에 블루 프린트 등록
    app.register_blueprint(bp_main)
    app.register_blueprint(bp_auth)
    app.register_blueprint(bp_upload)

    pass