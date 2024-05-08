import tls_client
import time
from colorama import Fore, init
init()
session = tls_client.Session(

    client_identifier="chrome112",

    random_tls_extension_order=True

)

#/////////////////////////////////////////////////////#

token = "" # your discord token here
api_key = ''# your Fcap Key
#/////////////////////////////////////////////////////#

print(f'''
{Fore.LIGHTMAGENTA_EX}



            ███╗░░░███╗░█████╗░░██████╗░██████╗  ██████╗░███╗░░░███╗
            ████╗░████║██╔══██╗██╔════╝██╔════╝  ██╔══██╗████╗░████║
            ██╔████╔██║███████║╚█████╗░╚█████╗░  ██║░░██║██╔████╔██║
            ██║╚██╔╝██║██╔══██║░╚═══██╗░╚═══██╗  ██║░░██║██║╚██╔╝██║
            ██║░╚═╝░██║██║░░██║██████╔╝██████╔╝  ██████╔╝██║░╚═╝░██║
            ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░╚═════╝░  ╚═════╝░╚═╝░░░░░╚═╝
            github.com/Exploited7


''')
def loadFriends(token):
    headers = {
            'Accept': '*/*',
            'Authorization': token,
            'Cookie': '__dcfduid=f79a8b70f86511eea3ac5543e51156ec; __sdcfduid=f79a8b71f86511eea3ac5543e51156ec4a8a17ce9dab680fdf43763805212efc87fb1ce0dc8f1f297dc4c9b42d699765; _ga=GA1.1.1933564394.1712943226; OptanonConsent=isIABGlobal=false&datestamp=Fri+Apr+12+2024+19%3A33%3A47+GMT%2B0200+(Eastern+European+Standard+Time)&version=6.33.0&hosts=; _ga_YL03HBJY7E=GS1.1.1712943225.1.0.1712943232.0.0.0; cf_clearance=atXQAnjsUsc.bL9PHSmFkHGQnsYr8MSFuqHl36cwnVY-1715019201-1.0.1.1-DWJsXrcVBznvxDETLtKVnqDKMQ7n5X4BNxrrSn8VemLYDfKiPCpMCnbHOncxMR6wDhHSfLMFphGGU41_GL2pKw; _ga_5CWMJQ1S0X=GS1.1.1715026789.3.1.1715026920.0.0.0; __cfruid=b324b56fef9f9140cceecc00e10fe892c49f9f85-1715092816; _cfuvid=ZRzbXfLD3FPIaHvlDSuL1_NUltssNKbWJ5HArjaNxJE-1715092816402-0.0.1.1-604800000',
            'Host': 'discord.com',
            'Referer': 'https://discord.com/channels/@me',
            'sec-ch-ua': '"Chromium";v="124", "Google Chrome";v="124", "Not-A.Brand";v="99"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'Sec-Fetch-Dest': 'empty',
            'Sec-Fetch-Mode': 'cors',
            'Sec-Fetch-Site': 'same-origin',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36',
            'X-Debug-Options': 'bugReporterEnabled',
            'X-Discord-Locale': 'en-US',
            'X-Discord-Timezone': 'Africa/Cairo',
            'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLVVTIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI0LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiJodHRwczovL2Rpc2NvcmQuY29tL2NoYW5uZWxzL0BtZSIsInJlZmVycmluZ19kb21haW4iOiJkaXNjb3JkLmNvbSIsInJlZmVycmVyX2N1cnJlbnQiOiIiLCJyZWZlcnJpbmdfZG9tYWluX2N1cnJlbnQiOiIiLCJyZWxlYXNlX2NoYW5uZWwiOiJzdGFibGUiLCJjbGllbnRfYnVpbGRfbnVtYmVyIjoyOTA5OTgsImNsaWVudF9ldmVudF9zb3VyY2UiOm51bGwsImRlc2lnbl9pZCI6MH0='
    }
    
    getFriends = session.get('https://discord.com/api/v9/users/@me/relationships',headers=headers)
    response_json = getFriends.json()
    user_ids = [user["id"] for user in response_json]
    return user_ids
import requests

def solveCaptcha(rqdata):
    try:
        if api_key == "" or api_key == None:
            print("Please add your FCAP api Key in the code .")
            return None
        headers = {
            'content-type': 'application/json',
            "authorization": api_key,
        }
        payload = {
            "sitekey":"a9b5fb07-92ff-493f-86fe-352a2803b3df",
            "host":"https://discord.com",
            "proxy": proxy,  
            "rqdata":rqdata
        }

        result = requests.post("https://api.fcaptcha.lol/api/createTask", headers=headers, json=payload)
        task_id = result.json()["task"]["task_id"]
        payload = {"task_id": task_id}
        while True:
            result = requests.get(f"https://api.fcaptcha.lol/api/getTaskData", headers=headers, json=payload)
            data = result.json()
            if data["task"]["state"] == "processing":
                continue
           
            capkey = data["task"]["captcha_key"]
            return capkey
    except Exception as e:
        print(F'{Fore.RESET}[{Fore.LIGHTRED_EX}FAILED{Fore.RESET}] {Fore.LIGHTBLUE_EX} Failed to solve >> {e}')
        return None
