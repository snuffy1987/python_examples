#!/usr/bin/python
## http://www.practicepython.org/
__author__ = 'tomas.balazsik'

try:
 num = int(raw_input('Zadaj kolko cisel Fibonnaci chces vyratat : '))
except ValueError:
 print "nezadal si cislo"
 sys.exit(2)

def fib(num):
 if num <= 1:
  return num
 else:
  F = fib(num-2) + fib(num-1)
 return F

print fib(num)
