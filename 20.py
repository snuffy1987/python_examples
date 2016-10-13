#!/usr/bin/python
## http://www.practicepython.org/
#binary search
__author__ = 'tomas.balazsik'

import sys
zoznam=(range(99999))
#print zoznam
cislo = int(raw_input('Ktore cislo chces hladat? '))
L = 0
R = len(zoznam)
m = (L+R)/2
i = 1


def hladaj(L,R,m,i):
 print ("L %s R %s m %s") % (L, R, m)
 if L > R:
  print ("nenachadza sa (pocet skokov %s)") % (i)
  sys.exit(2)
 elif zoznam[m] < cislo:
  L=m+1
  m=(L+R)/2
  i=i+1
  hladaj(L,R,m,i)
 elif zoznam[m] > cislo:
  R=m-1
  m=(L+R)/2
  i=i+1
  hladaj(L,R,m,i)
 else:
  print ("najdene v zozname na pozicii %s s poctom skokov %s") % (m, i)
hladaj(L,R,m,i)
