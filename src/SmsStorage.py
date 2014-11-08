#!/usr/bin/python

import re

from Sms import Sms

class SmsStorage:
    def __init__(self, allsmsoutput):
        self.allsmsoutput = allsmsoutput
        self.smses = []
        self.location = -1
        self.isBody = False
        self.body = "no body"
        self.number = "aaa"
        self.parseStorage()

    def parseStorage(self):
        for line in self.allsmsoutput:
            bodyMatch = re.match("^\n",line)
            if bodyMatch:
                self.isBody = not self.isBody
                continue;
            if self.isBody:
                self.body = line
                continue
            locationMatch = re.match("^Location ([0-9]*)",line)
            if locationMatch:
                newlocation=int(locationMatch.groups()[0])
                if newlocation != 0:
                    self.newSms()
                self.location=newlocation
                continue;
            numberMatch = re.match(r'^Remote number',line)
            if numberMatch:
                self.number = line
        self.newSms()

    def newSms(self):
        self.isBody = False
        try:
            sms = Sms(self.location, self.body, self.number)
            self.smses.append(sms)
        except SyntaxError:
            pass

    def getSize(self):
        return len(self.smses)

    def getValids(self):
        l = []
        for sms in self.smses:
                if sms.valid or sms.unsub:
                    l.append(sms)
        return l                

    def getValidCount(self):
        return len(self.getValids())

