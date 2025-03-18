from sqlite3 import Cursor
from main import conn

cursor: Cursor = conn.cursor()

#SQLite 데이터베이스 초기화
def init_db():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            "number"	INTEGER PRIMARY KEY,
            "name"	TEXT,
            "a-class"	TEXT,
            "b-class"	TEXT,
            "c-class"	TEXT,
            "d-class"	TEXT,
            "password"	TEXT
        );
    ''')
    conn.commit()
    conn.close()

#로그인
def login(number:str, password:str) -> bool:
    cursor.execute("SELECT * FROM users WHERE number = ? AND password = ?", (number, password))
    return cursor.fetchone()