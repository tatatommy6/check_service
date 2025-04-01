from flask import Flask
import sqlite3

# 기본 설정 파일
app = Flask(__name__)
app.secret_key = 'LN$oaYB9-5KBT7G'
conn = sqlite3.connect('EduTrack.db', check_same_thread=False)