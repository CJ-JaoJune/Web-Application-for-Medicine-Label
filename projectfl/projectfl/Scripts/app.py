# Import necessary modules
from flask import send_file,Flask,render_template, request, jsonify
from werkzeug.utils import secure_filename
import subprocess
import os
import pytesseract as tess
import re as r
import sys
from PIL import Image
import json
import openai
from gtts import gTTS
import threading
import time

# Create the Flask app
app = Flask(__name__)


# Configure the upload folder
UPLOAD_FOLDER = 'Project_Yolov8/dataset_char/test' 
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


# Counter for uploaded images
uploaded_images_count = 0
# กำหนด API key ของคุณ
openai.api_key = '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'

# ฟังก์ชันสำหรับอ่านข้อมูลจากไฟล์ในโฟลเดอร์และส่งไปยัง GPT-3.5
def read_text_from_folder(folder_path):
    all_texts = ""
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if file_name.endswith('.txt'):  # เฉพาะไฟล์ที่ลงท้ายด้วย .txt เท่านั้น
            with open(file_path, 'r', encoding='utf-8') as file:
                text_content = file.read()
                all_texts += text_content + "\n"  # รวมข้อมูลจากทุกไฟล์ .txt
    return all_texts

# ฟังก์ชันสำหรับส่งข้อมูลไปยัง GPT-3.5
def send_to_gpt(input_text):
    try:
        messages = [
            {"role": "system", "content": "แก้ไขคำต่อไปนี้ให้ถูกต้องและแยกข้อมูล ชื่อยา วิธีใช้ ประโยชน์ คำเตือน"},
        ]
        combined_prompt = messages + [{"role": "user", "content": input_text}]
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=combined_prompt,
            max_tokens=500
        )
        generated_text = response['choices'][0]['message']['content']
        return generated_text
    except Exception as e:
        return f"Error: {str(e)}"
                

# Route for the home page
@app.route('/')
def index():
    return render_template('index1.html', uploaded_images_count=uploaded_images_count)


# Route for uploading a file
@app.route('/upload_file', methods=['POST'])
def upload_file():
    global uploaded_images_count

    try:
        if 'file' not in request.files:
            return jsonify({'upload_result': 'No file'})

        file = request.files['file']

        if file.filename == '':
            return jsonify({'upload_result': 'No selected file'})

        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        uploaded_images_count += 1

        return jsonify({'upload_result': 'File uploaded successfully'})
    except Exception as e:
        return jsonify({'upload_result': str(e)})


# Route for predicting with YOLOv8
@app.route('/predict_yolov8')
def predict_yolov8():
    result = predict_with_yolov8()
    return render_template('index1.html', yolov8_result=result, uploaded_images_count=uploaded_images_count)


import os
import subprocess

def predict_with_yolov8():
    try:
        current_directory = os.getcwd()  # เก็บ directory ปัจจุบัน
        os.chdir(os.path.join(current_directory, 'Project_Yolov8'))  # เปลี่ยน directory

        command = [
            'python', 'yolov8_documentOcr.py', 'predict', 'yolov8_documentOcr_thai-dataset.yaml',
            'TrainResult/documentOcr/weights/best.pt', 'dataset_char/test', 'auto', 'save'
        ]
        
        subprocess.run(command, cwd=os.getcwd())

        # เมื่อเสร็จสิ้น คืนค่าอะไรก็ได้ เช่น None หรือข้อความว่าง

    except Exception as e:
        return f"Error: {str(e)}"
    finally:
        os.chdir(current_directory)  # เมื่อเสร็จสิ้นการทำงาน กลับไปที่ directory เดิม


@app.route('/process_ocr', methods=['POST'])
def process_ocr():
    try:


        # Assuming 'file' is the key for the uploaded image in the request
        if 'file' not in request.files:
            return jsonify({'ocr_result': 'No file provided'})

        file = request.files['file']

        if file.filename == '':
            return jsonify({'ocr_result': 'No selected file'})

        # Save the uploaded image
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Use OCR script to process the image
        ocr_result = extract_information_from_image(filepath)

        return jsonify({'ocr_result': ocr_result})

    except Exception as e:
        return jsonify({'ocr_result': f'Error processing OCR: {str(e)}'})


# เพิ่มตัวแปร global สำหรับเก็บค่า OCR Result
global ocr_result



# # Function to perform OCR and extract information
def extract_information_from_image(image_path):
    global ocr_result

    try:
        img = Image.open(image_path)
        text0 = tess.image_to_string(img, lang='tha+eng')
        text1 = text0.lower()
        text2 = text1.title()
        text3 = "".join(text2.splitlines())

      
        St = text2
        U = r.sub(r"(^.*(?<=สรรพคุณ).*$)", '', St, 0, r.MULTILINE)
        U1 = r.sub(r"(^.*(?<=คำเตือน).*$||(\n))", '', U, 0, r.MULTILINE)
        PP = r.sub(r"(^.*(?<=วิธีใช้).*$)", '', St, 0, r.MULTILINE)
        PP1 = r.sub(r"(^.*(?<=คำเตือน).*$||(\n))", '', PP, 0, r.MULTILINE)
        C = r.sub(r"(^.*(?<=สรรพคุณ).*$)", '', St, 0, r.MULTILINE)
        C1 = r.sub(r"(^.*(?<=วิธีไช้).*$||(\n))", '', C, 0, r.MULTILINE)

   
        # ocr_result = print(St)
        #  ocr_result = {'St': St, 'U1': U1, 'PP': PP, 'C1': C1}
        ocr_result = {'St': St}
 
        save_ocr_result_to_file(image_path, ocr_result)

 
        return ocr_result

    except Exception as e:
        return f"Error in OCR processing: {str(e)}"

