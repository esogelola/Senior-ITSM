# -*- coding: utf-8 -*-
"""
Created on Mon Sep 19 09:53:34 2022
"""

import subprocess  ### do we even need platform and psutil if we have subprocess?  Does this work with windows and linux?
import json
import datetime
import pyodbc
import environ
env = environ.Env()

server =  env('HOST_ADDRESS')
database = env('DATABASE_NAME')
username = env('DATABASE_USER')
password = env('DATABASE_PASS')
driver = '{ODBC Driver 17 for SQL Server}'



str_SerialNumber = subprocess.check_output('wmic bios get serialnumber').decode("utf-8")
str_SerialNumber = str(str_SerialNumber.split("\n")[1])
str_Now = "\"SysInfo Transfer Date\":\"" + datetime.datetime.now().strftime("%Y-%m-%d, %H:%M:%S %p") + "\","

str_SystemInfo = subprocess.check_output(['systeminfo']).decode('utf-8').split('\n')
pro, hot, net, hyp = 0, 0, 0, 0
str_Pro, str_Hot, str_Net, str_SN, str_json = "\"Processor(s)\":[", "\"Hotfix(s)\":[", "\"Network Card(s)\":[", "\"Serial Number\":\"","{"

str_SN = str_SN + str_SerialNumber.replace("\r","").rstrip() + "\","

for line in str_SystemInfo:
    item = line.split(": ")
    if (len(item) > 1) and (hyp == 0):
        
        if (item[0] == "Processor(s)"):
            pro, hot, net, hyp = 1, 0, 0, 0
        elif (item[0] == "Hotfix(s)"):
            pro, hot, net, hyp = 0, 1, 0, 0
        elif (item[0] == "Network Card(s)"):
            pro, hot, net, hyp = 0, 0, 1, 0
        elif (item[0] == "Hyper-V Requirements"):
            pro, hot, net, hyp = 0, 0, 0, 1
        else:
            
            if ((str(item[0])[0] == " ") and (pro == 1)):
                str_Pro = str_Pro + "\"" + str(item[1]).replace("\r","") + "\","

            elif ((str(item[0])[0] == " ") and (hot == 1)):
                str_Hot = str_Hot + "\"" + str(item[1]).replace("\r","") + "\","

            elif ((str(item[0])[0] == " ") and (net == 1)):
                
                if ("[0" in str(item[0]).lstrip()) and ("                               " not in str(item[0])):
                    str_Net = str_Net + "{\"NIC\":\"" + str(item[1]).replace("\r","") + "\","
                
                elif (str(item[0]).lstrip() == "Connection Name"):
                    str_Net = str_Net + "\"Connection Name\":\"" + str(item[1]).replace("\r","") + "\"},"
                
            else:                        
                str_json = str_json + "\"" + str(item[0]) + "\":\"" + str(item[1]).lstrip().replace("\r","") + "\","
                pro, hot, net, hyp = 0, 0, 0, 0

str_Pro = str_Pro.rstrip(str_Pro[-1]) + "],"
str_Hot = str_Hot.rstrip(str_Hot[-1]) + "],"
str_Net = str_Net.rstrip(str_Net[-1]) + "]"
str_json = str_json + str_Now + str_SN + str_Pro + str_Hot + str_Net + "}"
str_json = str_json.replace("\\","\\\\")

#Send str_json on timed basis
sysInfo = json.loads(str_json)


conn = pyodbc.connect('DRIVER='+driver+';SERVER=tcp:'+server+';PORT=1433;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = conn.cursor()


sql = "SELECT COUNT(*) FROM Hardware WHERE Manf LIKE ? AND Serial1 LIKE ?"
val = (sysInfo["System Manufacturer"],sysInfo["Serial Number"])

try:
    cursor.execute(sql,val)
except:
    print("Asset not found within database!")
else:
    print("Asset found within database!")
finally:
    pass   #execute regardless of state



result = cursor.fetchone()[0]
print("result:",result)



if (result > 0):
    sql = "UPDATE Hardware SET HostName=?, OSName=?, OSVersion=?, OSManf=?, OSConf=?, Owner1=?, BootTime=?, Model=?, Type1=?, BIOSVers=?, TimeZone=?, TotPhysMem=?, AvailPhysMem=?, Domain=?, LogonServer=?, TransDate=? WHERE Manf LIKE ? AND Serial1 LIKE ?"
    val = (sysInfo["Host Name"],sysInfo["OS Name"],sysInfo["OS Version"],sysInfo["OS Manufacturer"],sysInfo["OS Configuration"],sysInfo["Registered Owner"],sysInfo["System Boot Time"].replace(",",""),sysInfo["System Model"],sysInfo["System Type"],sysInfo["BIOS Version"],sysInfo["Time Zone"],sysInfo["Total Physical Memory"],sysInfo["Available Physical Memory"],sysInfo["Domain"],sysInfo["Logon Server"],sysInfo["SysInfo Transfer Date"].replace(",",""),sysInfo["System Manufacturer"],sysInfo["Serial Number"])

    try:
        cursor.execute(sql,val)
        cursor.commit()
    except:
        print("failed to update")
    else:
        print("successful update!")
    finally:
        pass

else:
    sql = "INSERT INTO Hardware (HostName, OSName, OSVersion, OSManf, OSConf, Owner1, BootTime, Manf, Model, Type1, BIOSVers, TimeZone, TotPhysMem, AvailPhysMem, Domain, LogonServer, TransDate, Serial1) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"
    val = (sysInfo["Host Name"],sysInfo["OS Name"],sysInfo["OS Version"],sysInfo["OS Manufacturer"],sysInfo["OS Configuration"],sysInfo["Registered Owner"],sysInfo["System Boot Time"].replace(",",""),sysInfo["System Manufacturer"],sysInfo["System Model"],sysInfo["System Type"],sysInfo["BIOS Version"],sysInfo["Time Zone"],sysInfo["Total Physical Memory"],sysInfo["Available Physical Memory"],sysInfo["Domain"],sysInfo["Logon Server"],sysInfo["SysInfo Transfer Date"].replace(",",""),sysInfo["Serial Number"])
    
    try:
       cursor.execute(sql,val)
       conn.commit()
    except:
        print("failed to insert")
    else:
        print("successful insert!")
    finally:
        pass



cursor.close()
conn.close()





