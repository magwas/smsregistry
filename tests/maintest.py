#!/usr/bin/python

import unittest
from Main import Main
from SmsStorage import SmsStorage
from FakeMailer import FakeMailer

def fakeRemove(sms):
    print "removing {0}".format(sms.location)

class maintest(unittest.TestCase):

    def test_main(self):
        with open ("testdata/testdata_manygood", "r") as myfile:
            self.manygood = myfile.readlines()
        allSms = SmsStorage(self.manygood)
        mailer = FakeMailer()
        prg = Main(mailer)
        prg.doRemove = fakeRemove
        prg.processLoop(allSms)
        self.assertEquals(prg.db.getEmailFor("+36209303349"),"mag@magwas.rulez.org")
        self.assertEquals(prg.db.getEmailFor("+36209301112"),"m4gw4s@gmai.com")
        self.assertEquals(prg.db.getEmailFor("+36209301113"),"mag+vote@magwas.rulez.org")
        self.assertEquals(prg.db.getEmailFor("+36209301114"),"mag-voter@demokracia.rulez.org")
        self.assertEquals(prg.db.getEmailFor("+36209301115"),"m4gw4s@gmail.com")
        with open ("testdata/testdata_updates", "r") as myfile:
            self.updates = myfile.readlines()
        allSms = SmsStorage(self.updates)
        prg.processLoop(allSms)
        self.assertEquals(prg.db.getEmailFor("+36209303349"),"mag@magwas.rulez.org")
        self.assertEquals(prg.db.getEmailFor("+36209301112"),"m4gw4ska@gmai.com")
        self.assertEquals(prg.db.getEmailFor("+36209301113"), None)
        self.assertEquals(prg.db.getEmailFor("+36209301114"), None)
        self.assertEquals(prg.db.getEmailFor("+36209301115"),"m4gw4s4bb@gmail.com")

if __name__ == '__main__':
        unittest.main()
