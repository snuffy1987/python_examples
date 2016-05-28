#!/usr/bin/python
## http://www.practicepython.org/
import random
import sys
__author__ = 'tomas.balazsik'



try:
 num = int(raw_input('Kolko znakov ma mat heslo? '))
except ValueError:
 print "nezadal si cislo"
 sys.exit(2)

p = random.sample("abcdefghijklmnopqrstuvwxyz01234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?", num )
print "Password:", "" .join(p)
