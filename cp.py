import sys
import os
a=sys.argv[1:]
if len(a)!=3 and a[1].isdigit()==False or (a[1]=="help" or a[1]=='--h'):
    print(">>>> ENTER ARGUMENTS IN VALID FORMAT")
    print(">>>> ENTER DIRECTRY AND NUMBER OF FILES AS ARGUMENS")
    print("ex {foldername} + {no of files} + {extension of file}")
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