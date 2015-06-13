#/usr/bin/python env

import ConfigParser
import sys

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

def list_config(config):
    for section in config.sections():
        print "[" + section + "]"
        for option in config.options(section):
            print option + ": " + config.get(section, option)

def get_config(conf_file):
    config = ConfigParser.ConfigParser()
    config.read(conf_file)
    if len(config.sections()) == 0:
        sys.exit("Configuration file missing or not readable")
    else:
        return config

def ftpd(config):
    authorizer = DummyAuthorizer()
    authorizer.add_user(
        str(config.get('FTPSettings', 'username')), 
        config.get('FTPSettings', 'password'), 
        config.get('FTPSettings', 'incomingfolder'), 
        perm="elradfmw")
    handler = FTPHandler
    handler.authorizer = authorizer
    server = FTPServer((config.get('FTPSettings', 'ipaddress'), config.get('FTPSettings', 'port')), handler)
    server.serve_forever()

config_file = 'imgFTPur.conf'

config = get_config(config_file)
#list_config(config)
ftpd(config)
