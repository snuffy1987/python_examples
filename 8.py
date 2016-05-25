#!/usr/bin/python
# http://www.practicepython.org/
import sys
__author__ = 'tomas.balazsik'

while True:
 print("Zadaj 1 pre kamen, 2 pre papier, 3 pre noznice")
 try:
  string1 = int(raw_input('Hrac 1 zadaj cislo : ' ))
  string2 = int(raw_input('Hrac 2 zadaj cislo : ' ))
 except ValueError:
  print "nezadal si cislo"
  sys.exit(2)
 if ((string1 and string2) >= 4) or ((string1 and string2) == 0 ):
  print ("bad option")
 else:
  if ((string1 == 1) and (string2 == 3)) or ((string1 == 2) and (string2 == 1)) or ((string1 == 3) and (string2 == 2)):
   print("Hrac 1 vyhrava")
  elif ((string1 == 2) and (string2 == 3)) or ((string1 == 1) and (string2 == 2)) or ((string1 == 3) and (string2 == 1)):
   print("Hrac 2 vyhrava")
  else: 
   print("Remiza..")

 try:
  string = int(raw_input('Chces koniec? Ak ano zadaj 3, inak pokracujeme..'))
 except ValueError:
  string = 0
 print string
 if string == 3:
  break
