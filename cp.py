import sys
import os
a=sys.argv[1:]
if len(a)==1 and a[0]=="help":
    print(">>>> ENTER DIRECTRY AND NUMBER OF FILES AS ARGUMENS")
    print(">>>> ex {foldername} + {no of files} + {extension of file}")
elif len(a)!=3 or a[1].isdigit()==False:
    print(">>>> ENTER ARGUMENTS IN VALID FORMAT")
else:
    print(">>>> CREATING FOLDER WITH FILES")
    n=int(a[1])
    if a[0] in os.listdir():
        print(">>>> FOLDER ALREADY EXIST")
    elif n>26:
        print(">>>> TO MANY FILES")
    elif n<=0:
        print(">>>> CANNOT CREATE FOLDER WITH NO FILES")
    else:
        os.mkdir(a[0])
        os.chdir(os.getcwd()+"/"+a[0])
        for x in range(ord('A'),ord('A')+n):
            fl=open(chr(x)+"."+a[2],'w')
            fl.close()
# By Akhil Rautela
# https://www.gihub.com/AkhilRautela