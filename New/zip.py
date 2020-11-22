import shutil
import json
import requests
import os
import time
import zipfile
from distutils.dir_util import copy_tree
import debugmode

def Checkingupdates():
    #Creating and checking directries
    print("Creating and checking directries")
    pidatafolder=debugmode.dpath+"pidata"
    pd=os.path.isdir(pidatafolder)
    if(pd==False):
        os.makedirs(pidatafolder, mode=0o777)
    detailsfile=debugmode.dpath+"pidata/version.txt"
    vfile=os.path.isfile(detailsfile)
    if(vfile==False):
        file1=open(detailsfile,'w+')
        file1.write("")
        file1.close()
    efile=os.path.getsize(detailsfile)
    if(efile==0):
        file1=open(detailsfile,'w+')
        file1.write("001; 001; ")
        file1.close()
    #reading current version
    print("Reading current version")
    file= open(detailsfile,'r')
    for line in file:
        feilds=line.split("; ")
        current_v=feilds[0]
    c=int(current_v)
    #c+=1
    #cv="0"+str(c)
    load={"version": c}
    print(load)
    #postingrequest
    print("Posting request")
    R_URL="https://high5.id/demo/cms/api/kiosk-get-build"
    pload=json.dumps(load)
    headerJson={"Content-Type": "application/json;charset=UTF-8",
    "Accept": "*/*",
    "Host": "high5.id",
    "Connection": "keep-alive",
    "User-Agent": "PostmanRuntime/7.22.0"}
    r=requests.post(R_URL, headers= headerJson)#params=pload,
    a=json.loads(r.text)
    v=a.get('success')
    zf_url=a.get('url')
    print("Success = " + str(v) +" and Request URL = " +zf_url)
    #split url and extract version
    print("Extracting version")
    temp=zf_url.split("/")[-1:]
    available_v=temp[0][-7:-4]
    if(a.get('success')):
        print("Current version= "+ str(current_v) + " and available version= "+ str(available_v))
        file1=open(detailsfile,'w+')
        string=str(current_v)+"; "+str(available_v)+"; "+str(zf_url)+"; "
        file1.write("")
        file1.write(string)
        file1.close()
    if(int(available_v)>int(current_v)):
        return True
    else:
        return False
    

def downloadingupdates(rupdate=False):
    print("Creating and checking directries")
    tempfolder=debugmode.dpath+"tempserver/"
    serverfolder=debugmode.dpath+"Server"
    queuefolder=debugmode.dpath+"queue"
    t=os.path.isdir(tempfolder)
    s=os.path.isdir(serverfolder)
    qd=os.path.isdir(queuefolder)
    if(t==False):
        os.makedirs(tempfolder, mode=0o777)
    if(s==False):
        os.makedirs(serverfolder, mode=0o777)
    if(qd==False):
        os.makedirs(queuefolder, mode=0o777)
    print("downloading function")
    tempfolder=debugmode.dpath+"tempserver/"
    serverfolder=debugmode.dpath+"Server"
    queuefolder=debugmode.dpath+"queue"
    #checking version and downloading
    detailsfile=debugmode.dpath+"pidata/version.txt"
    file= open(detailsfile,'r')
    for line in file:
        feilds=line.split("; ")
        currentv=feilds[0]
        availablev=feilds[1]
        zfurl=feilds[2]
    print("for loop exited")
    if(int(availablev)>int(currentv)):
        print("Downloading")
        print(zfurl)
        resp = requests.get(zfurl)
        zname = os.path.join(tempfolder,"pie.zip")
        print("zip created")
        zfile = open(zname, 'wb')
        zfile.write(resp.content)
        zfile.close()
        print("error1")
        epath=tempfolder+"pie.zip"
        with zipfile.ZipFile(epath, 'r') as zipe:
            zipe.extractall(tempfolder)
        checkstartfile=tempfolder+"New/start.py"
        s_file=os.path.isfile(checkstartfile)
        print("error2")
        if(s_file==True):
        #copying files
            print("Copying files")
            os.system("sudo chmod -R 777 "+debugmode.dpath+"Server/")
            copy_tree(tempfolder+"New", serverfolder)
        #Updating version file
            print("Updating version file")
            fin=open(detailsfile,"rt")
            data = fin.read()
            data = data.replace(currentv, availablev)
            fin.close()
            fin=open(detailsfile,"wt")
            fin.write(data)
            fin.close()
            file= open(detailsfile,'r')
            for line in file:
                feilds=line.split("; ")
                currentv=feilds[0]
                print("Current version= "+ str(currentv) + " and available version= "+ str(availablev))
    
        #Removing temp directories
            t=os.path.isdir(tempfolder)
            if(t==True):
                print("Removing temp directories")
                shutil.rmtree(tempfolder)
            if(rupdate==True):
                print("restarting after update")
                time.sleep(1)
                os.system("sudo reboot")
    else:
        print("else initiated")
        time.sleep(0.1)
        pass

