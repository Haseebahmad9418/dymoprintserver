import shutil
import json
import requests
import os
import zipfile
from distutils.dir_util import copy_tree
import zip


zip.Checkingupdates()
zip.downloadingupdates(True)



# def Checkingupdates():
#     #Creating and checking directries
#     print("Creating and checking directries")
#     tempfolder=("/home/pi/tempserver/")
#     serverfolder=("/home/pi/Server")
#     pidatafolder=("/home/pi/pidata")
#     queuefolder=("/home/pi/queue")
#     t=os.path.isdir(tempfolder)
#     s=os.path.isdir(serverfolder)
#     pd=os.path.isdir(pidatafolder)
#     qd=os.path.isdir(queuefolder)
#     if(t==False):
#         os.makedirs(tempfolder, mode=0o777)
#     if(s==False):
#         os.makedirs(serverfolder, mode=0o777)
#     if(pd==False):
#         os.makedirs(pidatafolder, mode=0o777)
#     if(qd==False):
#         os.makedirs(queuefolder, mode=0o777)
#     detailsfile=("/home/pi/pidata/version.txt")
#     vfile=os.path.isfile(detailsfile)
#     
#     if(vfile==False):
#         file1=open(detailsfile,'w+')
#         file1.write("")
#         file1.close()
#     efile=os.path.getsize(detailsfile)
#     if(efile==0):
#         file1=open(detailsfile,'w+')
#         file1.write("1; 1; ")
#         file1.close()
#     #reading current version
#     print("Reading current version")
#     file= open(detailsfile,'r')
#     for line in file:
#         feilds=line.split("; ")
#         current_v=feilds[0]
#     c=int(current_v)
#     c+=1
#     cv="00"+str(c)
#     load={"version": cv}
#     print(load)
#     #postingrequest
#     print("Posting request")
#     R_URL="https://high5.id/demo/cms/api/kiosk-get-build"
#     pload=json.dumps(load)
#     headerJson={"Content-Type": "application/json;charset=UTF-8",
#     "Accept": "*/*",
#     "Host": "high5.id",
#     "Connection": "keep-alive",
#     "User-Agent": "PostmanRuntime/7.22.0"}
#     r=requests.post(R_URL,params=pload, headers= headerJson)
#     a=json.loads(r.text)
#     v=a.get('success')
#     zf_url=a.get('url')
#     print("Success = " + str(v) +" and Request URL = " +zf_url)
#     #split url and extract version
#     print("Extracting version")
#     temp=zf_url.split("/")[-1:]
#     available_v=temp[0][-5]
#     if(a.get('success')):
#         print("Current version= "+ str(current_v) + " and available version= "+ str(available_v))
#         file1=open(detailsfile,'w+')
#         string=str(current_v)+"; "+str(available_v)+"; "+str(zf_url)+"; "
#         file1.write("")
#         file1.write(string)
#         file1.close()
# 
# def downloadingupdates():
#     print("downloading")
#     tempfolder=("/home/pi/tempserver/")
#     serverfolder=("/home/pi/Server")
#     pidatafolder=("/home/pi/pidata")
#     queuefolder=("/home/pi/queue")
#     #checking version and downloading
#     detailsfile=("/home/pi/pidata/version.txt")
#     file= open(detailsfile,'r')
#     for line in file:
#         feilds=line.split("; ")
#         current_v=feilds[0]
#         available_v=feilds[1]
#         zf_url=feilds[2]
#     if(available_v>current_v):
#         print("Downloading")
#         resp = requests.get(zf_url)
#         zname = os.path.join(tempfolder,"pie.zip")
#         zfile = open(zname, 'wb')
#         zfile.write(resp.content)
#         zfile.close()
#         epath='/home/pi/tempserver/pie.zip'
#         with zipfile.ZipFile(epath, 'r') as zipe:
#             zipe.extractall(tempfolder)
#         checkstartfile=("/home/pi/tempserver/New/start.py")
#         s_file=os.path.isfile(checkstartfile)
#         if(s_file==True):
#         #copying files
#             print("Copying files")
#             shutil.rmtree("/home/pi/Server/")
#             copy_tree("/home/pi/tempserver/New", "/home/pi/Server")
#         #Updating version file
#             print("Updating version file")
#             fin=open(detailsfile,"rt")
#             data = fin.read()
#             data = data.replace(current_v, available_v)
#             fin.close()
#             fin=open(detailsfile,"wt")
#             fin.write(data)
#             fin.close()
#             file= open(detailsfile,'r')
#             for line in file:
#                 feilds=line.split("; ")
#                 current_v=feilds[0]
#                 print("Current version= "+ str(current_v) + " and available version= "+ str(available_v))
#     
#         #Removing temp directories
#             t=os.path.isdir(tempfolder)
#             if(t==True):
#                 print("Removing temp directories")
#                 shutil.rmtree("/home/pi/tempserver")
#                 os.system("sudo reboot")
# 
# 