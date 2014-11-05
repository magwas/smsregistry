#!/usr/bin/python

import unittest
from Sms import Sms

class SmsTests(unittest.TestCase):
    def test_email_parsed_correctly(self):
        sms = Sms(5, "a Cimem: test@example.com\n", "+36209303349")
        self.assertEquals(sms.email, "test@example.com")

    def test_dotted_address_parsed_correctly(self):
        sms = Sms(5, "a Cimem: test.dummy@example.com\n", "+36209303349")
        self.assertEquals(sms.email, "test.dummy@example.com")

    def test_junk_is_refused(self):
        sms = Sms(5, "a Cimem: test.dummy.example.com\n", "+36209303349")
        self.assertFalse(sms.valid)

if __name__ == '__main__':
        unittest.main()
