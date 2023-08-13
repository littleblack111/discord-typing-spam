from requests import post
from configparser import ConfigParser as config

config.read('token.ini')
token = config.get("Auth", "token")

# make post request not sussful etc into function

def main():
    channelid = input("Please enter the channelid you want to spam typing in")
    url = f"https://discord.com/api/v9/channels/{channelid}/typing"
    headers = { 'Authorization': token }
    x = post(url, headers = headers)
    if x != 204:
        print("not succesful")
        exit 1
    else:
        loop = input("how much times do u want to spam(seconds)")
        if loop != "" and loop == int():
            for i in loop/3:
                x = post(url, headers = headers)
                if x != 204:
                    print("not succesful")
                    continue
        else:
            while True:
                x = post(url, headers = headers)
                if x != 204:
                    print("not succesful")
                    continue

        
