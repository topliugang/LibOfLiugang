import urllib
import urllib2 
import random
import threading
import time
import cookielib
from bs4 import BeautifulSoup
import sqlite3


def get_proxys_from_url(url):
	ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
	request = urllib2.Request(url)
	request.add_header('User-Agent', ua)
	response = urllib2.urlopen(request)
	html = response.read()

	soup = BeautifulSoup(html)
	table = soup.select('table')[0]
	trs = table.select('tr')[1:]

	conn = sqlite3.connect('fuck.db')
	for tr in trs:
		tds = tr.select('td')
		ip = tds[1].string
		port = tds[2].string
		sql = '''
		insert into proxy(ip, port) 
		select ?, ?
		where not exists (select 1 from proxy where ip=?); 
		'''
		conn.execute(sql, (ip, port, ip))
	conn.commit()	
	conn.close()


def get_proxy_2():
	url = 'http://www.kuaidaili.com/free/inha/1'
	ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
	request = urllib2.Request(url)
	request.add_header('User-Agent', ua)
	response = urllib2.urlopen(request)
	html = response.read()
	
	soup = BeautifulSoup(html)
	#table = soup.select('table')[1]
	print '------------------------------'
	print len(html)
	"""
	trs = table.select('tr')
	for tr in trs:
		tds = tr.select('td')
		ip = tds[1].string
		port = tds[2].string
		print ip, port
	"""


def check_proxy(proxy):
	print 'checking proxy:------------',proxy
	proxyfuck = urllib2.ProxyHandler({'http': proxy})
	opener=urllib2.build_opener(proxyfuck)        
	urllib2.install_opener(opener)  
	url = 'http://www.ip138.com/'
	ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.99 Safari/537.36'
	request = urllib2.Request(url)
	request.add_header('User-Agent', ua)
	try:
		print 'connecting...'
		content=urllib2.urlopen(url, timeout=5).read()
		return True
	except Exception, e:
		print e
		return False



if __name__ == "__main__":
	"""	
	url_template = 'http://www.xicidaili.com/nn/%d'
	url_template2 = 'http://www.xicidaili.com/wn/%d'

	conn = sqlite3.connect('fuck.db')
	
	conn.execute("delete from proxy;")
	conn.commit()
	conn.close()


	for i in range(1, 10):
		get_proxys_from_url(url_template%i)
		get_proxys_from_url(url_template2%i)
	"""
	get_proxy_2()