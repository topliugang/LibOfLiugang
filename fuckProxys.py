#encoding:UTF-8
import mylib
from bs4 import BeautifulSoup
import re




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
		
			

def fuck_89ip():
	url = 'http://www.89ip.cn/tiqu.php?sxb=&tqsl=5000&ports=&ktip=&xl=on&submit=%CC%E1++%C8%A1'
	proxys = dict()# == proxys = {}
	html = mylib.get_html_from_url(url)
	#html = unicode(html, "gb2312").encode("utf8")
	#编码问题 显示的时候加上
	ip_port_pattern = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}:\d{1,5}')
	ip_ports = ip_port_pattern.findall(html)
	for ip_port in ip_ports:
		ip_pattern = re.compile(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}')
		ip = ip_pattern.match(ip_port).group()
		#print ip
		port_pattern = re.compile(r':\d{1,5}')
		port = port_pattern.findall(ip_port)[0]
		#print port[1:]
		proxys[ip] = port[1:]



http://spys.ru/free-proxy-list/CN/
http://gatherproxy.com/proxylist/country/?c=China
http://cnproxy.com/proxy1.html
http://www.proxylisty.com/country/China-ip-list


if __name__ == '__main__':
	#main()
	#fuck_89ip()
	fuck_89ip()


