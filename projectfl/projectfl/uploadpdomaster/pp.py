import pytesseract as tess
import re as r
import sys
#!/usr/bin/env python
tess.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image

def main():
    img = Image.open('upload/img_1.jpg')
    text0 = tess.image_to_string(img, lang='tha+eng')
    text1 = text0.lower()
    text2 = text1.title()
    text3 = "".join(text2.splitlines())
    
    St = text2
    #with open('report1.txt','w') as r1:
      #  r1.write(text2)
      #  r1.close()
    #from RegExMed import main
    U = r.sub(r"(^.*(?<=สรรพค).*$)",'',St ,0,r.MULTILINE)
    U1 = r.sub(r"(^.*(?<=คำเตือน).*$||(\n))",'',U ,0,r.MULTILINE) #วิธีใช้

    PP = r.sub(r"(^.*(?<=วิธีใช้).*$)",'',St ,0,r.MULTILINE)
    PP1 = r.sub(r"(^.*(?<=คำเตือน).*$||(\n))",'',PP ,0,r.MULTILINE) #สรรพคุณ

    C = r.sub(r"(^.*(?<=สรรพคุณ).*$)",'', St,0,r.MULTILINE)
    C1 = r.sub(r"(^.*(?<=วิธีไช้).*$||(\n))",'',C ,0,r.MULTILINE) #คำเตือน
    
    print(PP1)
    
main()