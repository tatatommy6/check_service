import flask
from flask import render_template, request, redirect, send_file, url_for, session
import sqlite3
import qrcode
from PIL import Image
from io import BytesIO
import db_manager

app = flask.Flask(__name__)
flask.secret_key = 'LN$oaYB9-5KBT7G'

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
    return render_template('mypage.html')
    
@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    #number = session['number']
    # QR 코드 이미지 생성
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data("Hello, World!")
    qr.make(fit=True)
    # 이미지 저장 (BytesIO)
    img = qr.make_image(fill="black", back_color="white")
    img_bytes = BytesIO()
    img.save(img_bytes, format="PNG")
    img_bytes.seek(0)

    # 이미지 바이너리 반환
    return send_file(img_bytes, mimetype="image/png")

if __name__ == '__main__':
    db_manager.conn = sqlite3.connect('user.db', check_same_thread=False)
    db_manager.cursor = db_manager.conn.cursor()
    #db_manager.init_db()
    app.run(debug=True, host='0.0.0.0')