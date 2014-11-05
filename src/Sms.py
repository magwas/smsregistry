#!/usr/bin/python

import re

class Sms:
    def __init__(self, location, body, number):
        self.location = location
        self.valid = False
        self.email = re.sub(r".*?([\w\.]*@[\w\.]*).*",r"\1",body.strip()).lower()
        self.number = re.sub(r'^Remote number        : "(\+36[0-9]*).*"', r"\1", number.strip())

        if re.match(".*@.*\..*",self.email) and location >= 1:
            self.valid = True

