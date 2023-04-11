
SECRET_KEY = "dev"  # 서비스 추론이 불가한 해시값 추천

# ORM 처리용을 위한 환경변수 설정,(임의설정)
DB_PROTOCAL = "mysql+pymysql"
DB_USER     = "root"
DB_PASSWORD = "1234"
DB_HOST     = "127.0.0.1"
DB_PORT     = 3307
DB_DATABASE = "cctv_db" # 이 서비스에서 사용할 새로 만들 데이터베이스명 ( DB 생성 필요)

# 이 환경변수는 migrate가 필수로 요구하는 환경변수
SQLALCHEMY_DATABASE_URI=f"{DB_PROTOCAL}://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_DATABASE}"

# sqlalchemy 추가 설정
SQLALCHEMY_TRACK_MODIFICATIONS=False

# 업로드 받을 폴더 지정
UPLOAD_FOLDER = 'service/profile-picture'