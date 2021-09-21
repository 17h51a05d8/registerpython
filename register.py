import re
options=input("enter register/login:")
regexem = "^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$"
regexpass ="(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{5,10}$"
fptr=open("register.txt","a")
if(options=="register"):
    st=input("enter email address:")
    pas=input("enter password:")
    e=0
    p=0
    if(re.search(regexem,st)):
        e=1
        if(re.search(regexpass,pas)):
            fptr.write(st)
            fptr.write("\n")
            fptr.write(pas)
            fptr.write("\n")
            print("user registered successfully")
    else:
        print("wrong credentials")
fptr.close()