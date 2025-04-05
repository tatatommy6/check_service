from flask import request
from app import app, conn
import datetime

cursor = conn.cursor()

@app.route('/checked', methods=['POST'])
def checked():
    checked_data = request.get_json(force=True)

    number = checked_data['number']
    status = checked_data['status']
    # if status == '출석':
    #     date = datetime.datetime.today().weekday()
    #     if date == 5 or date == 6:
    #         return '주말에는 출석 체크를 할 수 없습니다.', 400
    #     choosed_subject = get_user_info(number)[2:7]
    # elif status == '타교실':
    #     print(classroom)
    # elif status == '지각':
    #     pass
    # else:
    #     return '잘못된 요청', 400
    return '출석 체크 완료', 201

def get_user_info(number: str) -> list[str]:
    cursor.execute("SELECT * FROM students WHERE number = ?", (number,))
    return cursor.fetchone()