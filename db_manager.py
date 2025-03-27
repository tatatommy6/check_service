from sqlite3 import Cursor
from main import conn

cursor: Cursor = conn.cursor()

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

def who_in_class(what_class: str, class_name: str) -> list[str]:
    # 허용된 컬럼 이름 목록
    allowed_columns = {"class1", "class2", "class3"}  # 허용된 컬럼 이름을 정의
    if what_class not in allowed_columns:
        raise ValueError("Invalid column name provided.")

    # SQL 쿼리 생성 (컬럼 이름은 검증 후 삽입)
    query = f"SELECT name FROM students WHERE {what_class} = ?"
    cursor.execute(query, (class_name,))
    return [row[0] for row in cursor.fetchall()]  # 이름만 추출하여 리스트로 반환