import flask
from flask import render_template, request, redirect, url_for, session
import sqlite3
import json
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

if __name__ == '__main__':
    db_manager.conn = sqlite3.connect('user.db', check_same_thread=False)
    db_manager.cursor = db_manager.conn.cursor()
    #db_manager.init_db()
    app.run(debug=True, host='0.0.0.0')