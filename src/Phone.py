#!/usr/bin/python

import subprocess

class Phone:

    def getAllSms(self):
       pipe = subprocess.Popen("gammu getallsms", shell=True, stdout=subprocess.PIPE).stdout
       return pipe.readlines() 

    def removeSms(self, location):
        if location <= 0:
            return
        subprocess.call(["gammu", "deletesms", "1", str(location)])
