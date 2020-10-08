# In the name of Allah
# Sana The A.I
# Version 2-Reboot

# =========== Imports =========
from Tkinter import *
import Tkinter, Tkconstants, tkFileDialog
import ttk
import tkMessageBox
import threading
import datetime
import sys,os,subprocess,time,random,hashlib,pyperclip
# ------------------- X -------------

alp=['a','c','b','e','d','g','f',
     'i','h','k','j','m','l','o',
     'n','q','p','r','u','t','w',
     'v','y','x','z']

# ========= Tkniter ==============

root = Tk()
root.title('MD5 Cracker')
#root.iconbitmap('md5.ico')

style = ttk.Style()
style.theme_use('winnative')

class Memo:
    md5=''
    cracked=''
    crackedmd5=''

    
def browse1():
    filename = tkFileDialog.askopenfilename(defaultextension="*.*",title = "Select file",filetypes = (("all files","*.*"),("jpeg files","*.jpg"),("text files","*.txt")))
    filename=os.path.basename(filename)
    entry1.delete(0,END)
    entry1.insert(0,filename)

def paste():
    entry2.delete(0,END)
    entry2.insert(0,pyperclip.paste())


def copy():
    pyperclip.copy(entry3.get())


label1 = ttk.Label(root, text='File name : ')
label1.grid(row=0, column=0)
entry1 = ttk.Entry(root, width=40)
entry1.grid(row=0, column=1, columnspan=4)

MyButton4 = ttk.Button(root, text='browse', width=10, command=browse1)
MyButton4.grid(row=0, column=5)


label2 = ttk.Label(root, text='MD5 : ')
label2.grid(row=2, column=0)
entry2 = ttk.Entry(root, width=40)
entry2.grid(row=2, column=1, columnspan=4)


MyButton5 = ttk.Button(root, text='paste', width=10, command=paste)
MyButton5.grid(row=2, column=5)


label3 = ttk.Label(root, text='Cracked : ')
label3.grid(row=3, column=0)
entry3 = ttk.Entry(root, width=40)
entry3.grid(row=3, column=1, columnspan=4)

MyButton6 = ttk.Button(root, text='copy', width=10, command=copy)
MyButton6.grid(row=3, column=5)

# ------------------- X ----------------

# =================== Internal ===============
def alert(title,msg):
    tkMessageBox.showerror(title,msg)
    
def dom(event):
    t = threading.Thread(target=gen)
    t.start()

def crack():
    entry3.delete(0,END)
    file=entry1.get()
    string=entry2.get()
    if file!='' and string !='':
        Memo.md5=string
        try:
            st = time.time()
            x=open(entry1.get(),'r').read().strip().split()
            map(md5cracker,x)
            #[md5cracker(w) for w in x]
            if Memo.cracked==True:
                en = time.time()
                alert("Yahoo!","Hash Cracked in %0.04f ms"%(en-st))
                entry3.insert(0,Memo.crackedmd5)
            else:
                en = time.time()
                alert("Opps!","Hash Not Cracked %0.04f ms"%(en-st))
                
        except IOError:
            alert("Opps!","This file doesn't exist")
        except MemoryError:
            alert("Opps!","This file is too much for Me")
    else:
        alert("Dude!","You forgot to fill up something")

def md5cracker(string):
    has=Memo.md5
    sah=hashlib.md5(string).hexdigest().strip()
    if sah==has:
        Memo.crackedmd5=string
        Memo.cracked=True
# ---------------------------------- X ------------------------------------------

entry2.bind('<Return>', dom)

MyButton1 = ttk.Button(root, text='Crack', width=10, command=crack)
MyButton1.grid(row=4, column=1)

entry1.focus()
root.wm_attributes('-topmost', 1)
root.mainloop()
