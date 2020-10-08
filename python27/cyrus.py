# i t n o A
# still need to work in SHA1 and SHA256


_banner="""
\n\n
\t\t-------------------------------
\t\t|\tCyrus the great\t\t|\n\t\t|\t\t\t\t|
\t\t|\t-by: Shakil\t\t|
\t\t-------------------------------
\n\n
"""

_ui="""
\t1) Hash Crack [MD5,SHA1,SHA256]
\t2) Hash Generator [MD5,SHA1,SHA256]
\t3) Encode Decode [BASE64, URL]
\t4) SQLi
\t5) Dir Buster
\t99) exit
"""

_banner_sqli="\t+"+'-'*39 + "+\n"+"\t|"+'\t'*2+'SQL Injection'+'\t'*2 + '|\n'+"\t|\t"+"Cyrus the great -by Shakil"+ "\t|\n"+"\t+"+'-'*39 + "+\n"+"\n\n" 

_ui_sqli="""\t1) Scanner
\t2) union select
\t3) table finder
\t4) column finder
\t5) char
\t99) return

"""

_ui_hash="""\t1) md5
\t2) sha1 
\t3) sha256
\t99) return
"""
_ui_hash_md5="""\t1) Dictonary (GUI) ,no tracing(466543 keys /sec) [Max 4.6 MB]
\t2) Dictonary console, no tracing (466543 keys /sec) [Max 4.6 MB]
\t3) Dictonary console, tracing [Max 4.6 MB] *slow
\t4) BruteForce console, no tracing
\t5) BruteForce console, tracing [after every 1000 steps]
\t99) return
"""
_ui_hash_sha1="""\t1) Dictonary (GUI) ,no tracing(466543 keys /sec) [Max 4.6 MB]
\t2) Dictonary console, no tracing (466543 keys /sec) [Max 4.6 MB]
\t3) Dictonary console, tracing [Max 4.6 MB] *slow
\t4) BruteForce console, no tracing
\t5) BruteForce console, tracing [after every 1000 steps]
\t99) return
"""
_ui_hash_sha256="""\t1) Dictonary (GUI) ,no tracing(466543 keys /sec) [Max 4.6 MB]
\t2) Dictonary console, no tracing (466543 keys /sec) [Max 4.6 MB]
\t3) Dictonary console, tracing [Max 4.6 MB] *slow
\t4) BruteForce console, no tracing
\t5) BruteForce console, tracing [after every 1000 steps]
\t99) return
"""


_ui_endcd="""\t1) Base64
\t2) URL
\t99) return
"""

_ui_endcd_bs64="""\t1) Encode
\t2) Decode
\t99) return
"""

_ui_endcd_url="""\t1) Encode
\t2) Decode
\t99) return
"""

import os
import urllib2

class Memo:
    wordlist=''
    cracked=False

def cmd(command):
    os.system(command)

def hashcrack():
    pass
def genhash():
    pass


def endcd():
    cmd('cls')
    print _banner
    print _ui_endcd
    while True:
        x=raw_input("Cyrus<<EncodeDecode<< ")
        if x=='1':
            endcd_bs()
        elif x=='2':
            endcd_url()
        elif x=='99':
            cmd('cls')
            print _banner
            print _ui
            break
            

def endcd_bs():
    cmd('cls')
    print _banner
    print _ui_endcd_bs64
    while True:
        x=raw_input("Cyrus<<EncodeDecode<<Base64<< ")
        if x=='1':
            key = raw_input("Key : ")
            print "Base64 : "+key.encode('base64').strip()
        elif x=='2':
            key = raw_input("Base64 : ")
            print "Key : "+key.decode('base64').strip()
        elif x=='99':
            cmd('cls')
            print _banner
            print _ui_endcd
            break
    return 0
            

def endcd_url():
    cmd('cls')
    print _banner
    print _ui_endcd_url
    while True:
        x=raw_input("Cyrus<<EncodeDecode<<URL<< ")
        if x=='1':
            key = raw_input("Key : ")
            print "Base64 : "+key.encode('base64').strip()
        elif x=='2':
            key = raw_input("Base64 : ")
            print "Key : "+key.decode('base64').strip()
        elif x=='99':
            cmd('cls')
            print _banner
            print _ui_endcd
            break
    return 0            
            
    



