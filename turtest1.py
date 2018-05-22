import requests
from bs4 import BeautifulSoup

r = requests.get('http://www.baidu.com')
if r.status_code == 200:
	r.encoding = 'utf-8'
	bfs = BeautifulSoup(r.text, "lxml")
	print(bfs.find_all('div'))
