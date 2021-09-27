import requests
import json
import os, platform
import time
import datetime
import winwifi

Primary_SSID='!....KENTHELL...!'
Secondary_SSID='....Kent Hell 2...'

def check_ping():
    hostname = "8.8.8.8"
    pingstatus=1
    active=0
    error=0
    pingList = []
    for x in range(5):
      time.sleep(1)  
      response = os.system("ping -n 1 " + hostname)
      pingList.append(response)
    print("\n"+"---------------------------------------------"+"\n")  
    for i in pingList:
       if i == 0:
         active += 1
       else:
         error += 1  
    print("Active:"+str(active))
    print("Error:"+str(error))
    if active > error:
      pingstatus = "Active"
    else:
      pingstatus = "Error"    
    return pingstatus

def change_wifi(status):
    print("STATUS: "+ status)
    if status == "Error":
      print("Switching to "+Secondary_SSID)
      time.sleep(1)
      winwifi.WinWiFi.connect(Secondary_SSID)
      print("Switched to "+Secondary_SSID)
      time_now=datetime.datetime.now()
      file = open("change.log", "a")
      file.write(time_now.strftime("%m/%d/%Y, %H:%M:%S")+" ::Failover to: "+Secondary_SSID + "\n")
      file.close()
      print("Waiting one minute to failover to "+Primary_SSID)
      time.sleep(60)
      winwifi.WinWiFi.connect(Primary_SSID)
      time_now=datetime.datetime.now()
      file = open("change.log", "a")
      file.write(time_now.strftime("%m/%d/%Y, %H:%M:%S")+" ::Successfully Failback to: "+Primary_SSID + "\n")
      file.close()
      print("Waiting few mnitues to restart the script")
      time.sleep(30)
      print("Successfully failover to "+Primary_SSID)
    else:
      print("No Issues observed")

while 1 < 6:
  pingstatus = check_ping()
  change_wifi(pingstatus)
