import os
import re
import sys
import logging
import configparser


def readConfigure():
    try:
        root = os.path.dirname(os.path.dirname(os.path.realpath(__file__)))
        # currently config.ini is in example folder
        config_path = os.path.join(root, 'examples/config.ini')
        # TODO: There is a better way to log this message than print.
        print "Reading secrets from %r" % config_path

        parser = configparser.ConfigParser()
        parser.read(config_path)
        config_data = dict(parser.items("default"))
    except Exception as e:
        # TODO: There is a better way to log this message than print.
        print 'Failed to load config.ini.  Reason: %r' % str(e)
