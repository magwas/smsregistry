#!/usr/bin/python

import re

class Sms:
    def __init__(self, location, body, number):
        self.location = location
        self.valid = False
        normbody = body.strip().lower()
        #self.email = re.sub(r".*?([\w\.\-\+]*@[\w\.]*).*",r"\1",normbody)
        self.emailgot = re.search(r"([a-z0-9._%+-]+@[a-z0-9.-]+\.[a-z]{2,4})",normbody)
        # from http://www.regular-expressions.info/email.html
        found = self.emailgot.groups()
        if len(found) == 1 :
            self.email = found[0]
        else:
            self.email = None
        self.unsub = re.match(r".*unsub.*",normbody)
        self.number = re.sub(r'^Remote number        : "(\+36[0-9]*).*"', r"\1", number.strip())

        if (self.email is not None) and location >= 1:
            self.valid = True
