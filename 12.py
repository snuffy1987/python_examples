#!/usr/bin/python
## http://www.practicepython.org/

a = [5, 10, 15, 20, 25, 30]
b = []

def list_end():
 return [a[0], a[len(a)-1]]

b = list_end()
print b
