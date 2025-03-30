import flask
from flask import render_template, request, redirect, send_file, url_for, session
import sqlite3
import os
from io import BytesIO
import db_manager
import datetime
import timetable as tt
import makeqr

app = flask.Flask(__name__)
conn = sqlite3.connect('EduTrack.db', check_same_thread=False)
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
    class_name = str(user_info[0])[1:3] # 사용자의 반 가져오기
    print(class_name)
    if class_name == '09':
        timetable = tt.timetable_for_1(*user_info[2:6])
    timetable = tt.timetable_for_1(*user_info[2:6]) # 시간표 생성

    return render_template('mypage.html', number=user_info[0], name=user_info[1], timetable=timetable)
    
@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    # # 서버의 호스트 URL 동적으로 생성
    # host_url = request.host_url.rstrip('/')
    # qr.add_data(f"{host_url}/checked/{session['number']}")
    # qr.make(fit=True)

    # img = qr.make_image(fill="black", back_color="white")
    # img_bytes = BytesIO()   # 이미지 저장 (BytesIO)
    # img.save(img_bytes, format="PNG")
    # img_bytes.seek(0)
    # return send_file(img_bytes, mimetype="image/png")
    # 1. 세션에 로그인된 사용자 정보가 있는지 확인
    # 세션에서 사용자 정보 가져오기

    #내가 바꾼 코드
    filepath = makeqr.gen_qr()
    if os.path.exists(filepath):
        return send_file(filepath, mimetype='image/png')
    else:
        return {"error": "QR 코드 생성 실패"}, 500

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
    
@app.route('/checked', methods=['POST'])
def checked():
    number = request.form['number']
    time = request.form['time']
    status = request.form['status']
    classroom = request.form['class']
    print(number, time, status, classroom)

    if status == '출석':
        date = datetime.datetime.today().weekday()
        if date == 5 or date == 6:
            return '주말에는 출석 체크를 할 수 없습니다.', 400
        choosed_subject = db_manager.get_user_info(number)[2:7]
    elif status == '타교실':
        print(classroom)
    elif status == '지각':
        pass
    else:
        return '잘못된 요청', 400
    return '출석 체크 완료', 201

if __name__ == '__main__':
    #db_manager.init_db()
    app.run(debug=True, host='0.0.0.0')
    