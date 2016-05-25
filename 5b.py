#!/usr/bin/python
# http://www.practicepython.org/
from sets import Set
__author__ = 'tomas.balazsik'

a = set([1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 99])
b = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 99])
#print a,'\n',b

print a.intersection(b)
