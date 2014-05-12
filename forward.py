__author__ = 'Francis'

import smtplib
import urllib
import xml.etree.ElementTree as ET
from datetime import datetime

info = dict()

with open("config.cfg") as f:
    lines = f.readlines()
for line in lines:
    tList = line.split("=")
    info[tList[0]] = tList[1]



mailMessageQuery = "https://api.eveonline.com/char/MailMessages.xml.aspx?keyID=%s&vCode=%s&characterID=%s" % (info['keyID'], info['vCode'], info['characterID'])
messageTree = ET.parse(urllib.urlopen(mailMessageQuery)).getroot()
headerList = []
headers = messageTree.find('result/rowset')

emailsAfter = datetime.strptime(info['emailsAfter'], '%Y-%m-%d %H:%M:%S')
for child in headers:
    dict = child.attrib
    sentDate = datetime.strptime(dict['sentDate'], '%Y-%m-%d %H:%M:%S')
    if sentDate > emailsAfter:

    headerList.append(child.attrib)


mailBodyQuery = "https://api.eveonline.com/char/MailBodies.xml.aspx?keyID=%s&vCode=%s&characterID=%s&ids=" % (info['keyID'], info['vCode'], info['characterID'])

for id in ids:
    mailBodyQuery += id + ","
mailBodyQuery = mailBodyQuery[:-1]


message = ""
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(info['mailLogin'], info['mailPasswd'])
server.sendmail(info['mailFrom'], info['mailTo'], message)

