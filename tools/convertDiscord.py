import sys
import os
import re
import csv
import time
import random
from shutil import copyfile
import numpy as np
import pandas as pd
path=sys.argv[1]
def strFilter(stdin):
	return re.sub("[^a-zA-Z0-9]"," ", stdin.lower().strip())

while os.path.exists(path) == False or len(path) < 1:
    path = input("Path argument invalid. Please input a path: ")
print("Converting "+path+" to trainer data.")
i=0;
while True:
    try:
        df=pd.read_csv(path, delimiter=';', names = ['Author', 'Content', 'Date', 'Attachments'])
    except Exception as e:
        if str(e).startswith("Error tokenizing data."):
            removeline=str(int(re.findall('\d+', str(e) )[1])-1)
            print("Failed to process line "+removeline+", removing")
            copyfile(path, path+".old")
            infile = open(path+".old",'r').readlines()
            with open(path,'w') as outfile:
                for index,line in enumerate(infile):
                    if index != int(removeline):
                        outfile.write(line)
                        i+=1;
            os.remove(path+".old")

        else:
                raise Exception("CSV file error: "+str(e))
    else:
         print("Nothing went wrong.")
         break
print("Removed: "+str(i)+" lines.")

user1 = ""
while user1=="":
    test=str(df.sample(1).Author)
    user=test.split('\n',1)[0].split('    ')[0]
    if user1 == "":
        user1=user
        break
user2 = ""
while user2=="":
    test2=str(df.sample(1).Author)
    user=test2.split('\n',1)[0].split('    ')[0]
    if user2 == "" and user1 != user:
        user2=user
        break

print("USER 1: "+user1)
print("USER 2: "+user2+"\n\n")
#print(df.sample(1).Author)
tempfile=open("machinefile-old","w+")
datafile=open(path,"r").readlines()
#string=str(datafile[SELECTIONHERE]).replace(user1,'').replace(user2,'')
i=0
while i < len(datafile):
    i+=1
    string=str(datafile[i]).replace(user1,'').replace(user2,'')
    str_list=string.split(";")
    str_list[:] = [item for item in str_list if item != ""] 	
    if i == len(datafile)-3:
        break
    try:	
        if len(str_list[2]) < 3 and not str_list.startswith("http"):
            tempfile.write(strFilter(str_list[3])+"\n")
            print(strFilter(str_list[3])+"\n")
        else:
            tempfile.write(strFilter(str_list[2])+"\n")
            print(strFilter(str_list[2])+"\n")
        
    except Exception as e:
        pass
tempfile.close()

#print(str(df.sample(1)).split('\n')[2])
