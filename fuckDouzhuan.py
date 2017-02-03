import urllib
import urllib2 
import random
import threading
import time
import cookielib
import sqlite3



url = "http://www.ycoho.com/95b5c197-e100-4ccc-b17a-72d31c08f066205527/1481430332/read.do"
#use_proxy = True


#download page html
def get_html_from_url(url, proxy_str=None, referer_str=None):
	ua = 'Mozilla/5.0 (Linux; Android 4.4.2; HM NOTE 1TD Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile MQQBrowser/6.8 TBS/036887 Safari/537.36 MicroMessenger/6.3.31.940 NetType/WIFI Language/zh_CN'
	if proxy_str:

		proxy = urllib2.ProxyHandler({'http': proxy_str})
		#proxy_opener = urllib2.build_opener(proxy)
		#urllib2.install_opener(proxy_opener)
	#ua about
	request = urllib2.Request(url)
	request.add_header('User-agent', ua)
	if referer_str:
		request.add_header('Referer', referer_str)
	#cookie about
	cookie_file_name = 'cookie.txt'
	cookie = cookielib.MozillaCookieJar(cookie_file_name)
	cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
	handler=urllib2.HTTPCookieProcessor(cookie)
	if proxy_str:
		cookie_opener = urllib2.build_opener(proxy, handler)
	else:
		cookie_opener = urllib2.build_opener(handler)

	try:
		#print 'getting html from url:'
		#print 'url: '+url
		#if proxy_str:
			#print 'proxy: '+proxy_str
		#if referer_str:
			#print 'referer: '+referer_str
		response = cookie_opener.open(request, timeout=10)
		html = response.read()
		#print 'got-----------------------------------------------------'
		cookie.save(ignore_discard=True, ignore_expires=True)
		return html
	except Exception, e:
		print e
	


		


def ajax_html(url,data,referer=None):
	ua = 'Mozilla/5.0 (Linux; Android 4.4.2; HM NOTE 1TD Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile MQQBrowser/6.8 TBS/036887 Safari/537.36 MicroMessenger/6.3.31.940 NetType/WIFI Language/zh_CN'
	req = urllib2.Request(url)
	req.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
	req.add_header('X-Requested-With','XMLHttpRequest')
	req.add_header('User-Agent',ua)
	if referer:
		req.add_header('Referer',referer)
	params = urllib.urlencode(data)
	response = urllib2.urlopen(req, params)
	jsonText = response.read()
	return json.loads(jsonText)

#for parse index url
def find_from_html(html, str):
	start_pos = html.find(str)
	length = html[start_pos:].find('\n')
	line_str = html[start_pos:start_pos+length]
	return line_str.split('"')[1]


def fuck(index, proxy):
	print 'fucking index %s with proxy %s!!!!!!!!!'%(index, proxy)
	html = get_html_from_url(index, proxy)
	#####
	domainur1 = find_from_html(html, 'var domainur1=')
	shareID = find_from_html(html, 'shareID')
	rs = find_from_html(html, 'rs = "')
	domain = 'www.xiangtudai.com'

	cnzz_article_url = domainur1 + "/webarticle/cnzz_article.action?shareID="+shareID
	cnzz_article_html = get_html_from_url(cnzz_article_url, proxy)

	query_article_url = domainur1+'/webarticle/qureyArticle.action?'\
		+'shareID='+shareID+'&jsonpCallback=displayArticle&domainur1='+domain
	query_article_html = get_html_from_url(query_article_url, proxy)	

	indexcode = query_article_html.split('"')[-2]

	time.sleep(2)
	count_article_url = domainur1+"/weixin20/readarticle/dzcotunArticlew.action?"\
		+'shareID='+shareID+'&rs='+rs+'&indexcode='+indexcode+'&jsonpCallback=countArticleSuccess'
	count_article_html = get_html_from_url(count_article_url, proxy)

def fuck2(index, proxy=None):
	print '----------------------------------------------------------'
	print 'fuck2ing index %s with proxy %s'%(index, proxy)
	try:
		html = get_html_from_url(index, proxy_str=proxy)
		#####
		domainur1 = find_from_html(html, 'var domainur1="')
		sharekey = find_from_html(html, 'sharekey="')
		rs = find_from_html(html, 'rs = "')
		domain = 'www.xiaohanbz.com'


		cnzz_article_url = domainur1 + "/webarticle/cnzz_article.action?shareID="+sharekey
		cnzz_article_html = get_html_from_url(cnzz_article_url, proxy_str=proxy, referer_str=index)

		query_article_url = domainur1+'/webarticle/qureyNewArticle.action?'\
			+'sharekey='+sharekey+'&jsonpCallback=displayArticle&domainur1='+domain
		query_article_html = get_html_from_url(query_article_url, proxy_str=proxy, referer_str=index)

		indexcode = query_article_html.split('"')[-2]

		time.sleep(2)
		count_article_url = domainur1+"/weixin20/readarticle/dzcotunArticlew11.action?"\
			+'sharekey='+sharekey+'&rs='+rs+'&indexcode='+indexcode+'&jsonpCallback=countArticleSuccess'
		count_article_html = get_html_from_url(count_article_url, proxy_str=proxy, referer_str=index)
		print 'success!!!!!'
	except Exception, e:
		print e


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
	index = 'http://www.xiaohanbz.com/scpe/S8/1481543368/b2427ad8c2634b099a33e9a35c3ca960207608207608/oJU/GNCM4ZR/M33HnCEWWS/ar32C'

	"""
	conn = sqlite3.connect('fuck.db')
	
	cursor = conn.execute("select ip, port from proxy;")
	for row in cursor:
	   pxy_str = row[0]+':'+row[1]
	   fuck2(index, pxy_str)

	conn.close()
	"""

	fuck2(index, '121.232.147.86:9000')
