#!/usr/bin/python
## http://www.practicepython.org/
import random

__author__ = 'tomas.balazsik'

def porovnaj(gen, tip):
 stat = [0,0]
 for i in range(0,4):
  for j in range(0,4):
    if i == j:
     if tip[i] == gen[j]:
      stat[0] = stat[0] + 1
    else:
     if tip[i] == gen[j]:
      stat[1] = stat[1] + 1
 return stat

a = random.randint(1000, 9999)
is_true = 1
c = 1
while is_true:
 stat = [0,0]
 cislo = raw_input('Zadaj cislo a ja ti poviem, ci si hadal spravne :')
 if str(cislo) == "" or len(str(cislo)) != 4:
  print("Zadal si neplatne cislo..skus znovu")
  c = c + 1
 else:
  if a == int(cislo):
   print("uhadol si a potreboval si na to %s pokusov!!!") % (c)
   is_true = 0
  else:
   vysledok = porovnaj(str(a), str(cislo))
   c = c + 1
   print ("Mas %s cows a %s bulls") % (vysledok[0], vysledok[1])
