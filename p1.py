i,j,k,l,m,n,o,p=0,0,0,0,0,0,0,0
import os
a="wget https://jnanabhumi.ap.gov.in/Uploads/Photos/19501/2017"
b="_photo.jpg"
while(i<=9):
    if(p>9):
        p=0
        o+=1
    if(o>9):
        o=0
        n+=1
    if(n>9):
        n=0
        m+=1
    if(m>9):
        m=0
        l+=1
    if(l>9):
        l=0
        k+=1
    if(k>9):
        k=0
        j+=1
    if(j>9):
        j=0
        i+=1
    if(i>9):
        break
    s=str(i)+str(j)+str(k)+str(l)+str(m)+str(n)+str(o)+str(p)
    s=a+s+b
    os.system(s)
    p=p+1
