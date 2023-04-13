import os, time, random, cv2, base64, boto3
import numpy as np

from flask import render_template, request, session, Response, redirect, url_for, g, jsonify
from flask import current_app
from service.controllers import bp_upload as upload
from service.model.models import User
from werkzeug.utils import secure_filename  # 업로드할 파일이 실제 시스템에 저장되기 전 이름을 보호하기 위해 사용

from ultralytics import YOLO
from PIL import Image


fire_dect = YOLO("service/predict_data/model/fire.pt")


@upload.route("/load", methods=["POST"])
def load():
    # 1. 클라이언트로 부터 정보 넘겨받기
    file = request.files.get("input_file")  # 파일 받아오기
    filename = secure_filename(file.filename) # 파일 이름 암호화

    # 2. 저장한 사진을 받아 분석한다
    img = Image.open(filename)
    res = fire_dect(img)  # 탐지 결과
    img = res[0].orig_img  # 이미지 배열

    # 3. 분석 결과를 이용해 탐지된 객체를 그린다
    for box in res[0].boxes.xyxy.tolist():
        x, y, x2, y2 = box
        frame = cv2.rectangle(
            img,
            pt1=(int(x), int(y)),
            pt2=(int(x2), int(y2)),
            color=(255, 0, 0),
            thickness=2,
        )
        
    # 3.5 
    
    # 4. 이미지를 html에서 읽을 수 있도록 인코딩 해준다
    _, buffer = cv2.imencode(".png", img)
    encoded_img = base64.b64encode(buffer).decode("utf-8")

    # 5. 인코딩한 결과를 반환한다
    return jsonify({"msg": encoded_img})


def upload(bk, key):
    with open(key, "rb") as f:
        img = f.read()
    # 업로드 -> 버킷 선택
    s3.Bucket(bk).put_object(Key=key, Body=img)