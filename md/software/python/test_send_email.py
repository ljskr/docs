#!/usr/bin/python
#-*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.utils import formataddr, formatdate

def sendEmail():
    smtpHost = "smtp.mxhichina.com"
    #smtpPort = 25
    sslPort = 465
    username = "abc@pair.party"
    password = "123456"
    fromTuple = (u"发送用户", "abc@pair.party")
    toTuples = [(u"接收用户1", "111@pair.party"), (u"接收用户2","222@pair.party")]

    encoding = 'utf-8'

    fromAddr = fromTuple[1]
    fromHeader = formataddr((Header(fromTuple[0], encoding).encode(), fromTuple[1].encode(encoding)))

    toAddr = []
    toHeader = []
    for addrPair in toTuples:
        toAddr.append(addrPair[1])
        h = formataddr((Header(addrPair[0], encoding).encode(), addrPair[1].encode(encoding)))
        toHeader.append(h)

    msg = MIMEText(u"这里是正文。", "plain", encoding)
    msg['Subject'] = Header(u'这是主题', encoding).encode()
    msg['From'] = fromHeader
    msg['To'] = ','.join(toHeader)
    msg['Date'] = formatdate()
    #print (toAddr)
    #print (toHeader)
    #print (msg.as_string())

    #三种方式： 明文/TLS/SSL
    #1.普通方式，通信过程不加密
    #smtp = smtplib.SMTP(smtpHost, smtpPort)
    #smtp.ehlo()
    #smtp.login(username, password)

    #2.TLS加密方式，正常smtp端口，通信过程加密
    #smtp = smtplib.SMTP(smtpHost, smtpPort)
    #smtp.ehlo()
    #smtp.starttls()
    #smtp.ehlo()
    #smtp.login(username, password)

    #3.SSL加密方式，使用ssl端口，通信过程加密
    smtp = smtplib.SMTP_SSL(smtpHost, sslPort, "pair.party")
    smtp.set_debuglevel(True)
    smtp.login(username, password)

    try:
        smtp.sendmail(fromAddr, toAddr, msg.as_string())
    finally:
        smtp.quit()
    

if __name__ == '__main__':
    sendEmail()
