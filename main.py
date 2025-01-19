import json
import numpy as np
from sklearn.linear_model import LinearRegression

try:
    # เปิดไฟล์ JSON และโหลดข้อมูล
    with open('data.json', 'r') as file:
        data = json.load(file)

    # ตรวจสอบว่า data มีคีย์ที่ต้องการหรือไม่
    if "password_length" not in data or "time_to_generate" not in data:
        raise Exception("Missing necessary keys in the JSON file.")
    
    # แปลงข้อมูลเป็น numpy array
    x = np.array(data["password_length"]).reshape(-1, 1)
    y = np.array(data["time_to_generate"])

    # สร้างและฝึกโมเดล
    model = LinearRegression()
    model.fit(x, y)

    # รับค่าจากผู้ใช้เพื่อนำข้อมูลมาทำนาย
    min_password_length = input("ความยาวรหัสผ่านขั้นต่ำ: ")
    max_password_length = input("ความยาวรหัสผ่านสูงสุด: ")

    # ตรวจสอบความถูกต้องของข้อมูล
    if not min_password_length.isdigit() or not max_password_length.isdigit():
        raise Exception("ความยาวรหัสผ่านต้องเป็นตัวเลขเท่านั้น")
    if min_password_length < 1 or max_password_length < 1:
        raise Exception("ความยาวรหัสผ่านต้องเป็นจำนวนเต็มบวกเท่านั้น")
    if min_password_length > max_password_length:
        raise Exception("ความยาวรหัสผ่านขั้นต่ำจะต้องมีความยาวมากกว่ารหัสผ่านสูงสุด")
    
    # สร้างรายการความยาวของรหัสผ่านที่ต้องการทำนายระยะเวลาในการสร้าง
    password_length = np.arange(min_password_length, max_password_length + 1).reshape(-1, 1)

    # ทำนายระยะเวลาในการสร้างรหัสผ่าน
    predicted = model.predict(password_length)

    # แสดงผลการทำนาย
    for length, time in zip(password_length.flatten(), predicted):
        print(f"ระยะเวลาในการสร้างรหัสผ่านสำหรับความยาว {length} คือ {time:.2} วินาที")
    print(f"ระยะเวลาในการสร้างรหัสผ่านสำหรับความยาวตั้งแต่ {min_password_length} ถึง {max_password_length} จะใช้เวลารวมทั้งหมด {np.sum(predicted, axis=0):.2} วินาที")

except FileNotFoundError:
    print('System: ไม่พบไฟล์')
except json.JSONDecodeError:
    print('System: รูปแบบไฟล์เจสันไม่ถูกต้อง')
except Exception as e:
    print(f"System: {e}")