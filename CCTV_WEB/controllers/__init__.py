from flask import Blueprint

# 메인서비스 페이지
bp_main = Blueprint(
    "main.bp",
    __name__,
    url_prefix="/",
    template_folder ="../templates/public",
    static_folder ="../assets",
)

# 인증 관련 서비스 
bp_auth = Blueprint(
    "auth.bp",
    __name__,
    url_prefix="/auth",
    template_folder ="../templates/auth",
    static_folder ="../assets",
)

# 파일 업로드 관련 서비스
bp_upload = Blueprint(
    "upload.bp",
    __name__,
    url_prefix="/upload",
    template_folder ="../templates/upload",
    static_folder ="../assets",
)