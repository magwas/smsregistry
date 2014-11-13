#!/usr/bin/python

import subprocess

class Phone:

    def getAllSms(self):
       pipe = subprocess.Popen("gammu getallsms", shell=True, stdout=subprocess.PIPE).stdout
       return pipe.readlines() 

    def removeSms(self, sms):
        if sms.location <= 0:
            return
        args = ["gammu", "deletesms", "1", str(sms.location)]
        subprocess.call(args)
