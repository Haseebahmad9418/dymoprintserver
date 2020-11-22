from threading import Thread
import time
import os
import debugmode

def startprgm(i):
    print("Running thread %d" % i)
    
    if(i == 0):
        os.system("wpa_cli -i wlan0 reconfigure")
        try:
            os.system("sudo chmod -R 777 "+debugmode.dpath+"Server/")
            os.system("sudo chmod -R 777 "+debugmode.dpath+"pidata/")
            os.system("sudo chmod -R 777 "+debugmode.dpath+"tempserver/")
        except:
            pass
        
    if(i == 1):
        while True:
            time.sleep(10800)
            os.system("sudo python3 /home/pi/Server/updatechk.py")
    elif (i == 2):
        print('Running Main:')
        time.sleep(15)
        os.system("sudo python3 /home/pi/Server/main.py")
    elif (i == 3):
        print('Creating WebServer')
        time.sleep(3)
        os.system("sudo python3 /home/pi/Server/webserver.py")
    else:
        pass
for i in range(4):
    t = Thread(target=startprgm, args=(i,))
    t.start()