import sys
import requests
from pathlib import Path

url = "https://api.pushover.net/1/messages.json"
userAddress = "u1u24KYp2tAbk33xxQQ4S78rndVGi6"

#Get an API key from pushover.net and create 
#the file pushover_api below with nothing else in it

source_path = Path(__file__).resolve()
source_dir = str(source_path.parent)
file = source_dir + "/pushover_api"

keyfile = open(file, "r")
key = keyfile.read()
keyfile.close
#remove newline from the API key, probably from ansible-vault
key = key.strip()

def run(title,message,priority):
    postObjs = {
        'token': key,
        'user': userAddress,
        'message': message,
        'title': title,
        'priority': priority
    
    }
    
    
    #print("key is",key)
    r = requests.post(url,data = postObjs)
    #print(r.text)
    
    

if __name__ == "__main__":
    message = sys.argv[2]
    title = sys.argv[1]
    priority = sys.argv[3]
    run(title,message,priority)
