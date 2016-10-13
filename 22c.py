#!/usr/bin/python
## http://www.practicepython.org/
__author__ = 'tomas.balazsik'

count = {}
with open('nameslist.txt', 'r') as subor:
 pole=subor.read().splitlines()
for i in pole:
 category=i.split("/")[2]
 if count.get(category, None):
  count[category] += 1
 else:
  count[category] = 1

print count
