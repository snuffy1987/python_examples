#!/usr/bin/python
## http://www.practicepython.org/

__author__ = 'tomas.balazsik'

try:
 num1 = int(raw_input('Zadaj cislo policok v matici: '))
except ValueError:
 print "nezadal si cislo"
 sys.exit(2)

print (" ---") * num1
for i in range (0, num1):
 print ("|   ") * int(num1+1)
 print (" ---") * num1
