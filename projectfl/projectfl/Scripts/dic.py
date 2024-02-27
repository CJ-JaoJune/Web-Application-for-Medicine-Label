import os

# สร้าง Dictionary ที่เก็บคำศัพท์และความหมายเหมือน
synonyms_dict = {
    'ชื่อยา': ['ชื่อ', 'ชื่อยา', 'ชื่อสามัญทางยา' , ''],
    'วิธีใช้': ['วิธีใช้','ขั้นตอน', 'วิธีรับประทาน', 'ขนาดและวิธีใช้', 'ขนาดรับประทาน','ควรรับประเทาน', 'รับประทาน', 'รับประทานครั้งละ', 'ใช้','ใช้เฉพาะ'],
    'ประโยชน์': ['ประโยชน์', 'ประโยชน์และสรรพคุณ', 'ประโยชน์และคุณลักษณะ','สรรพคุณ', 
                 'คุณลักษณะ', 'ประโยชน์และสรรพคุณ', 'แก้' , 'แก้ปวดลดไข้','แก้ปว'],
    'คำเตือน': ['คำเตือน', 'ข้อควรระวัง', 'ข้อห้ามใช้', 'ห้ามใช้', 'ข้อระวัง','ห้าม','ห้ามใช้เกิน']
}

# ฟังก์ชันสำหรับตรวจสอบคำที่มีอยู่ใน Dictionary
def check_synonyms(input_word):
    input_first_word = input_word.split()[0]  # แยกวรรคแรก

    for word, synonyms in synonyms_dict.items():
        if input_first_word in synonyms:
            return word  # ส่งค่าชื่อของกลุ่มคำที่มีความหมายตรงกับ Dictionary กลับไป

    return None  # ถ้าไม่พบคำที่ตรงกับ Dictionary ให้ส่งค่า None กลับไป

# ฟังก์ชันสำหรับอ่านคำจากไฟล์ .txt และตรวจสอบความหมายของคำแรกในแต่ละบรรทัด
def read_and_check_text_from_folder(folder_path):
    files = os.listdir(folder_path)
    
    # สร้าง Dictionary เพื่อเก็บผลลัพธ์ของแต่ละกลุ่มคำ
    results = {group: [] for group in synonyms_dict.keys()}
    
    for file_name in files:
        file_path = os.path.join(folder_path, file_name)
        if os.path.isfile(file_path) and file_name.endswith('.txt'):
            with open(file_path, 'r', encoding='utf-8') as file:
                for line in file:
                    if line.strip():  # ตรวจสอบว่าบรรทัดไม่ว่าง
                        words = line.split()
                        first_word = words[0]  # เลือกคำแรกในแต่ละบรรทัด
                        result = check_synonyms(first_word)
                        if result:  # ตรวจสอบว่าคำมีความหมายตรงกับ Dictionary หรือไม่
                            results[result].append(line.strip())
    
    # พิมพ์ผลลัพธ์ของแต่ละกลุ่มคำ
    for group, lines in results.items():
        if lines:  # ตรวจสอบว่ามีข้อมูลในกลุ่มคำหรือไม่
            print(f'{group}:')
            for line in lines:
                print(line)

# เรียกใช้ฟังก์ชันเพื่ออ่านคำจากไฟล์ .txt และตรวจสอบความหมาย
folder_path = 'GPT\\RE'

read_and_check_text_from_folder(folder_path)