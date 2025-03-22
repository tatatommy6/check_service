import flask
from flask import render_template, request, redirect, send_file, url_for, session
import sqlite3
import qrcode
from io import BytesIO
import db_manager
# from socket_server import socket_io
#from PIL import Image

app = flask.Flask(__name__)
conn = sqlite3.connect('user.db', check_same_thread=False)
app.secret_key = 'LN$oaYB9-5KBT7G'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['GET','POST'])
def login():
    if request.method == 'POST':
        number = request.form['number']
        password = request.form['password']
        print(number, password)
        if db_manager.login(number, password):
            session['number'] = number
            return '로그인 성공', 200
        else:
            return '로그인 실패', 401
    else:
        return render_template('login.html')
    
@app.route('/mypage')
def mypage():
    if 'number' not in session:
        return redirect(url_for('login'))
    user_info = db_manager.get_user_info(session['number']) # 사용자 정보 가져오기
    print(user_info)

    timetable = [['체육', user_info[4], '언어와 매체', user_info[3], '사회'],
                [user_info[2], '영어', user_info[3], '영어', '미술'],
                [user_info[3], '음악', '미적분', user_info[4], '미술'],
                ['언어와 매체', user_info[3], user_info[5], '언어와 매체', user_info[4]],
                ['창체', '공강', '담임자율/동아리', '체육', '미적분'],
                [user_info[4], user_info[2], '담임자율/동아리', user_info[2], user_info[5]],
                [user_info[5], '미적분', '-', user_info[5], '영어']] # 시간표 가독성 수준

    return render_template('mypage.html',
        number=user_info[0],
        name=user_info[1],
        timetable=timetable
    )
    
@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    # QR 코드 이미지 생성
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    # 서버의 호스트 URL 동적으로 생성
    host_url = request.host_url.rstrip('/')
    qr.add_data(f"{host_url}/checked/{session['number']}")
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img_bytes = BytesIO()   # 이미지 저장 (BytesIO)
    img.save(img_bytes, format="PNG")
    img_bytes.seek(0)

    # 이미지 바이너리 반환
    return send_file(img_bytes, mimetype="image/png")

@app.route('/change_password', methods=['GET','POST'])
def change_password():
    if request.method == 'POST':
        new_password = request.form['new_password'] # 새로운 비밀번호
        if db_manager.change_password(session['number'], new_password):
            return '비밀번호 변경 성공', 200 
        else:
            return '비밀번호 변경 실패', 401
    else:
        return render_template('change_password.html')
    
@app.route('/checked/<string:number>')
def checked(number):
    return f'{number}님 출석 완료'

if __name__ == '__main__':
    #db_manager.init_db()
    app.run(debug=True, host='0.0.0.0')
    