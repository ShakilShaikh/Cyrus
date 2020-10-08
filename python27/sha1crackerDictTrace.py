# In the name of Allah
# Sana The A.I
# Version 2-Reboot

# =========== Imports =========

import os,time,random,hashlib
from sys import *
from sys import stdout

say = stdout.write
# ------------------- X -------------

def cmd(s):
    os.system(s)


class Memo:
    md5=''
    cracked=False
    crackedmd5=''


def md5cracker(string):
    #print string
    has=Memo.md5
    sah=hashlib.sha1(string).hexdigest().strip()
    if sah==has:
        Memo.cracked=True
        Memo.crackedmd5=string
        return True
        
            
            

def main():
    st=time.time()
    #key='937c513dd1f5b216e7f632f9c3bdc1a5'
    Memo.md5=argv[1]
    fil= argv[2] #'words.txt'
    try:
        f=open(fil,'r').read().strip().split()
        for w in f:
            say("%s\n"%w)
            if md5cracker(w):
                en = time.time()
                say("Hash Cracked in %0.04f ms  "%(en-st))
                say("%s\n"%Memo.crackedmd5)
                break
                #stdout.flush()
        if Memo.cracked==False:
            en = time.time()
            say("Hash Not Cracked in %0.04f ms"%(en-st))
            #print Memo.crackedmd5
        cmd('pause')
    except IOError:
        print "File Do not exist"
    

main()
