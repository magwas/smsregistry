#!/usr/bin/python

import re

emailre = r"""([a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?)"""
class Sms:
    def __init__(self, location, body, number):
        self.location = location
        self.valid = False
        normbody = body.strip().lower()
        #self.email = re.sub(r".*?([\w\.\-\+]*@[\w\.]*).*",r"\1",normbody)
        #self.emailgot = re.search(r"([a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4})",normbody)
        self.emailgot = re.search(emailre,normbody)
        # from http://www.regular-expressions.info/email.html
        self.email = None
        if self.emailgot is not None:
            found = self.emailgot.groups()
            self.email = found[0]
        self.unsub = re.match(r".*unsub.*",normbody)
        self.number = re.sub(r'^Remote number        : "(\+36[0-9]*).*"', r"\1", number.strip())

        if (self.email is not None) and location >= 1:
            self.valid = True
