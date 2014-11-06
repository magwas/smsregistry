#!/usr/bin/python

import unittest
from Phone import Phone
from SmsStorage import SmsStorage

class SmsTests(unittest.TestCase):
    def test_phone_interaction(self):
        #this test interacts with real hardware
        #the phone should contain one sms with a valid email address beyound the loation 0 one when starting
        phone = Phone()
        allsms = phone.getAllSms()
        store = SmsStorage(allsms)
        self.assertEquals(store.getSize(),2)
        self.assertEquals(store.getValidCount(),1)
        self.assertEquals(store.smses[0].valid, False)

        for sms in store.smses:
            phone.removeSms(sms.location)

        allsms = phone.getAllSms()
        store = SmsStorage(allsms)
        self.assertEquals(store.getSize(),1)
        self.assertEquals(store.getValidCount(),0)




if __name__ == '__main__':
        unittest.main()
