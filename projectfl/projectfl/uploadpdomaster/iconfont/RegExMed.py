import re as r
with open('report1.txt', 'r') as file:
    St = file.read()#.replace('\n', '')
def main():
    i = input("Choose What You Want: ")
    if i == "U":
        print("Usage : \n")
        Usage()
        a = input("Again ?: ")
        if a == "Y":
            main()
        else:
            print("See you!!!!")
            return None
    elif i == "C":
        Caution()
        a = input("Again ?: ")
        if a == "Y":
            main()
        else:
            print("See you!!!!")
            return None
    elif i == "P":
        Properties()
        a = input("Again ?: ")
        if a == "Y":
            main()
        else:
            print("See you!!!!")
            return None
    else:
        main()
def Usage():
    U = r.sub(r"(^.*(?<=สรรพคุณ).*$)",'',St ,0,r.MULTILINE)
    U1 = r.sub(r"(^.*(?<=คำเตือน).*$||(\n))",'',U ,0,r.MULTILINE)
    print(U1)
def Properties():
    PP = r.sub(r"(^.*(?<=วิธีใช้).*$)",'',St ,0,r.MULTILINE)
    PP1 = r.sub(r"(^.*(?<=คำเตือน).*$||(\n))",'',PP ,0,r.MULTILINE)
    print(PP1)
def Caution():
    C = r.sub(r"(^.*(?<=สรรพคุณ).*$)",'', St,0,r.MULTILINE)
    C1 = r.sub(r"(^.*(?<=วิธีใช้).*$||(\n))",'',C ,0,r.MULTILINE)
    print(C1)
main()
