#!/usr/bin/python
# http://www.practicepython.org/
__author__ = 'tomas.balazsik'

try:
 num = int(raw_input('Zadaj cislo ktore chces skontrolovat : '))
 check = int(raw_input('Zadaj cislo ktorym chces delit : '))
except ValueError:
 print "nezadal si cislo"
 sys.exit(2)
b=[]
x = range(2, check+1)
for delitel in x: 
  if num % delitel == 0:
   b.append(delitel)

print b
