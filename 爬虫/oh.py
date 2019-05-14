Python 3.7.2 (tags/v3.7.2:9a3ffc0492, Dec 23 2018, 23:09:28) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import requests
>>> r=requests.get("http://python123.io/ws/demo.html")
>>> demo=r.text
>>> demo
'<html><head><title>This is a python demo page</title></head>\r\n<body>\r\n<p class="title"><b>The demo python introduces several python courses.</b></p>\r\n<p class="course">Python is a wonderful general-purpose programming language. You can learn Python from novice to professional by tracking the following courses:\r\n<a href="http://www.icourse163.org/course/BIT-268001" class="py1" id="link1">Basic Python</a> and <a href="http://www.icourse163.org/course/BIT-1001870001" class="py2" id="link2">Advanced Python</a>.</p>\r\n</body></html>'
>>> from bs4 import BeautifulSoup
>>> soup=BeautifulSoup(demo,"html.parser")
>>> for link in soup.find_all('a'):
	print(link.get('href'))

	
http://www.icourse163.org/course/BIT-268001
http://www.icourse163.org/course/BIT-1001870001
>>> 
