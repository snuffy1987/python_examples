#!/usr/bin/python
import requests
from datetime import datetime
import re
import dns.resolver

"""simple crawler je jednoduchy crawler, ktory oskenuje IPadresy, ulozi response code, Server signature a na konci vypise statistiku. Pri skenovani velkeho rozsahu je limitujuci faktor pamat, pretoze pocas skenovania sa priebezne vysledky ukladaju do pamate - co nie je vhodne riesenie, ale pre moje ucely mi to postacovalo"""

headers = {  'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko' }
IP = '127.'

result = {} 
i = 0 #obycajny counter na to aby sme vedeli kolko IP adries sme oskenovali
up = 0 #counter na to aby sme vedeli kolko adries ma otvoreny port 80
t1=datetime.now()

#zadefinujeme si triedu server s danymi parametrami
class server:
 def __init__(self, response_code, url, server_signature = "none"):
  self.response_code = response_code
  self.signature = server_signature
  self.url = url
 def ukazServer(self): #just for fun here
  print "RC:", self.response_code, " signature:", self.signature, " URL:", self.url
 def __str__(self):
  return "RC: {:d} SIG: {:s} URL: {:s}\n".format(self.response_code,self.signature, self.url)

#skenovanie rozsahu a vytvorenie instancii triedy server
for x in range(58, 59):
 for c in range(244, 245):
  for b in range(1, 255):
   url = ("%s%d.%d.%d") % (IP, x, c, b)
   i = i + 1
   try:
     r = requests.get("http://%s" % url, headers=headers, timeout=0.5)
     if r.status_code:
       up = up + 1
#       try:
#        myResolver = dns.resolver.Resolver()
#        req = '.'.join(reversed(url.split("."))) + ".in-addr.arpa"
#        answer = myResolver.query(req, "PTR")
#        for rdata in answer:
#         answer = rdata
#       except:
#        answer = "none"
       if "Server" in r.headers:
        result[up]=server(r.status_code, r.url, r.headers['Server'])
       else:
        result[up]=server(r.status_code, r.url)
       result[up].ukazServer()
   except:
     pass

# prechadzame instancie a zapiseme do suboru vysledky
with open ('results.txt', 'w') as f:
 for x in range(1, up+1):
  f.write (str(result[x]))
  del result[x]
print ("----------------------")
t2=datetime.now()
print ("scanned %d IP addresses, %d seems to be up, scanning took %s s") % (i, up, t2-t1)

count_RC = {}
count_SIG = {}
with open('results.txt', 'r') as subor:
 pole=subor.read().splitlines()
for i in pole:
 RC = i.split(" ")[1]
 m = re.match(r"(?:^RC:\s\d{3}\sSIG:\s)(.*)(?:\sURL:.*)", i)
 SIG = m.group(1)
 if count_RC.get(RC, None):
  count_RC[RC] += 1
 else:
  count_RC[RC] = 1
 if count_SIG.get(SIG, None):
  count_SIG[SIG] += 1
 else:
  count_SIG[SIG] = 1

maxim = 0
for i in count_SIG.keys():
 if maxim < len(i):
  maxim = len(i)

for i in  count_RC.keys():
 print "RC: ",i+" "* (maxim-len(i)), "-" * (30 * count_RC.get(i) / up), " " , count_RC.get(i)
for i in  count_SIG.keys():
 print "SIG: ",i+" "* (maxim-len(i)), "-" * (30 * count_SIG.get(i) / up)," ", count_SIG.get(i)
