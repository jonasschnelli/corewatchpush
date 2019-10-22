#!/usr/bin/env python3

from config import *

from email.utils import make_msgid

import sys
import smtplib
import datetime

class Notify_SMTP:
    def push(text="test"):
        smtpObj = smtplib.SMTP(Config.notify_email_smtphost)
        smtpObj.login(Config.notify_email_smtpuser, Config.notify_email_smtppass)
        
        message = "Content-Type: text/plain; charset=utf-8\nMessage-ID: "+make_msgid(None, "corewatchpush.local")+"\nDate: "+datetime.datetime.now().strftime('%a, %d %b %Y  %H:%M:%S %Z')+"\n"+"Content-Disposition: inline\nContent-Transfer-Encoding: 8bit\nFrom: "+Config.notify_email_sender+"\nTo: "+Config.notify_email_receiver+"\n"+"Subject: CoreWatchPush"+"\n\r\n\r"
        message += text
        smtpObj.sendmail(Config.notify_email_sender, [Config.notify_email_receiver], message.encode("utf8"))

if __name__ == '__main__':
    if len(sys.argv) == 2:
        Notify_SMTP.push(sys.argv[1])