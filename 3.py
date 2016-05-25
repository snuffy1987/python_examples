#!/usr/bin/python
# http://www.practicepython.org/
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b=[]

try:
 num = int(raw_input('Zadaj cislo ktore chces skontrolovat : '))
except ValueError:
 print "nezadal si cislo"
 sys.exit(2)

for i in a:
  if i < num:  
   b.append(i)

print b
