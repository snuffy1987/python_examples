#!/usr/bin/python
# http://www.practicepython.org/
__author__ = 'tomas.balazsik'

string = raw_input("Zadaj retazec a ja zistim ci je palindrome:")

a = 0
b = len(string) - 1


for a in range(0, (len(string) -1)): 
 if string[a] == string [b]:
  a = a+1
  b = b-1
  if b == 1:
   print ("je to palindrome")
 else:
  print ("not palindrome")
  break
