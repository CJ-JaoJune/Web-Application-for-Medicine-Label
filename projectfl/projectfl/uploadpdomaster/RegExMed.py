import re as r
with open('report.txt', 'r') as file:
    St = file.read()#.replace('\n', '')
def main():
    u_counter = 0
    c_counter = 0
    p_counter = 0  
    i = input("Choose What You Want: ")
    if r.search("วิธีใช้",St):
        u_counter +=1
    else:
        u_counter = 0
    if r.search("คำเตือน",St):
        c_counter +=1
    else:
        c_counter = 0
    if r.search("สรรพคุณ",St):
        p_counter +=1
    else:
        p_counter = 0
    if i == "U":
        print("Usage : \n")
        if u_counter == 1 :
            Usage()
            a = input("Again ?: ")
            if a == "Y":
                main()
            else:
                print("See you!!!!")
                return None
        else:
            print("No Data. \n")
            a = input("Again ?: ")
            if a == "Y":
                main()
            else:
                print("See you!!!!")
                return None
    elif i == "C":
        print("Caution : \n")
        if c_counter == 1 :
            Caution()
            a = input("Again ?: ")
            if a == "Y":
                main()
            else:
                print("See you!!!!")
                return None
        else:
            print("No Data. \n")
            a = input("Again ?: ")
            if a == "Y":
                main()
            else:
                print("See you!!!!")
                return None
    elif i == "P":
        print("Properties : \n")
        if p_counter == 1 :
            Properties()
            a = input("Again ?: ")
            if a == "Y":
                main()
            else:
                print("See you!!!!")
                return None
        else:
            print("No Data. \n")
            a = input("Again ?: ")
            if a == "Y":
                main()
            else:
                print("See you!!!!")
                return None
    else:
        main()
def Usage():
    U0 = r.sub(r"(?=คำเตือน).*",'',St ,0 , r.DOTALL)
    U1 = r.sub(r"(?=สรรพคุณ).*||\n",'',U0 ,0 , r.DOTALL)
    if U1 == '':
        U0  = r.sub(r"(?=คำเตือน).*",'',St ,0 , r.DOTALL)
        U1 = r.sub(r".*วิธีใช้",'วิธีใช้',U0 ,0 , r.DOTALL)
    print(U1)
def Properties():
    PP0 = r.sub(r"(?=คำเตือน).*",'',St ,0 , r.DOTALL)
    PP1 = r.sub(r"(?=วิธีใช้).*||\n",'',PP0 ,0 , r.DOTALL)
    if PP1 == '':
        PP0 = r.sub(r"(?=คำเตือน).*",'',St ,0 , r.DOTALL)
        PP1 = r.sub(r".*สรรพคุณ",'สรรพคุณ',PP0 ,0 , r.DOTALL)
    else:    
        print(PP1)
def Caution():
    C1 = r.sub(r".*คำเตือน",'คำเตือน',St ,0 , r.DOTALL)
    print(C1)
main()