def sqli():
    cmd('cls')
    print _banner_sqli
    print _ui_sqli
    while True:
        x=raw_input("Cyrys<<sqli<< ")
        if x=='1':
            pass
        elif x=='2':
            try:
                n=int(raw_input("union select 1 to "))
                print "\nunion select "+','.join([str(i) for i in range(1,n+1)])+'\n'
            except NameError:
                print "Idiot !!!"
        elif x=='3':
            print '\ngroup_Concat(table_name)'
            print 'from information_Schema.tables where table_Schema=database()\n'
        elif x=='4':
            print '\ngroup_Concat(column_name)'
            print 'from information_Schema.columns where table_name=\n'
        elif x=='5':
            x=list(raw_input('To Char : '))
            print 'CHAR('+','.join([str(ord(_))for _ in x])+')'
        elif x=='99':
            cmd('cls')
            print _banner
            print _ui
            break
            
     


def dirbust():
    pass

def ui():
    print _ui
    while True:
        x=raw_input("Cyrus<< ")
        l=x.split()
        if x=='1':
            _hashcrackUI()
        elif x=='2':
            genhash()
        elif x=='3':
            endcd()
        elif x=='4':
            sqli()
        elif x=='5':
            dirbust()
        else:
            if len(l)>1:
                pass
            elif x=='exit' or x=='99':
                exit()
            else:
                print "Invaild command"
        
def _hashcrackUI():
    cmd('cls')
    print _banner
    print _ui_hash
    while True:
        x=raw_input("Cyrus<<HashCrack<< ")
        if x=='1':
            _hashcrackmd5()
        elif x=='2':
            _hashcracksha1()
        elif x=='3':
            _hashcracksha256()
        elif x=='99':
            cmd('cls')
            print _banner
            print _ui
            break
    return 0

def _hashcrackmd5():
    cmd('cls')
    print _banner 
    print _ui_hash_md5
    while True:
        x=raw_input("Cyrus<<HashCrack<<MD5<< ")
        if x=='1':
            os.system('start '+path+'pythonw.exe md5crackerDictGUI.py')
        elif x=='2':
            k = raw_input("MD5 Hash : ")
            w = raw_input("Wordlist : ")
            os.system(path+'python.exe md5crackerDictNoTrace.py '+k+' '+w)
        elif x=='3':
            k = raw_input("MD5 Hash : ")
            w = raw_input("Wordlist : ")
            os.system('start '+path+'python.exe md5crackerDictTrace.py '+k+' '+w)
        elif x=='4':
            k = raw_input("MD5 Hash : ")
            mil = raw_input("Minimum Length : ")
            mxl = raw_input("Maximum Length : ")
            opp = raw_input("Only/Extrem : (O/X)")
            if opp=='':
                opp='O'
                os.system('start '+path+'python.exe md5crackerBruteForceNoTrace.py '+k+' '+mil+' '+mxl+' '+opp)
            elif opp not in ['O','X']:
                print "Try Again"
            else:
                os.system('start '+path+'python.exe md5crackerBruteForceNoTrace.py '+k+' '+mil+' '+mxl+' '+opp)
        elif x=='5':
            k = raw_input("MD5 Hash : ")
            mil = raw_input("Minimum Length : ")
            mxl = raw_input("Maximum Length : ")
            opp = raw_input("Only/Extrem : (O/X)")
            if opp=='':
                opp='O'
                os.system('start '+path+'python.exe md5crackerBruteForceTrace.py '+k+' '+mil+' '+mxl+' '+opp)
            elif opp not in ['O','X']:
                print "Try Again"
            else:
                os.system('start '+path+'python.exe md5crackerBruteForceTrace.py '+k+' '+mil+' '+mxl+' '+opp)
        elif x=='99':
            cmd('cls')
            print _banner
            print _ui_hash
            break
    return 0
    
