#!/usr/bin/python
# http://www.practicepython.org/
from datetime import date
import sys

meno = raw_input('Zadaj meno : ')

if not meno:
 print ("nezadal si meno")
 sys.exit(1)
try:
 vek = int(raw_input('Zadaj vek : '))
 opak = int(raw_input('Zadaj cislo pre opakovanie : '))
except ValueError:
 print "nezadal si cislo"
 sys.exit(2)
if vek > 100:
 print("100 rokov uz mas")
else:
 count = 0
 while (count < opak):
   count = count + 1
   print('Tvoje meno je {} rokov mas  {} a 100 rokov budes mat v roku {}.'.format(meno, vek, date.today().year-vek+99))
# print('Tvoje meno je %s rokov mas  %s a 100 rokov budes mat v roku %s.' % (meno, vek, date.today().year-vek+99))
