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
            "password"	INTEGER
        );
    ''')
    conn.commit()
    conn.close()

#로그인
def login(number: str, password: str) -> bool:
    cursor.execute("SELECT * FROM students WHERE number = ? AND password = ?", (number, password))
    return cursor.fetchone() is not None  # 결과가 있으면 True, 없으면 False 반환

def change_password(number: str , new_password: str) -> bool:
    print(number, new_password)
    cursor.execute("UPDATE students SET password = ? WHERE number = ?", (new_password, number))
    conn.commit()
    cursor.execute("SELECT * FROM students WHERE number = ? AND password = ?", (number, new_password))
    return cursor.fetchone() is not None # 아마도 구현함

def get_user_info(number:str) -> list[str]:
    cursor.execute("SELECT * FROM students WHERE number = ?", (number,))
    return cursor.fetchone()