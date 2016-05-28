#!/usr/bin/python
## http://www.practicepython.org/
import sys
__author__ = 'tomas.balazsik'

def zadaj():
 try:
  num = int(raw_input('Zadaj cislo ktore chces skontrolovat : '))
 except ValueError:
  print "nezadal si cislo"
  sys.exit(2)
 return num

def makaj(num):
 b=[]
 x = range(2, num-1)
 for delitel in x: 
   if num % delitel == 0:
    b.append(delitel)
    break
 return b

x = zadaj()
if (x == 0) or (x == 1):
 print("nie je prvocislo")
else:
 if len(makaj(x)) == 0:
  print("je to prvocislo")
 else: 
  print("nie je prvocislo")
