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

# 방법

    - 플라스크 객체를 생성하는 코드
        - 특정 패키지 밑에 위치 => CCTV_WEB
        - __init__.py로 이름변경
        - 구조
            - CCTV_WEB
                ▷ __init__.py
        - 최종 실행 명령
            - flask --app CCTV_WEB --debug run
