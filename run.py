import sys
import os
file=sys.argv[1:]
dname=" ".join(file)
if dname[-3:].lower()=="cpp":
    fname=dname.split("\\")[-1]
    parent=dname.split("\\")[-2]
    print(">>>> BUILDING ")
    os.system("g++ "+parent+"/"+fname+" -o "+parent+"/"+fname[:-3]+"exe")
    com=dname[:-3]+"exe"
    sdir=dname.split("\\")
    com=""
    #print(sdir[:-1])
    for x in sdir[:-1]:
        if " " in x:
            com=com+'"'+x+'"'+"/"
        else:
            com=com+x+"/"
    
    print(">>>> EXECUTING ")
    os.system(com+fname[:-3]+"exe")
elif dname[-2:].lower()=="py":
    fname=dname.split("\\")[-1]
    com=""
    sdir=dname.split("\\")
    for x in sdir[:-1]:
        if " " in x:
            com=com+'"'+x+'"'+"/"
        else:
            com=com+x+"/"
    print(">>>> RUNNING ")
    os.system("python "+com+fname[:-2]+"py")

else:
    print(">>>> NOT ADDED THESE TYPES OF FILES")
    
# By Akhil Rautela
# https://www.gihub.com/AkhilRautela
