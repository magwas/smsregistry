#!/usr/bin/python

from email.mime.text import MIMEText
from email.header import Header
from subprocess import Popen, PIPE
from Config import config
from syslog import syslog

class Mailer:
    def __init__(self):
        self.senderprog = ["/usr/sbin/sendmail", "-t"]
        self.footer = config.get("email", "footer")
        self.registerTemplate = config.get("email", "register")
        self.registerSubject = config.get("email", "registersubject")
        self.deleteTemplate = config.get("email", "delete")
        self.deleteSubject = config.get("email", "deletesubject")
        self.updateOldSubject = config.get("email", "updateoldsubject")
        self.updateOldTemplate = config.get("email", "updateold")
        self.updateNewSubject = config.get("email", "updatenewsubject")
        self.updateNewTemplate = config.get("email", "updatenew")
        self.mailaddress = config.get("email", "myaddress")
        self.doSend = self.sendWithProg
    def sendMessage(self, recipient, subject, text):
        msg = MIMEText(text, 'plain', 'utf-8')
        msg["From"] = self.mailaddress
        msg["To"] = recipient
        msg["Subject"] = Header(subject,'utf-8')
        self.doSend(msg)
    def sendWithProg(self,msg):
        p = Popen(self.senderprog, stdin=PIPE)
        p.communicate(msg.as_string())
    def registered(self, sms):
        text = self.registerTemplate.format(sms)
        text += self.footer
        self.sendMessage(sms.email, self.registerSubject, text)
    def updated(self, sms, oldemail):
        text = self.updateNewTemplate.format(sms, oldemail)
        text += self.footer
        self.sendMessage(sms.email, self.updateNewSubject, text)

        text2 = self.updateOldTemplate.format(sms, oldemail)
        text2 += self.footer
        self.sendMessage(oldemail, self.updateOldSubject, text2)
    def deleted(self, sms, oldemail):
        text = self.deleteTemplate.format(sms, oldemail)
        text += self.footer
        self.sendMessage(oldemail, self.deleteSubject, text)
    def triedUnsubNonexistent(self, sms):
        syslog("unregistered unsubscribe from %s\n"%(sms.number))

