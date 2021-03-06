    
import os, re, os.path, logging, datetime, random
from pathlib import Path
from spellchecker import SpellChecker
from difflib import SequenceMatcher
from shutil import copyfile
import requests
from urllib.request import Request, urlopen


path="."
#random line of file
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)
#similarity of two lines
def similar(a, b):
    return SequenceMatcher(False, a, b).ratio()
#count words
def word_count(stdIn):
    words=strFilter(stdIn).split(" ")
    return len(words)
#clear file of repeated lines
def clean_file(filename):
    copyfile(path+"/"+filename, path+"/"+filename+".old")
    lines_seen = set() # holds lines already seen
    outfile = open(path+"/"+filename, "w")
    for line in open(path+"/"+filename+".old", "r"):
        if line not in lines_seen and not strFilter(line).startswith("http"): # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()
    os.remove(path+"/"+filename+".old")
def assfart():
    url="http://assf.art/api/random/index.php"
    req = Request(url, headers={'User-Agent': 'Mozilla/5.0'})
    bullshit = urlopen(req).read()
    return strFilter(str(bullshit))
#filter text to a-Z0-9
def strFilter(stdin):
	return re.sub("[^a-zA-Z0-9]"," ", stdin.lower().strip())
#logging function
logfile="logs/log.txt"
DATE=datetime.datetime.today().strftime('%m-%d-%Y')
f=open(logfile,"a+")
f.write("NEW: "+DATE+"\n")
f.close()
def log(severity, event):
	
	SEV=str(strFilter(severity))
	DAT=str(strFilter(event))
	#f=open(logfile,"a")
	#f.write(DATE+":"+SEV+": "+DAT)
	logging.basicConfig(filename=logfile,level=logging.WARN)
	if severity == "debug":
		logging.debug(DAT)
	if severity == "info":
		logging.info(DAT)
	if severity == "warning":
		logging.warning(DAT)
	if severity == "critical":
		logging.critical(DAT)
	#f.close
	print(severity+":"+event)
	return

#read variable data
def readvar(name, id):
	if os.path.isfile(str(id)+"/"+name):
		f=open(str(id)+"/"+name,"r")
		data=f.read()
		f.close()
#		log("info","read data "+data+" from "+id+"/"+name)
		return data
	else:
		return ""
#		log("warn","failed to read data from "+id+"/"+name)

#change or make a variable
def flashvar(name, var, id):
	DATA=strFilter(var)
	NAME=strFilter(name)
	if not os.path.isdir(str(id)):
		os.mkdir(str(id))
	if len(DATA) > 128 or len(DATA) < 2:
		#log("critical"," VARIABLE DATA LENGTH FAIL "+DATA)
		return False;
	if len(NAME) > 16 or len(NAME) < 2:
		#log("critical"," VARIABLE NAME LENGTH FAIL "+NAME)
		return False;
	f=open(str(id)+"/"+NAME,"w")
	f.write(DATA)
	log("info","wrote data "+DATA+" to "+str(id)+"/"+NAME)
	f.close
	return True;

#file length
def file_len(fname):
    with open(fname) as f:
        for i, l in enumerate(f):
            pass
    return i + 1