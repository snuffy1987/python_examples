#!/usr/bin/python
## http://www.practicepython.org/

__author__ = 'tomas.balazsik'

with open('prime.txt', 'r') as subor:
 pole=subor.read().splitlines()
with open('happy.txt', 'r') as subor2:
 pole2=subor2.read().splitlines()
subor.close()
subor2.close()

print [x for x in pole if x in pole2]
