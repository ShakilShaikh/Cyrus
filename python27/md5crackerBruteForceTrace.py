# i t n o A
# brute-force by shakil
# file.py key length mode

# alp
# ulp
# num
# alp+ulp
# alp+num
# ulp+num
# alp+spc
# ulp+spc
# num+spc
# alp+ulp+spc
# alp+num+spc
# ulp+num+spc
# alp+ulp+num
# alp+ulp+num+spc


import time,os,hashlib
from sys import stdout
from sys import *
from itertools import product

say =stdout.write

ui="""\t1) lowercase\n
\t2) Uppercase\n
\t3) Numbers\n
\t4) Lowercase + Uppercase\n
\t5) Lowercase + Spacials\n 
\t6) Lowercase + Numbers\n
\t7) Uppercase + Numbers\n
\t8) Uppercase + Spacials\n
\t9) Numbers + Spacials\n
\t10) Lowercase + Uppercase + Spacials\n
\t11) Lowercase + Numbers + Spacials\n
\t12) Uppercase + Numbers + Spacials\n
\t13) Lowercase + Uppercase + Numbers\n
\t14) Lowercase + Upercase + Numbers + Spacials\n 
"""

alp='abcdefghijklmnopqrstuvwxyz'
ulp=alp.upper()
nums ='0123456789'
spl = """!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""

ac=''

def main():
    print "\tKey : "+key
    print "\tLength : "+min_length+" ~ "+max_length
      
    print ui
    x=raw_input(">> ")
    if x=='1':
        ac = alp
    elif x=='2':
        ac= ulp
    elif x=='3':
        ac = nums
    elif x=='4':
        ac= alp+ulp
    elif x=='5':
        ac = alp + spl
    elif x=='6':
        ac = alp + nums
    elif x=='7':
        ac = ulp + nums
    elif x=='8':
        ac = ulp + spl
    elif x=='9':
        ac = nums + spl
    elif x=='10':
        ac = alp + ulp + spl
    elif x=='11':
        ac = alp + nums + spl
    elif x=='12':
        ac = upl + nums + spl
    elif x=='13':
        ac= alp + ulp +nums
    elif x=='14':
        ac= alp + ulp +nums+spl
    elif x=='99':
        exit()
    else:
        print "Idiot"
        main()
    calc(ac)
    
def calc(text):
    if mode=='O':
        eta = (3.7 / (26**5)*(len(text)**int(min_length)))
        print eta
    elif mode=='X':
        tt = 0
        for i in range(int(min_length),int(max_length)+1):
            tt+= len(text)**i
        eta = (3.7 / (26**5)*tt)
    say("%s"%("It will take  "))
    if eta<60:
        say("%0.04f sec\n"%eta)
    elif eta>=60 and eta<3600:
        say("%0.04f mins\n"%(eta/60))
    elif eta>=3600 and eta<(3600*24):
        say("%0.04f hours\n"%(eta/3600))
    elif eta>=(3600*24) and eta<(3600*24*30):
        say("%0.04f days\n"%(eta/(3600*24)))
    elif eta>=(3600*24*30) and eta<(3600*24*30*12):
        say("%0.04f months\n"%(eta/(3600*24*30)))
    elif eta>=(3600*24*30*12):
        say("%0.04f years\n"%(eta/(3600*24*30*12)))
    print "\tAre We Cool ??? "
    print "\t1) Yes Bro , this is a supper computer"
    print "\t2) Well I give up, I don't thin my pc can handle it"
    gg = raw_input()
    if gg=='1':
        print "Then lets hit it bro :D"
        cracker(text)
    elif gg=='2':
        print "I understand Bro... :("
        time.sleep(5)
    

def cracker(text):
    if mode=='O':
        st = time.time()
        step = 0
        f=1
        for w in product(list(text),repeat=int(min_length)):
            if key==hashlib.md5("".join(w)).hexdigest().strip():
                print "Hash cracked : %s in %0.04f ms"%("".join(w),(time.time()-st))
                f=0
                break
            if step%500==0:
                print "Step %d"%step
            step+=1
        if f:
            print "Hash not cracked :("
        os.system('pause')
    elif mode=='X':
        st = time.time()
        step = 0
        f=1
        for ii in range(int(min_length),int(max_length)+1):
            for w in product(list(text),repeat=ii):
                if key==hashlib.md5("".join(w)).hexdigest().strip():
                    print "Hash cracked : %s in %0.04f ms"%("".join(w),(time.time()-st))
                    f=0
                    break
            if step%500==0:
                print "Step %d"%step
            step+=1
        if f:
            print "Hash not cracked :("
        os.system('pause')
    
    
        

key = argv[1]
min_length = argv[2]
max_length = argv[3]
mode = argv[4]

main()



