#!/usr/bin/python
# http://www.practicepython.org/
from sets import Set
import random

a = random.sample(range(0,100),25)
b = random.sample(range(0,100),30)

c = []
print a,'\n',b
for cislo in a:
  for num in b:
    if cislo == num:
      c.append(cislo)

print list(set(c))

