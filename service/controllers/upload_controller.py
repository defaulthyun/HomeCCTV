import os

# py을 모듈가져 온 후, (객체)를 세팅해서 처리 가능
import service.config as config
from flask import render_template, request, session, Response, redirect, url_for, g
from flask import current_app
from service.controllers import bp_upload as upload
from service.model.models import User

from werkzeug.utils import secure_filename # 업로드할 파일이 실제 시스템에 저장되기 전 이름을 보호하기 위해 사용

@upload.route('/upload', methods=('GET', 'POST'))
def upload():
    if request.method == 'POST':

        # 업로드 한 파일 가져옴
        uploaded_file = request.files['file']

        # 업로드 한 파일 저장
        filename = secure_filename(uploaded_file.filename)
        filepath = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        uploaded_file.save(filepath)

        # 업로드 한 파일을 모델 예측

        # 예측 결과를 이미지
        return "Upload successful"
    else:
        return redirect(request.url)