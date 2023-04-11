from flask import Blueprint

# 인증 관련 서비스 
bp_auth = Blueprint(
    "auth_bp",
    __name__,
    url_prefix="/",
    template_folder ="../templates",
    static_folder ="../static",
)

# 메인서비스 페이지
bp_main = Blueprint(
    "main_bp",
    __name__,
    url_prefix="/main",
    template_folder ="../templates",
    static_folder ="../static",
)

# 파일 업로드 관련 서비스
bp_upload = Blueprint(
    "upload_bp",
    __name__,
    url_prefix="/upload",
    template_folder ="../templates",
    static_folder ="../static",
)