#!/usr/bin/python

from Config import config
from SmsStorage import SmsStorage
from Database import Database
from Sms import Sms
from Mailer import Mailer
from Phone import Phone
import sys
import syslog
import traceback
import time

class Main:
    def __init__(self, mailer=None):
        if mailer is None:
            mailer = Mailer()
        self.mailer = mailer
        self.db = Database(mailer)
        self.phone = Phone()
        self.doRemove = self.remove

    def processLoop(self, storage):
        for sms in storage.getValids():
                self.db.add(sms)
                self.doRemove(sms)

    def remove(self,sms):
        self.phone.removeSms(sms)

    def oneStep(self):
        allsms = Phone().getAllSms()
        store = SmsStorage(allsms)
        self.processLoop(store)

    def main(self):
        while True:
            try:
                self.oneStep()
            except Exception, e:
                exctype, exc, tb = sys.exc_info()
                syslog.syslog("%s:%s:%s"%(exctype,str(exc),traceback.format_tb(tb)))
            time.sleep(1)

if __name__ == '__main__':
    Main().main()
