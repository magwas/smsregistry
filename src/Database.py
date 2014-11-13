#!/usr/bin/python

import sqlite3
import hashlib
from Config import config
from syslog import syslog

class Database:
    def __init__(self, mailer):
        self.mailer = mailer
        self.dbfilename = config.get("storage", "dbfile")
        self.secret = config.get("storage", "secret")
        self.conn = sqlite3.connect(self.dbfilename)
        cursor = self.conn.cursor()
        cursor.execute("create table if not exists voterregistry ( number text , email text )")
        cursor.close()

    def hash(self, number):
        hashable= self.secret + number
        sha = hashlib.sha512()
        sha.update(hashable)
        digest = sha.hexdigest()
        return digest

    def add(self, sms):
        #print sms.number,sms.email,sms.valid,sms.unsub
        if not (sms.valid or sms.unsub):
            return
        hashed = self.hash(sms.number)
        oldemail = self.getEmailFor(sms.number)
        cursor = self.conn.cursor()
        if sms.unsub is not None:
            cursor.execute("delete from voterregistry where number=?",(hashed,))
            self.conn.commit()
            if oldemail is not None:
                syslog("unsub {0}".format(oldemail))
                self.mailer.deleted(sms,oldemail)
            else:
                syslog("unsub nonexistent".format(oldemail))
                self.mailer.triedUnsubNonexistent(sms)
        else:
            if oldemail is not None:
                syslog("update {1} to {0.email}".format(sms,oldemail))
                cursor.execute("update voterregistry set email=? where number=?",(sms.email,hashed))
                self.conn.commit()
                self.mailer.updated(sms,oldemail)
            else:
                syslog("register {0.email}".format(sms))
                cursor.execute("insert into voterregistry (number, email) values (?, ?)",(hashed, sms.email))
                self.conn.commit()
                self.mailer.registered(sms)
        cursor.close()
        
    def _Databasetest__clear(self):
        cursor = self.conn.cursor()
        cursor.execute("delete from voterregistry")
        self.conn.commit()
        cursor.close()

    def getEmailFor(self,number):
        hashed = self.hash(number)
        cursor = self.conn.cursor()
        cursor.execute("select email from voterregistry where number = ?",(hashed,))
        rows = cursor.fetchall()
        cursor.close()
        if len(rows) == 1:
            return rows[0][0]
        return None
        
    def senderExists(self,sms):
        return self.getEmailFor(sms.number) is not None
        


