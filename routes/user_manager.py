from flask import render_template, request, session
from app import app, conn

cursor = conn.cursor()

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user_number = request.form['number']
        user_password = request.form['password']
        
        if authenticate_user(user_number, user_password):
            session['number'] = user_number
            return '로그인 성공', 200
        return '로그인 실패', 401

    return render_template('login.html')

@app.route('/change_password', methods=['GET', 'POST'])
def change_password():
    if request.method == 'POST':
        new_password = request.form['new_password']
        user_number = session.get('number')

        if not user_number:
            return '로그인이 필요합니다.', 401

        if update_user_password(user_number, new_password):
            return '비밀번호 변경 성공', 200
        return '비밀번호 변경 실패', 400

    return render_template('change_password.html')

def authenticate_user(user_number: str, user_password: str) -> bool:
    """사용자 인증"""
    query = "SELECT 1 FROM students WHERE number = ? AND password = ?"
    cursor.execute(query, (user_number, user_password))
    return cursor.fetchone() is not None

def update_user_password(user_number: str, new_password: str) -> bool:
    """사용자 비밀번호 변경"""
    update_query = "UPDATE students SET password = ? WHERE number = ?"
    cursor.execute(update_query, (new_password, user_number))
    conn.commit()

    # 비밀번호 변경 성공 여부 확인
    verify_query = "SELECT 1 FROM students WHERE number = ? AND password = ?"
    cursor.execute(verify_query, (user_number, new_password))
    return cursor.fetchone() is not None