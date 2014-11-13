#!/usr/bin/python

import unittest
from SmsStorage import SmsStorage

class SmsParseTests(unittest.TestCase):
    def setUp(self):
        with open ("testdata/testdata_emptystore", "r") as myfile:
            self.emptystore = myfile.readlines()
        with open ("testdata/testdata_onesms", "r") as myfile:
            self.onesms = myfile.readlines()
        with open ("testdata/testdata_twosms", "r") as myfile:
            self.twosms = myfile.readlines()
        with open ("testdata/testdata_twosms_badformat", "r") as myfile:
            self.badformat = myfile.readlines()
        with open ("testdata/nophone", "r") as myfile:
            self.nophone = myfile.readlines()


    def test_setUp(self):
        self.assertEquals(len(self.onesms),13)

    def test_first_stored_sms_is_ignored_due_to_gammu(self):
        allSms = SmsStorage(self.onesms)
        self.assertEquals(allSms.getSize(),1)
        self.assertEquals(allSms.getValidCount(), 0)

    def test_empty_storage_contains_zero_sms(self):
        allSms = SmsStorage(self.emptystore)
        self.assertEquals(allSms.getValidCount(), 0)

    def test_storage_with_two_contains_one_useable_sms(self):
        allSms = SmsStorage(self.twosms)
        self.assertEquals(allSms.getValidCount(), 1)
        self.assertEquals(allSms.getValids()[0].location, 1)

    def test_bad_sms_does_not_count(self):
        allSms = SmsStorage(self.badformat)
        self.assertEquals(allSms.getValidCount(), 0)
            
    def test_email_available(self):
        allSms = SmsStorage(self.twosms)
        self.assertEquals(allSms.getValids()[0].email, "mag@magwas.rulez.org")

    def test_number_available(self):
        allSms = SmsStorage(self.twosms)
        self.assertEquals(allSms.getValids()[0].number, "+36209303349")

    def test_phone_error(self):
        with self.assertRaises(ValueError):
            SmsStorage(self.nophone)

if __name__ == '__main__':
        unittest.main()
