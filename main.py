from app import app
from routes import check, index, mypage, user_manager

# 그냥 실행 파일
if __name__ == '__main__':
    check # 출석 체크
    index # 메인 페이지 맟 기타 일반 페이지
    mypage # 마이페이지
    user_manager # 유저 인터렉션 페이지
    app.run(debug=True, host='0.0.0.0')