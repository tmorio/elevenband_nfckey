import logging
log = logging.getLogger('main')

import os
import sys
import time
import string
import struct
import argparse
import hmac, hashlib

sys.path.insert(1, os.path.split(sys.path[0])[0])
from cli import CommandLineInterface
import binascii
import nfc
import nfc.clf

def on_connect(tag):
	print tag
	print tag.type
	print binascii.hexlify(tag.identifier).upper()

def main():
	clf = nfc.ContactlessFrontend("usb")

	rdwr_options = {
		'targets': ['212F' , '424F'],
		'on-connect': on_connect,
	}
	clf.connect(rdwr=rdwr_options)

if __name__ == '__main__':
	main()
