#!/usr/bin/python
## http://www.practicepython.org/
#binary search
__author__ = 'tomas.balazsik'
import sys,random

stred=random.randint(0, 100)
L=0
R=100
i=1

while i:
 try:
  print ("Hadam cislo ====> %s <====") % (stred)
  string1 = raw_input("Je tvoje cislo - 'l' mensie, 'h' vacsie, e 'rovnake'?")
 except ValueError:
  print "nezadal si cislo"
  sys.exit(2)
 
 if L+1 == R:
  print ("Vycerpal som vsetky moznosti")
  i=0

 if (string1 == "e"):
  print ("Nasiel som to na %s pokusov") % (i) 
  i=0
 elif (string1 == "h" ):
  L=stred
  stred = (L+R)/2
  i=i+1
  print L,R,stred
 elif (string1 == "l" ):
  R=stred
  stred = (L+R)/2
  i=i+1
  print L,R,stred