def runMassDm(token):
    userIDS = loadFriends(token)
    for user in userIDS:
        
        url = "https://discord.com/api/v9/users/@me/channels"
        headers = {
            "Authorization": token,
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36",
            "Content-Type": "application/json",
            "Accept": "*/*",
            "Accept-Encoding": "gzip, deflate, br, zstd",
            "Accept-Language": "en-GB,en;q=0.9",
            "Origin": "https://discord.com",
            "Sec-Fetch-Dest": "empty",
            "Sec-Fetch-Mode": "cors",
            "Sec-Fetch-Site": "same-origin",
            "X-Debug-Options": "bugReporterEnabled",
            "X-Discord-Locale": "en-GB",
            "X-Discord-Timezone": "Europe/London",
            "X-Super-Properties": "eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiQ2hyb21lIiwiZGV2aWNlIjoiIiwic3lzdGVtX2xvY2FsZSI6ImVuLUdCIiwiYnJvd3Nlcl91c2VyX2FnZW50IjoiTW96aWxsYS81LjAgKFdpbmRvd3MgTlQgMTAuMDsgV2luNjQ7IHg2NCkgQXBwbGVXZWJLaXQvNTM3LjM2IChLSFRNTCwgbGlrZSBHZWNrbykgQ2hyb21lLzEyNC4wLjAuMCBTYWZhcmkvNTM3LjM2IiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTI0LjAuMC4wIiwib3NfdmVyc2lvbiI6IjEwIiwicmVmZXJyZXIiOiIiLCJyZWZlcnJpbmdfZG9tYWluIjoiIiwicmVmZXJyZXJfY3VycmVudCI6IiIsInJlZmVycmluZ19kb21haW5fY3VycmVudCI6IiIsInJlbGVhc2VfY2hhbm5lbCI6InN0YWJsZSIsImNsaWVudF9idWlsZF9udW1iZXIiOjI5MDQ1MywiY2xpZW50X2V2ZW50X3NvdXJjZSI6bnVsbCwiZGVzaWduX2lkIjowfQ=="
        }
        data = {
            "recipients": [
                user
            ]
        }
        response = session.post(url, headers=headers, json=data)
        if response.status_code == 200:
            a = response.json()["id"]
        else:
            return None
        response = session.post(f"https://discord.com/api/v9/channels/{a}/messages",headers=headers,json={
            "mobile_network_type": "unknown",
            "content": "MassDM Test - looking for fake players? DM @justmanooo",
            "nonce": user,
            "tts": False,
            "flags": 0
        })
        response2 = session.get(
            f'https://discord.com/api/users/{user}',headers=headers
        ).json()
        userSentTo = response2['username']
        if response.status_code == 200 or response.status_code == 204 :
                print(F"{Fore.RESET}[{Fore.LIGHTGREEN_EX}SUCCESS{Fore.RESET}] {Fore.LIGHTBLUE_EX} Sent , {Fore.LIGHTBLACK_EX} Username = {userSentTo} ")
        elif response.status_code == 429:
            print(F'{Fore.RESET}[{Fore.LIGHTRED_EX}FAILED{Fore.RESET}] {Fore.LIGHTBLUE_EX} RateLimited')
        elif response.status_code == 403 :
            print(F'{Fore.RESET}[{Fore.LIGHTRED_EX}FAILED{Fore.RESET}] {Fore.LIGHTBLUE_EX} DMs Closed')
        elif response.status_code == 400 :
                print(F'{Fore.RESET}[{Fore.LIGHTRED_EX}FAILED{Fore.RESET}] {Fore.LIGHTBLUE_EX} Captcha Detected')
                if api_key != None and api_key != "":
                    capkey = solveCaptcha(response.json()['captcha_rqdata'])
                    headers['X-Captcha-Key'] = capkey
                    headers['X-Captcha-Rqtoken'] = response.json()['captcha_rqtoken']
                    x = session.post(f"https://discord.com/api/v9/channels/{a}/messages",headers=headers,json={
                        "mobile_network_type": "unknown",
                        "content": "MassDM Test - looking for fake players? DM @justmanooo",
                        "nonce": user,
                        "tts": False,
                        "flags": 0
                    })
                    if x.status_code == 200 or x.status_code == 204 :
                        print(F"{Fore.RESET}[{Fore.LIGHTGREEN_EX}SUCCESS{Fore.RESET}] {Fore.LIGHTBLUE_EX} Sent , {Fore.LIGHTBLACK_EX} Username = {userSentTo} ")



        else:
            print(F'{Fore.RESET}[{Fore.LIGHTRED_EX}FAILED{Fore.RESET}] {Fore.LIGHTBLUE_EX} Could not send message, with status code : ',{response.status_code})

        time.sleep(2)
runMassDm(token)
