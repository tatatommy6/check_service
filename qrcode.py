from flask import Flask, request, send_file
import qrcode
import io
import random
import time
import threading

#전역변수로 qr코드 데이터 저장
curr_qrdata=""

app = Flask(__name__)

def random_qr():
    return str(random.randint(100000,999999))

def update_qr_data():
    global curr_qrdata
    print(f"new qrdata generated:{curr_qrdata}")
    time.sleep(30)

threading.Thread(target=update_qr_data, daemon=True).start()

@app.route("/generate_qr/")
def generate_qr():
    data = request.args.get("data", "")
    if not data:
        return "No data provided", 401

    # QR 코드 생성
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)

    # 이미지 저장 (BytesIO)
    img = qr.make_image(fill="black", back_color="white")
    img_bytes = io.BytesIO()
    img.save(img_bytes, format="PNG")
    img_bytes.seek(0)

    # 이미지 바이너리 반환
    return send_file(img_bytes, mimetype="image/png")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
