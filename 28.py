#!/usr/bin/python
## http://www.practicepython.org/
__author__ = 'tomas.balazsik'

try:
 num1 = int(raw_input('Zadaj cislo 1 : '))
 num2 = int(raw_input('Zadaj cislo 2 : '))
 num3 = int(raw_input('Zadaj cislo 3 : '))
except ValueError:
 print "nezadal si cislo"
 sys.exit(2)

if (num1 > num2 and num1 > num3):
 print("Najvacsie je cislo 1")
elif (num1 < num2 and num2 > num3):
 print("Najvacsie je cislo 2")
elif num3 > num2:
  print("Najvacsie je cislo 3")
else:
 print ("Cisla sa rovnaju..")
