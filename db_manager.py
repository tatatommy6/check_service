from sqlite3 import Connection

conn: Connection
cursor: Connection.cursor

#SQLite 데이터베이스 초기화
def init_db():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
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