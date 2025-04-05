from flask import render_template, redirect, send_file, url_for, session
from app import app, conn
import qrcode
import json
from datetime import datetime
from io import BytesIO

cursor = conn.cursor()

def generate_timetable(A_class, B_class, C_class, D_class, class_number:int): 
    timetable = {
        1: [['체육', C_class, '언어와 매체', C_class, '사회'],
            [A_class, '영어', B_class, '영어', '미술'],
            [B_class, '음악', '미적분', C_class, '미술'],
            ['언어와 매체', B_class, D_class, '언어와 매체', C_class],
            ['창체', '공강', '담임자율/동아리', '체육', '미적분'],
            [C_class, A_class, '담임자율/동아리', A_class, D_class],
            [D_class, '미적분', '-', D_class, '영어']],
        2: [['체육', C_class, '언어와 매체', C_class, '사회'],
            [A_class, '영어', B_class, '영어', '미술'],
            [B_class, '음악', '미적분', C_class, '미술'],
            ['언어와 매체', B_class, D_class, '언어와 매체', C_class],
            ['창체', '공강', '담임자율/동아리', '체육', '미적분'],
            [C_class, A_class, '담임자율/동아리', A_class, D_class],
            [D_class, '미적분', '-', D_class, '영어']],
        9: [['체육', C_class, '언어와 매체', C_class, '사회'],
            [A_class, '영어', B_class, '영어', '미술'],
            [B_class, '음악', '미적분', C_class, '미술'],
            ['언어와 매체', B_class, D_class, '언어와 매체', C_class],
            ['창체', '공강', '담임자율/동아리', '체육', '미적분'],
            [C_class, A_class, '담임자율/동아리', A_class, D_class],
            [D_class, '미적분', '-', D_class, '영어']]
    }
    return timetable.get(class_number, [])

@app.route('/mypage')
def mypage():
    if 'number' not in session:
        return redirect(url_for('login'))
    
    user_info = get_user_info(session['number'])
    class_num = str(user_info[0])[1:3]
    timetable = generate_timetable(*user_info[2:6],int(class_num))
    return render_template('mypage.html', number=user_info[0], name=user_info[1], timetable=timetable)

@app.route('/generate_qr', methods=['POST'])
def generate_qr():

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data = {
        "name": "배재호",
        "student_id": "30621",
        "timestamp": now,
        "classroom": "국어3"
    }

    json_data = json.dumps(data, ensure_ascii=False)
    qr = qrcode.make(json_data)

    img_bytes = BytesIO()   # 이미지 저장 (BytesIO)
    qr.save(img_bytes, format="PNG")
    img_bytes.seek(0)

    return send_file(img_bytes, mimetype='image/png')

def get_user_info(number:str) -> list[str]:
    cursor.execute("SELECT * FROM students WHERE number = ?", (number,))
    return cursor.fetchone()