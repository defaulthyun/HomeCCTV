import os
from flask import render_template, request, Response, redirect, url_for 
from service.controllers import bp_main as main
from werkzeug.utils import secure_filename # 업로드할 파일이 실제 시스템에 저장되기 전 이름을 보호하기 위해 사용


# ~/main/
@main.route("/")
def home():
    return render_template("main/index.html")

@main.route('/detection', methods=['POST'])
def detection():
    file = request.files['file']
    if file:
        filename = file.filename
        file.save(os.path.join('uploads', filename))
        flash('File uploaded successfully!')
    else:
        flash('No file uploaded.')
    return render_template('main/index.html')