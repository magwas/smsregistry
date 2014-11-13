#!/usr/bin/python

class FakeMailer:
    def __init__(self):
        self.log = []
    def registered(self, sms):
        self.log.append(("registered", sms.number, sms.email))
    def deleted(self, sms, oldemail):
        self.log.append(("deleted", sms.number, oldemail))
    def updated(self, sms, oldemail):
        self.log.append(("updated", sms.number, sms.email, oldemail))
    def triedUnsubNonexistent(self, sms):
        self.log.append(("tried", sms.number))

