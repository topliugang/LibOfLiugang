#encoding:UTF-8
import mylib
from bs4 import BeautifulSoup




def fuck_xicidaili():
	urls = []
	proxys = dict()# == proxys = {}

	for i in range(10, 1, -1):
		urls.append('http://www.xicidaili.com/nn/%d/'%i) 
		urls.append('http://www.xicidaili.com/wn/%d/'%i) 
	
	for url in urls:
		html = mylib.get_html_from_url(url)
		soup = BeautifulSoup(html, 'html.parser')
		table = soup.select('table')[0]
		trs = table.select('tr')[1:]
		for tr in trs:
			tds = tr.select('td')
			ip = tds[1].string
			port = tds[2].string
			#put into dict
			proxys[ip] = port
		
		for sb in proxys:
			print sb, proxys[sb]
		exit()

def fuck_kuaidaili():
	urls = []
	proxys = dict()# == proxys = {}

	for i in range(10, 1, -1):
		urls.append('http://www.kuaidaili.com/free/inha/%d/'%i) 
		urls.append('http://www.kuaidaili.com/free/outha/%d/'%i) 
	
	for url in urls:
		html = mylib.get_html_from_url(url)
		soup = BeautifulSoup(html, 'html.parser')
		table = soup.select('tbody')[0]
		trs = table.select('tr')
		for tr in trs:
			tds = tr.select('td')
			ip = tds[0].string
			port = tds[1].string
			#put into dict
			proxys[ip] = port
		
		for sb in proxys:
			print sb, proxys[sb]
		exit()		

def fuck_nianshao():
	urls = []
	proxys = dict()# == proxys = {}

	for i in range(10, 1, -1):
		urls.append('http://www.nianshao.me/?page=%d'%i) 
			
	for url in urls:
		html = mylib.get_html_from_url(url)
		soup = BeautifulSoup(html, 'html.parser')
		table = soup.select('tbody')[0]
		trs = table.select('tr')
		for tr in trs:
			tds = tr.select('td')
			ip = tds[0].string
			port = tds[1].string
			#put into dict
			proxys[ip] = port
		
		for sb in proxys:
			print sb, proxys[sb]
		exit()		

def fuck_89ip():
	url = 'http://www.89ip.cn/tiqu.php?sxb=&tqsl=5000&ports=&ktip=&xl=on&submit=%CC%E1++%C8%A1'
	html = mylib.get_html_from_url(url)
	soup = BeautifulSoup(html, 'html.parser')
	fuck = soup.find(class_ = "mass")
	print fuck

	"""
	table = soup.select('tbody')[0]
	trs = table.select('tr')
	for tr in trs:
		tds = tr.select('td')
		ip = tds[0].string
		port = tds[1].string
		#put into dict
		proxys[ip] = port
	
	for sb in proxys:
		print sb, proxys[sb]
	"""
if __name__ == '__main__':
	#main()
	fuck_89ip()
	

