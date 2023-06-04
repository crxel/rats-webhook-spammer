import requests
import time
import os
from colorama import Fore, Style

os.system('cls')
banner = fr"""{Fore.BLUE + Style.BRIGHT}
__________    _________________________ .____    .____   _________               
\______   \  /  _  \__    ___/   _____/ |    |   |    |  \_   ___ \              
 |       _/ /  /_\  \|    |  \_____  \  |    |   |    |  /    \  \/              
 |    |   \/    |    \    |  /        \ |    |___|    |__\     \____             
 |____|_  /\____|__  /____| /_______  / |_______ \_______ \______  /             
        \/         \/               \/          \/       \/      \/              
              ___.   .__                   __       __                .__  .__   
__  _  __ ____\_ |__ |  |__   ____   ____ |  | __ _/  |________  ____ |  | |  |  
\ \/ \/ // __ \| __ \|  |  \ /  _ \ /  _ \|  |/ / \   __\_  __ \/  _ \|  | |  |  
 \     /\  ___/| \_\ \   Y  (  <_> |  <_> )    <   |  |  |  | \(  <_> )  |_|  |__
  \/\_/  \___  >___  /___|  /\____/ \____/|__|_ \  |__|  |__|   \____/|____/____/
             \/    \/     \/                   \/                                
"""


options = fr"""
 +-+-+ +-+-+-+-+-+-+-+-+  
 |1. | |Spam Webhook   |    
 +-+-+ +-+-+-+-+-+-+-+-+
 |2. | |Delete Webhook |
 +-+-+ +-+-+-+-+-+-+-+-+
"""

print(banner + options)
answer = input("rats@controller:~$ ")

if answer == "1":
    webhook = input("Webhook : ")
    message = input("Message : ")
    data = {
    "content" : f"{message}",
    }
    def spam():
        time.sleep(0.5)
        sendmessage = requests.post(webhook, json = data)
        try:
            sendmessage.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print(fr"{Fore.RED}Webhook is invalid")
            time.sleep(1)
            exit()
        else:
            print(fr'{Fore.BLUE + Style.BRIGHT}Successfully sent message "{message}" to "{webhook}"')

        spam()

    spam()

if answer == "2":
    time.sleep(0.5)
    webhook = input(fr"{Fore.BLUE + Style.BRIGHT}Webhook : ")
    sendmessage = requests.delete(webhook)
    try:
        sendmessage.raise_for_status()
    except requests.exceptions.HTTPError as e:
        print(fr"{Fore.RED}Webhook is already deleted.")
        time.sleep(1)
        exit()
    else:
        print(fr'{Fore.BLUE + Style.BRIGHT}Successfully deleted "{webhook}"')