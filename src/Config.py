#!/usr/bin/python

import ConfigParser, os

config = ConfigParser.ConfigParser()
config.read(['/etc/smsregistry.cfg', 'smsregistry.cfg'])