def save_ocr_result_to_file(image_path, ocr_result):
    try:
        filename_without_extension = os.path.splitext(os.path.basename(image_path))[0]
        txt_file_path = os.path.join(os.path.dirname(image_path), f"{filename_without_extension}_ocr_result.txt")

        with open(txt_file_path, 'w', encoding='utf-8') as txt_file:
            for key, value in ocr_result.items():
                txt_file.write(f"{value}\n")

    except Exception as e:
        print(f"Error saving OCR result to file: {str(e)}")


# ฟังก์ชันสำหรับการดึงข้อมูลจากไฟล์ .txt
def get_text_from_file(folder_path):
    try:
        all_texts = ""
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            if file_name.endswith('.txt'):  # เฉพาะไฟล์ที่ลงท้ายด้วย .txt เท่านั้น
                with open(file_path, 'r', encoding='utf-8') as file:
                    text_content = file.read()
                    all_texts += text_content + "\n"  # รวมข้อมูลจากทุกไฟล์ .txt
        return all_texts
    except Exception as e:
        return str(e)
    


# ฟังก์ชันสำหรับลบไฟล์ทั้งหมดในโฟลเดอร์ที่ระบุ
def delete_all_files_in_folder(folder_path):
    try:
        # ตรวจสอบไฟล์ทั้งหมดในโฟลเดอร์
        for file_name in os.listdir(folder_path):
            file_path = os.path.join(folder_path, file_name)
            # ลบไฟล์ทั้งหมดในโฟลเดอร์
            os.remove(file_path)

        return "All files in the folder have been deleted successfully."
    except Exception as e:
        return f"Error deleting files: {str(e)}"

# ฟังก์ชันสำหรับการรอเวลา 5 นาทีแล้วจึงลบไฟล์ในโฟลเดอร์
def wait_and_delete_files(folder_path):
    # รอเวลา 5 นาที
    time.sleep(120)

    # เรียกใช้ฟังก์ชันเพื่อลบไฟล์ทั้งหมดในโฟลเดอร์
    result = delete_all_files_in_folder(folder_path)
    print(result)

# Route สำหรับเรียกใช้งานฟังก์ชัน get_text() และจัดการการลบไฟล์ในโฟลเดอร์หลังจาก 5 นาที
@app.route('/get_text')
def get_text_and_delete_files():
    folder_path = 'Project_Yolov8\\dataset_char\\test\\'   
    text = get_text_from_file(folder_path)

    # สร้างเธรดใหม่เพื่อลบไฟล์หลังจากผ่านไป 5 นาที
    delete_thread = threading.Thread(target=wait_and_delete_files, args=(folder_path,))
    delete_thread.start()

    return jsonify({'text': text})

# @app.route('/get_text')
# def get_text():
#     folder_path = 'Project_Yolov8\\dataset_char\\test\\'   
#     text = get_text_from_file(folder_path)
#     return jsonify({'text': text})


 
@app.route('/send_to_gpt', methods=['POST'])
def send_data_to_gpt():
    try:
     
        folder_path = 'Project_Yolov8\\dataset_char\\test\\'
        all_texts = read_text_from_folder(folder_path)
 
        gpt_result = send_to_gpt(all_texts)

 
        output_file_path = 'Project_Yolov8\\dataset_char\\test\\Result1.txt'
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(gpt_result)

  # เพิ่มโค้ดสำหรับลบไฟล์ที่ไม่ใช่ "Result1.txt" ในโฟลเดอร์
        folder_path = 'Project_Yolov8\\dataset_char\\test\\'
        for file_name in os.listdir(folder_path):
            if file_name != 'Result1.txt':
                file_path = os.path.join(folder_path, file_name)
                os.remove(file_path)

        return jsonify({'success': True, 'message': 'Generated text saved successfully.'})
    except Exception as e:
        return jsonify({'error': f'Error sending data to GPT: {str(e)}'})
 

def read_text_to_speech(text, output_path):
    try:
        # สร้างเสียง TTS
        tts = gTTS(text=text, lang='th')
        
        # กำหนดที่เก็บไฟล์เสียง
        folder_path = 'Project_Yolov8/dataset_char/test'
        output_path = os.path.join(folder_path, output_path)
        
        # เซฟไฟล์เสียง
        tts.save(output_path)
        
        return output_path
    except Exception as e:
        return str(e)


@app.route('/read_text_to_speech')
def generate_audio_from_text():
    try:
        file_path = 'Project_Yolov8/dataset_char/test/Result1.txt'   
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
        
        audio_path = read_text_to_speech(text, 'sound.mp3')

        return jsonify({'audio_path': audio_path})
    except Exception as e:
        return jsonify({'error': str(e)})
    

@app.route('/play_audio')
def play_audio_file():
    try:
        # ระบุที่อยู่ของไฟล์เสียง
        audio_path = 'Project_Yolov8/dataset_char/test/sound.mp3'

        # ตรวจสอบว่าไฟล์เสียงอยู่ในโฟลเดอร์หรือไม่
        if os.path.exists(audio_path):
            return send_file(audio_path, as_attachment=True)
        else:
            return jsonify({'error': 'Audio file not found'})
    except Exception as e:
        return jsonify({'error': str(e)})    

    return jsonify({'audio_path': audio_path})
# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)
