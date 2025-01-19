# Chronometer
โปรแกรมทำนายเวลาที่ใช้ในสร้างไฟล์ที่เก็บรูปแบบรหัสผ่านที่เป็นไปได้ เพื่อใช้ทำ `Penetration test` ด้วยวิธี `Brute-force attack`

## ความต้องการของระบบ (เพื่อให้ง่ายต่อการทำตามคู่มือ)
- windows 10
- Python 3.10.10
- Git
- Visual Studio Code (เพื่อความง่ายในการแสดงผล เนื่องจากตัวโปรแกรมเป็นภาษาไทย)
- อินเทอร์เน็ต

## ชุดข้อมูลสำหรับการฝึกฝนอยู่ในไฟล์ `data.json`
```json
{
    "password_length": [1, 2, 3, 4],
    "time_to_generate": [0.0004839, 0.0049152, 0.323587, 30.523585]
}
```
`password_length` คือรายการของความยาวรหัสผ่าน

`time_to_generate` คือรายการของระยะเวลาที่ใช้ในการสร้างไฟล์ที่เก็บรูปแบบรหัสผ่านที่เป็นไปได้ (หน่วยเป็นวินาที)

## เริ่มต้นใช้งานโปรแกรม
โคลนและเข้าถึง `chronometer`
```cmd
git clone https://github.com/NatchaLatte/chronometer.git && cd chronometer
```
สร้าง `Virtual environment` โดยตั้งชื่อ Environment ว่า `.venv`
```cmd
python -m venv .venv
```
เปิดใช้งาน `Virtual environment`
```cmd
.venv\Scripts\activate
```
ติดตั้ง `Libraries` ที่จำเป็น
```cmd
pip install -r requirements.txt
```
เปิดโปรแกรม `Visual Studio Code`
```cmd
code .
```
กด `ctrl` + `j` เพื่อเปิดหน้าต่าง `TERMINAL`

รันโปรแกรม `chronometer`
```cmd
python .\main.py
```
