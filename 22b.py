#!/usr/bin/python
## http://www.practicepython.org/
# riesenie skratkou ale funkcne :)
__author__ = 'tomas.balazsik'

List = []
with open('nameslist.txt', 'r') as subor:
 pole=subor.read().splitlines()
for i in pole:
 List.append(i.split("/")[2])
set1 = set(List)
for i in set1:
 print('%s - %s') % (i, List.count(i))
