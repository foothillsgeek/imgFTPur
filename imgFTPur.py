#/usr/bin/python env

import ConfigParser
import sys

def list_config(config):
    for section in config.sections():
        print "[" + section + "]"
        for option in config.options(section):
            print option + ": " + config.get(section,option)

def get_config(conf_file):
    config = ConfigParser.ConfigParser()
    config.read(conf_file)
    if len(config.sections()) == 0:
        sys.exit("Configuration file missing or not readable")
    else:
        return config

config_file = 'imgFTPur.conf'

config = get_config(config_file)
list_config(config)
