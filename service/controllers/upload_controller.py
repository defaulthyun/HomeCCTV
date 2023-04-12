import os

from flask import render_template, request, session, Response, redirect, url_for, g
from flask import current_app
from service.controllers import bp_upload as upload
from service.model.models import User

from werkzeug.utils import secure_filename # 업로드할 파일이 실제 시스템에 저장되기 전 이름을 보호하기 위해 사용

@upload.route('/upload', methods=('GET', 'POST'))
def upload():
    if request.method == 'POST':

        # 앞 서 upload.html에서 받은 파일을 불러온다
        uploaded_file = request.files['file']

        if 'user_id' in session:
            user_id = session['user_id']
        else:
            user_id = 'unknown'

        # 각 회원의 아이디로 개인 폴더를 만든 뒤, 구분하여 저장
        filename = secure_filename(uploaded_file.filename)
        user_folder = os.path.join(current_app.config['UPLOAD_FOLDER'], str(user_id))

        # 이미 개인 폴더 있을 시 폴더 생성 X
        os.makedirs(user_folder, exist_ok=True)
        filepath = os.path.join(user_folder, filename)
        uploaded_file.save(filepath)

        # 예측 결과를 이미지
        return "Upload successful"
    else:
        return redirect(request.url)