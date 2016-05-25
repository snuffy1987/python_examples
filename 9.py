#!/usr/bin/python
## http://www.practicepython.org/
import random

def generate():
 a = random.randint(1,9)
 return a

a = generate()
is_true = 0
c = 1

while not is_true:
 cislo = raw_input('Zadaj cislo a ja ti poviem, ci si hadal spravne (napis "quit" alebo stlac enter pre koniec) :')
 if str(cislo) == "" or str(cislo) == "quit":
  is_true=1
 if str(cislo) == "" or str(cislo) == "quit":
  is_true=1
 else:
  if a == int(cislo):
   print("uhadol si a potreboval si na to %s pokusov!!!") % (c)
   a = generate()
   c = 1
  elif int(cislo) < a:
   print("Musis zvysit")
   c = c + 1
  else:
   print("Musis znizit")
   c = c + 1

