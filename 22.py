#!/usr/bin/python
## http://www.practicepython.org/

__author__ = 'tomas.balazsik'

with open('nameslist.txt', 'r') as subor:
 pole=subor.read().splitlines()
subor.close()
set1 = set(pole)
for i in set1:
 print('%s - %s') % (i, pole.count(i))
