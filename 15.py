#!/usr/bin/python
## http://www.practicepython.org/

retazec = raw_input('Zadaj retazec : ')
def otoc(retazec):
 db = retazec.split()
 db.reverse()

 return " ".join(db)

print otoc(retazec)
