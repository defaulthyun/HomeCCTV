# 가상환경 구축

    - 순수 파이썬으로 구축
        - 가상환경을 모아두는 폴더 생성
            - mkdir venvs
        - 해당 폴더로 이동
            - cd venvs
        - 가상환경 생성
            - python -m venv cctv
    - 가상환경 활성화 시키는 파일 위치까지 이동
        - cd ./cctv/Scripts
    - 가상환경 활성화
        - activate(Window) or . activate(Mac, Linux)
    - 최종 프롬포트 형태
        - (cctv) : 윈도우
        - (cctv) $ : 맥/리눅스 사용자 계정
        - (cctv) # : 맥/리눅스 루트 계정

    - 아나콘다 환경으로 구성

# 필요한 패키지 설치

    - 설치
        - cd HomeCCTV
        - pip instal -r requirement.txt

# 실행

    - 플라스크 객체를 생성하는 코드
        - 특정 패키지 밑에 위치 => service
        - __init__.py로 이름변경
        - 구조
            - service
                ▷ __init__.py
        - 최종 실행 명령
            - cd ..
            - (cctv) C:\Users\HANSUNG\github\HomeCCTV>flask --app service --debug run

# DB 관련 (ORM)

        - 경로 설정 : (cctv) C:\Users\HANSUNG\github\HomeCCTV>
        - DB 생성 및 초기화 (1회)
            - FLASK_APP=service 은 없어도 되는데, 이 앱은 app or wsfi로 시작하는 엔트리가 없어 별도로 지정해야된다.
            - flask --app service db init
                - sqllite : 소형 DB, 스마트폰에 사용되는 DB, DB 자동 생성 및 파일럿 형태에서 사용
                - mysql와 같은 DB(케이스별 상이)는 실제로는 생성 안됨
            - MAC)FLASK_APP=service flask db init
            - migrations 폴더가 새로 생성돈다
                - 내부는 자동으로 만들어지는 구조이므로, 관려하지 않음
                - 단 versions 밑으로 수정할때마다 새로운 버전 DB 관련 생성
        - 모델(테이블) 생성, 변경
            - model > models.py에 테이블 관련 내용 기술
            - service> __init.py
                - !!! from .model import models : 주석해제, 신규작성 !!!
            - 들어가기 전 데이터베이스(cctv_db) 생성 필요
                - flask --app service db migrate
        - 모델(테이블) 생성, 변경 후 DB 적용
            - flask --app service db upgrade
        - 컨테이너 이미지 생성 시
            - 위 명령들을 차례대로 수행해서 DB 초기화, 생성과정 수행 필요

    - 필요한 기능들 CLI를 통해 시뮬레이션
        - DBA는 sql문을 작성해서 쿼리 구현
        - ORM는 shell을 열어 파이썬 코드로 구현
            - Flask --app service shell
