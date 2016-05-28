#!/usr/bin/python
## http://www.practicepython.org/
from sets import Set
# povodne zadanie bolo moc lahke (kedze obsahovalo iba vymazanie duplikatov) , ja som ho zmenil na celkove vymazanie duplicitnych mien zo zoznamu

names = ["Robin", "Robin", "Sara", "Sara", "Michele", "Michele", "Tomas", "Sara"]

def removedupli(pole):
 pole2 = []
 i = 0
 b = 0
 while i < len(pole):
   while b < len(pole):
    if i != b:
     if str(pole[i]) == str(pole[b]):
      pole2.append(pole[i]) 
     b = b + 1
    else:
     b = b + 1
   i = i + 1
   b = 0
 return pole2

pole2 = set(removedupli(names))
pole = set(names).difference(pole2)
print list(pole)
