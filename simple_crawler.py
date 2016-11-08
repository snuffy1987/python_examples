#!/usr/bin/python
import requests

headers = {  'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Trident/7.0; rv:11.0) like Gecko' }
IP = '212.58.244'

result = {} 
i = 0 #obycajny counter na to aby sme vedeli kolko IP adries sme oskenovali
up = 0 #counter na to aby sme vedeli kolko adries ma otvoreny port 80

class server:
 def __init__(self, response_code, url, server_signature = "none"):
  self.response_code = response_code
  self.signature = server_signature
  self.url = url
 def ukazServer(self):
  print "RC: ", self.response_code, ", signature: ", self.signature, ", url: ", self.url 


for x in range(1, 100):
  url = ("%s.%d") % (IP, x)
  i = i + 1
  try:
    r = requests.get("http://%s" % url, headers=headers, timeout=0.5)
#    print ("%s - %d - %s") % (url, r.status_code, r.url)
    if r.status_code:
      up = up + 1
      if "Server" in r.headers:
       result[up]=server(r.status_code, r.url, r.headers['Server'])
      else:
       result[up]=server(r.status_code, r.url)
  except:
    pass

print ("scanned %d IP addresses, %d seems to be up") % (i, up)
print ("----------------------")

for x in range(1, up+1):
 result[x].ukazServer()
