import urllib.requst
import urllib.parse
importre

url = 'http://pythonprogramming.net'
values = {'s':'basics','submit':'search'}
data = urllib.pares.urlencode(values)
data = data.encode('utf-8')
req = urllib.requst.Requst(url, data)
resp = urllib.requst.urlopen(req)
resData = resp.read()
#print(respData)

paragraphs = re.findall(r'<p>(.*?)</p>',str(resData))

for eachP in paragraphs:
	print(eachP)