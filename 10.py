#!/usr/bin/python
## http://www.practicepython.org/
from sets import Set
import random

a = random.sample(range(100), 10)
b = random.sample(range(100), 15)
c = [cislo for cislo in a for cislo2 in b if cislo == cislo2]

print a,b
print ("Prienik 2 poli je %s") % list(set(c))
