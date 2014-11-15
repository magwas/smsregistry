#!/usr/bin/python

import unittest
from Config import config
from SmsStorage import SmsStorage
from Database import Database
from Sms import Sms
from FakeMailer import FakeMailer


class Databasetest(unittest.TestCase):

    def setUp(self):
        self.assertEquals(config.get("storage", "dbfile"), "testdata/db.sqlite3")
        with open ("testdata/testdata_twosms", "r") as myfile:
            self.twosms = myfile.readlines()
        with open ("testdata/testdata_manygood", "r") as myfile:
            self.manygood = myfile.readlines()
        with open ("testdata/errordump_utopszkij", "r") as myfile:
            self.utopszkij = myfile.readlines()
        mailer = FakeMailer()
        self.db = Database(mailer)
        self.db.__clear()

    def test_storage_with_two_contains_one_useable_sms(self):
        allSms = SmsStorage(self.twosms)
        for sms in allSms.getValids():
            self.assertFalse(self.db.senderExists(sms))
        for sms in allSms.getValids():
            self.db.add(sms)
        for sms in allSms.getValids():
            self.assertTrue(self.db.senderExists(sms))

    def test_storage_with_many_works_well(self):
        allSms = SmsStorage(self.manygood)
        for sms in allSms.getValids():
            self.assertFalse(self.db.senderExists(sms))
        for sms in allSms.getValids():
            self.db.add(sms)
        for sms in allSms.getValids():
            self.assertTrue(self.db.senderExists(sms))

    def test_update(self):
        allSms = SmsStorage(self.manygood)
        for sms in allSms.getValids():
            self.db.add(sms)
        self.assertEquals(self.db.getEmailFor("+36209303349"),"mag@magwas.rulez.org")
        sms = Sms(5, "a Cimem: m4gw4s@gmail.com\n", "+36209303349")
        self.db.add(sms)
        self.assertEquals(self.db.getEmailFor("+36209303349"),sms.email)

    def test_delete(self):
        allSms = SmsStorage(self.manygood)
        for sms in allSms.getValids():
            self.db.add(sms)
        self.assertEquals(self.db.getEmailFor("+36209303349"),"mag@magwas.rulez.org")
        sms = Sms(5, "unsub\n", "+36209303349")
        self.db.add(sms)
        self.assertEquals(self.db.getEmailFor("+36209303349"),None)

    def test_utopszkij(self):
        allSms = SmsStorage(self.utopszkij)
        for sms in allSms.getValids():
            self.db.add(sms)
        self.assertEquals(self.db.mailer.log,[('registered', '+36302222201', 'tibor.nemtibor@gmail.com\n2 sms parts in 2 sms sequences')])

if __name__ == '__main__':
        unittest.main()
