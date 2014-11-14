#!/usr/bin/python

import unittest
from Config import config
from Sms import Sms
from Mailer import Mailer

class FakeSender:
    def __init__(self):
        self.sent = []
    def send(self, msg):
        self.sent.append(msg)

class MailerTest(unittest.TestCase):

    def test_send_registration(self):
        sms = Sms(5, "a Cimem: m4gw4s@gmail.com\n", "+36209303349")
        mailer = Mailer()
        sender = FakeSender()
        mailer.doSend = sender.send
        mailer.registered(sms)
        with open("testdata/registration_msg") as f:
            expected = f.read()
        self.assertEquals(expected,sender.sent[0].as_string())

    def test_send_update(self):
        sms = Sms(5, "a Cimem: m4gw4ska@gmail.com\n", "+36209303349")
        mailer = Mailer()
        sender = FakeSender()
        mailer.doSend = sender.send
        mailer.updated(sms, "m4gw4s@gmail.com")
        with open("testdata/update_registerer_msg") as f:
            expected_new = f.read()
        with open("testdata/update_oldaddress_msg") as f:
            expected_old = f.read()
        self.assertEquals(expected_new,sender.sent[0].as_string())
        self.assertEquals(expected_old,sender.sent[1].as_string())

    def test_send_delete(self):
        sms = Sms(5, "m: m4gw4ska@gmail.com\n", "+36209303349")
        mailer = Mailer()
        sender = FakeSender()
        mailer.doSend = sender.send
        mailer.deleted(sms, "m4gw4s@gmail.com")
        with open("testdata/delete_msg") as f:
            expected = f.read()
        self.assertEquals(expected,sender.sent[0].as_string())

    def test_sendmail_is_missing(self):
        sms = Sms(5, "a Cimem: m4gw4s@gmail.com\n", "+36209303349")
        mailer = Mailer()
        mailer.senderprog = ["/nonexistent/binary"]
        with self.assertRaises(OSError):
            mailer.registered(sms)

    def test_sendmail_fails(self):
        sms = Sms(5, "a Cimem: m4gw4s@gmail.com\n", "+36209303349")
        mailer = Mailer()
        mailer.senderprog = ["tests/badscript"]
        with self.assertRaises(ValueError):
            mailer.registered(sms)

if __name__ == '__main__':
        unittest.main()
