import requests


url = "https://api.pushover.net/1/messages.json"
userAddress = "u1u24KYp2tAbk33xxQQ4S78rndVGi6"

#Get an API key from pushover.net and create 
#the file below with nothing else in it
keyfile = open("pushover_api", "r")
key = keyfile.read()
keyfile.close


def run(title,message,priority):
    postObjs = {
        'token': key,
        'user': userAddress,
        'message': message,
        'title': title,
        'priority': priority
    
    }
    
    
   # print("key is",key)
    r = requests.post(url,data = postObjs)
    #print(r.text)
    
    

if __name__ == "__main__":
    message = "test message"
    title = "test title"
    priority = -1
    run(title,message,priority)
