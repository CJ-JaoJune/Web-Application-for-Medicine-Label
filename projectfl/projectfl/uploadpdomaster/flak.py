#-*- coding=utf-8 -*-
from flask import Flask
app = Flask(__name__)
@app.route('/')

def hello_world():  #def  เป็นคำสำคัญสำหรับการสร้างฟังก์ชัน
   return 'Hello World' #ให้แสดงข้อความว่า Hello World ออกทางหน้าฟอร์ม

if __name__ == '__main__':
   app.run()