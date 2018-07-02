#!/usr/bin/env python
import nfc
def connected(tag):
  print tag
  print str(tag.identifier).encode('hex').upper()
clf = nfc.ContactlessFrontend('usb')
clf.connect(rdwr={'on-connect': connected})
