a="wget https://jnanabhumi.ap.gov.in/Uploads/Photos/19501/2017"
b="_photo.jpg"
import os
with open("t.txt")as f:
    for line in f:
        try:
            line=line.rstrip()
            temp=a+line+b
            os.system(temp)
        except:
            pass
     
