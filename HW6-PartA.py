from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = "http://py4e-data.dr-chuck.net/comments_31472.html"
html = urlopen(url, context=ctx).read()

soup = BeautifulSoup(html, "html.parser")
tags = soup('span')
count = 0
for t in tags:
	num = int (t.text)
	count = count + num
print (count)
	