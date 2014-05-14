__author__ = 'Francis'

import smtplib
import urllib
import re
import sys
import fileinput
import xml.etree.ElementTree as ET
from datetime import datetime

info = dict()

with open("config.cfg") as f:
    lines = f.readlines()
for line in lines:
    line = line.strip()
    pLine = line.replace("\n", "")
    tList = pLine.split("=")
    info[tList[0]] = tList[1]



mailMessageQuery = "https://api.eveonline.com/char/MailMessages.xml.aspx?keyID=%s&vCode=%s&characterID=%s" % (info['keyID'], info['vCode'], info['characterID'])
messageTree = ET.parse(urllib.urlopen(mailMessageQuery)).getroot()
headerList = []
headers = messageTree.find('result/rowset')
emailsAfter = datetime.strptime(info['emailsAfter'], '%Y-%m-%d %H:%M:%S')
mailCounter = 0
#get the mail message headers from the eve api
for child in headers:
    dict = child.attrib
    sentDate = datetime.strptime(dict['sentDate'], '%Y-%m-%d %H:%M:%S')
    if sentDate > emailsAfter and dict['senderID'] != info['characterID']:
            headerList.append([dict['messageID'], dict['senderName'], dict['title'], dict['sentDate'], ""])
            mailCounter += 1

#if we havent retrieved any messages we know to be new, terminate execution
if mailCounter == 0:
    sys.exit("No mails remain to be fetched")

#get the body for every mail and accumulate them in a list
mailBodyQuery = "https://api.eveonline.com/char/MailBodies.xml.aspx?keyID=%s&vCode=%s&characterID=%s&ids=" % (info['keyID'], info['vCode'], info['characterID'])
for tuple in headerList:
    mailBodyQuery += tuple[0] + ","
mailBodyQuery = mailBodyQuery[:-1]
mailTree = ET.parse(urllib.urlopen(mailBodyQuery)).getroot()
bodies = mailTree.find('result/rowset')

for child in bodies:
    for x in range(0,len(headerList)):
        if headerList[x][0] == child.attrib['messageID']:
            headerList[x][4] = child.text
            break

#compile the final message
message = "\n Mail messages received since: %s \n \n" % (info['emailsAfter'])
t1MSGLength = len(message)
for ls in headerList:
    message += "From: " + ls[1] + "\n Subject:" + ls[2] + "\n Sent: " + ls[3] + "\n \n" + (re.sub(r'</?\w+\s+[^>]*>','',ls[4])).replace("<br>", "") + "\n ======================== \n \n"   #regex needs fixing for double >>

#set up the connection with the google smtp
if len(message) > t1MSGLength:
   server = smtplib.SMTP('smtp.gmail.com:587')
   server.starttls()
   server.login(info['mailLogin'], info['mailPasswd'])
   server.sendmail(info['mailFrom'], info['mailTo'], message)

   newest = emailsAfter
   for ls in headerList:
       sentDate = datetime.strptime(ls[3], '%Y-%m-%d %H:%M:%S')
       if sentDate > newest:
           newest = sentDate

   for line in fileinput.input("config.cfg", inplace=True):
       print line.replace(("emailsAfter=" + info['emailsAfter']),("emailsAfter=" + newest.strftime('%Y-%m-%d %H:%M:%S'))),
