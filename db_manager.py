from sqlite3 import Connection

conn: Connection
cursor = conn.cursor()

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
            "password"	TEXT,
        );
    ''')
    conn.commit()
    conn.close()