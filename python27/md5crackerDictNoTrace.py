# In the name of Allah
# Sana The A.I
# Version 2-Reboot

# =========== Imports =========

import sys,os,subprocess,time,random,hashlib,pyperclip
from sys import *
# ------------------- X -------------



class Memo:
    md5=''
    cracked=''
    crackedmd5=''


def md5cracker(string):
    #print string
    has=Memo.md5
    sah=hashlib.md5(string).hexdigest().strip()
    if sah==has:
        Memo.cracked=True
        Memo.crackedmd5=string
        
            
            

def main():
    st=time.time()
    #key='937c513dd1f5b216e7f632f9c3bdc1a5'
    Memo.md5=argv[1]
    fil= argv[2] #'words.txt'
    try:
        f=open(fil,'r').read().strip().split()
        map(md5cracker,f)
        if Memo.cracked==True:
            en = time.time()
            print "Hash Cracked in %0.04f ms"%(en-st)
            print Memo.crackedmd5
        else:
            en = time.time()
            print "Hash Not Cracked in %0.04f ms"%(en-st)
            #print Memo.crackedmd5
    except IOError:
        print "File Do not exist"
    

main()
