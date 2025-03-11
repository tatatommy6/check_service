import flask
from flask import render_template, request, redirect, url_for, session
import sqlite3
import json

app = flask.Flask(__name__)
conn = sqlite3.connect('user.db', check_same_thread=False)
cursor = conn.cursor()
flask.secret_key = 'LN$oaYB9-5KBT7G'

#SQLite 데이터베이스 초기화
def init_db():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            "number"	INTEGER,
        );
    ''')
    conn.commit()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

if __name__ == '__main__':
    #init_db()
    app.run(debug=True, host='0.0.0.0')