def _hashcracksha1():
    cmd('cls')
    print _banner
    print _ui_hash_sha1
    while True:
        x=raw_input("Cyrus<<HashCrack<<SHA1<< ")
        if x=='1':
            os.system('start '+path+'pythonw.exe sha1crackerDictGUI.py')
        elif x=='2':
            k = raw_input("SHA1 Hash : ")
            w = raw_input("Wordlist : ")
            os.system(path+'python.exe sha1crackerDictNoTrace.py '+k+' '+w)
        elif x=='3':
            k = raw_input("SHA1 Hash : ")
            w = raw_input("Wordlist : ")
            os.system('start '+path+'python.exe sha1crackerDictTrace.py '+k+' '+w)
        elif x=='4':
            k = raw_input("SHA1Hash : ")
            mil = raw_input("Minimum Length : ")
            mxl = raw_input("Maximum Length : ")
            opp = raw_input("Only/Extrem : (O/X)")
            if opp=='':
                opp='O'
                os.system('start '+path+'python.exe sha1crackerBruteForceNoTrace.py '+k+' '+mil+' '+mxl+' '+opp)
            elif opp not in ['O','X']:
                print "Try Again"
            else:
                os.system('start '+path+'python.exe sha1crackerBruteForceNoTrace.py '+k+' '+mil+' '+mxl+' '+opp)
        elif x=='5':
            k = raw_input("SHA1 Hash : ")
            mil = raw_input("Minimum Length : ")
            mxl = raw_input("Maximum Length : ")
            opp = raw_input("Only/Extrem : (O/X)")
            if opp=='':
                opp='O'
                os.system('start '+path+'python.exe sha1crackerBruteForceTrace.py '+k+' '+mil+' '+mxl+' '+opp)
            elif opp not in ['O','X']:
                print "Try Again"
            else:
                os.system('start '+path+'python.exe sha1crackerBruteForceTrace.py '+k+' '+mil+' '+mxl+' '+opp)
        elif x=='99':
            cmd('cls')
            print _banner
            print _ui_hash
            break
    return 0    

def _hashcracksha256():
    cmd('cls')
    print _banner
    print _ui_hash_sha1
    while True:
        x=raw_input("Cyrus<<HashCrack<<SHA256<< ")
        if x=='1':
            os.system('start '+path+'pythonw.exe sha256crackerDictGUI.py')
        elif x=='2':
            k = raw_input("SHA256 Hash : ")
            w = raw_input("Wordlist : ")
            os.system(path+'python.exe sha256crackerDictNoTrace.py '+k+' '+w)
        elif x=='3':
            k = raw_input("SHA256 Hash : ")
            w = raw_input("Wordlist : ")
            os.system('start '+path+'python.exe sha256crackerDictTrace.py '+k+' '+w)
        elif x=='4':
            k = raw_input("SHA1Hash : ")
            mil = raw_input("Minimum Length : ")
            mxl = raw_input("Maximum Length : ")
            opp = raw_input("Only/Extrem : (O/X)")
            if opp=='':
                opp='O'
                os.system('start '+path+'python.exe sha256crackerBruteForceNoTrace.py '+k+' '+mil+' '+mxl+' '+opp)
            elif opp not in ['O','X']:
                print "Try Again"
            else:
                os.system('start '+path+'python.exe sha256crackerBruteForceNoTrace.py '+k+' '+mil+' '+mxl+' '+opp)
        elif x=='5':
            k = raw_input("SHA256 Hash : ")
            mil = raw_input("Minimum Length : ")
            mxl = raw_input("Maximum Length : ")
            opp = raw_input("Only/Extrem : (O/X)")
            if opp=='':
                opp='O'
                os.system('start '+path+'python.exe sha256crackerBruteForceTrace.py '+k+' '+mil+' '+mxl+' '+opp)
            elif opp not in ['O','X']:
                print "Try Again"
            else:
                os.system('start '+path+'python.exe sha256crackerBruteForceTrace.py '+k+' '+mil+' '+mxl+' '+opp)
        elif x=='99':
            cmd('cls')
            print _banner
            print _ui_hash
            break
    return 0
    
    
try:
    path=open('path','r').read().strip()
    #cmd("title Cyrus v1")
    #cmd("color 0a")
    #cmd("cls")
    print _banner
    ui()
except IOError:
    print "No File"


