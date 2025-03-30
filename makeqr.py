import qrcode
import json
from datetime import datetime

#나중에 이걸로 바꾸면됨
# def gen_qr(name, student_id, classroom="국어3"):
def gen_qr(classroom="국어3"):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    data = {
        "name": "배재호",
        "student_id": "30621",
        "timestamp": now,
        "classroom": classroom
    }

    json_data = json.dumps(data, ensure_ascii=False)
    qr = qrcode.make(json_data)

    filename = f"qrcode_{'30621'}.png"
    qr.save(filename)

    return filename
saved_path = gen_qr()
print(f"QR 코드 저장 경로: {saved_path}")