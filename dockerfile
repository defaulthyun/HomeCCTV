# 베이스 이미지
FROM python:3.10 AS builder

# 깃허브 레포지트리 다운
RUN git clone https://github.com/defaulthyun/HomeCCTV.git

# 작업 디렉토리 지정. 없으면 생성한다
WORKDIR /HOMECCTV

# 1개의 컨테이너에는 1개의 소프트웨어를 담는다
# 가상환경이 필요없다
# 필요한 설치 패키지를 기술한 파일을 ADD or COPY
COPY requirements.txt /HOMECCTV

# 통상 리눅스에는 pip -> python 2.x , pip3 -> python 3.x
# 명령어는 pip3 install -r requirements.txt
# 마운트되고, 컨테이너가 가동되면서 pip3 명령수행시 정확하게 명령어를 인식하게 하기위해
# 캐싱을 활성화 했다
RUN --mount=type=cache,target=/root/.cache/pip pip3 install -r requirements.txt

# 원소스 -> /service 밑으로 이동
# *.py, templates, static, 기타 패키지등등
# 방법 1 : *.tar로 묶어서 한번에 원하는 위치에 풀어 놓는다 => ADD
# 방법 2 : https://.. 주소에 넣어서 원하는 위치에 놓는다 => ADD
# 방법 3 : git 명령을 통해서 내려받는다 -> RUN
# 방법 4 : 로컬상에 소스가 있다면 그냥 COPY
# 방법 5 : AWS Cloud9에서 작업했다면 -> 여기서 바로 빌드(1~4 병행) -> 이미지 등록

# 여기서는 방법 4번으로 간단하게 처리 -> 불필요한것, 이미 복사된것도 카피됨
COPY service /service

# 환경변수, 앱의 이름은 flask run 명령시 자동 인식하는 이름이므로 생략
ENV FLASK_APP service
ENV FLASK_RUN_PORT 8000
ENV FLASK_RUN_HOST 0.0.0.0

# 포트 설정 : 8000
EXPOSE 8000

# 구동 명령
ENTRYPOINT [ "flask" ] 
CMD [ "--app" , "service", "--debug", "run"]
# builder를 기반으로 추가 기술
# 리눅스 관련 작업
# 패캐지 업데이트, 계정 추가, 권한 부여등등
# FROM builder AS flask-env