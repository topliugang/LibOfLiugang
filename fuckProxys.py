#encoding:UTF-8
import mylib
from bs4 import BeautifulSoup
import re
import sqllib



def fuck_xicidaili():
	urls = []
	proxys = list()

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
			proxys.append((ip, port))
	return proxys
		
		
		

def fuck_kuaidaili():
	urls = []
	proxys = list()

	for i in range(10, 1, -1):
		urls.append('http://www.kuaidaili.com/free/inha/%d/'%i) 
		urls.append('http://www.kuaidaili.com/free/outha/%d/'%i) 
	
	for url in urls:
		html = mylib.get_html_from_url(url)
		
		if html:
			soup = BeautifulSoup(html, 'html.parser')
			table = soup.select('tbody')[0]
			trs = table.select('tr')
			for tr in trs:
				tds = tr.select('td')
				ip = tds[0].string
				port = tds[1].string
				#put into dict
				proxys.append((ip, port))
	return proxys
		
		

def fuck_nianshao():
	urls = []
	proxys = list()

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
			proxys.append((ip, port))
	return proxys
		
			

def fuck_89ip():
	url = 'http://www.89ip.cn/tiqu.php?sxb=&tqsl=5000&ports=&ktip=&xl=on&submit=%CC%E1++%C8%A1'
	proxys = list()
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
		port = port[1:]
		proxys.append((ip, port))
	return proxys


def fuck_spys():
	url = 'http://spys.ru/free-proxy-list/CN/'
	proxys = list()
	html = mylib.get_html_from_url(url, proxy_str='127.0.0.1:8087')
	print html

"""
http://spys.ru/free-proxy-list/CN/
http://www.gatherproxy.com/proxylist/country/?c=China
http://www.gatherproxy.com/zh/
http://cnproxy.com/proxy1.html
http://www.proxylisty.com/country/China-ip-list
"""
def check_proxy(ip, port):
	url = 'http://www.ip138.com/'
	mylib.get_html_from_url(url, proxy_str = '%s:%s'%(ip, port))


if __name__ == '__main__':
	
	sqllib.delete_all()
	sqllib.insert(fuck_xicidaili())	
	#sqllib.insert(fuck_kuaidaili())
	#sqllib.insert(fuck_nianshao())
	#sqllib.insert(fuck_89ip())
	ip_port_list = sqllib.select()
	for ip, port in ip_port_list:
		check_proxy( ip, port )