#!/usr/bin/python
## http://www.practicepython.org/

import sys

try:
 num = int(raw_input('Zadaj cislo ktore chces skontrolovat : '))
 check = int(raw_input('Zadaj cislo ktorym chces delit : '))
except ValueError:
 print "nezadal si cislo"
 sys.exit(2)

if num % 4 == 0:
 print("je delitelne 4")
else:
 if num % 2 == 0:
  print("je delitelne 2")
 else:
  print("je neparne")

if num % check == 0:
  print('{} je delitelne cislom {}').format(num, check)
else:
  print('{} nie je delitelne cislom {}').format(num, check)
