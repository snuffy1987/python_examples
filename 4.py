#!/usr/bin/python
## http://www.practicepython.org/
__author__ = 'tomas.balazsik'

try:
 num = int(raw_input('Zadaj cislo ktore chces skontrolovat : '))
except ValueError:
 print "nezadal si cislo"
 sys.exit(2)
b=[]
x = range(2, num+1)
for delitel in x: 
  if num % delitel == 0:
   b.append(delitel)
print b
