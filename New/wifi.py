import os
import urllib.request
import debugmode
import time
def connectivity():
    try:
        urllib.request.urlopen("https://www.google.com/",timeout=2)
        print("efs")
        return True
    except:
        print("zc")
        return False

selectedssid='PTCL-BB'
pw='devomech121261'
config = (
        'ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev\n'
        'update_config=0\n'
        'country=US\n'
        '\nnetwork={{\n' +
        '\tssid="{}"\n' +
        '\tpsk="{}"\n' + '}}').format(selectedssid, pw)
# print(config)


with open("/etc/wpa_supplicant/wpa_supplicant.conf",'w+') as wifi:
    wifi.write(config)
    wifi.close()
os.system("wpa_cli -i wlan0 reconfigure")
time.sleep(20)
i=connectivity()
if(i==True):
    print("connection")
    

        


