import urllib2 
import cookielib
import gzip
import StringIO

#download page html
#proxy_str: '127.0.0.1:8888'
#user-agent is for mobile phone
def get_html_from_url(url, proxy_str=None, referer_str=None, timeout = 10):
	print '----------------------------------------'
	print 'getting html from url:%s'%url
	ua = 'Mozilla/5.0 (Linux; Android 4.4.2; HM NOTE 1TD Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile MQQBrowser/6.8 TBS/036887 Safari/537.36 MicroMessenger/6.3.31.940 NetType/WIFI Language/zh_CN'
	ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
	request = urllib2.Request(url)
	request.add_header('User-agent', ua)
	if referer_str:
		request.add_header('Referer', referer_str)
	#cookie about
	cookie_file_name = 'cookie.txt'
	cookie = cookielib.MozillaCookieJar(cookie_file_name)
	cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
	cookie_handler=urllib2.HTTPCookieProcessor(cookie)
	
	if proxy_str :
		proxy_handler = urllib2.ProxyHandler({'http': proxy_str})
		cookie_opener = urllib2.build_opener(proxy_handler, cookie_handler)
	else:
		cookie_opener = urllib2.build_opener(cookie_handler)
	try:
		response = None
		response = cookie_opener.open(request, timeout = timeout)
		html = response.read()
		#gzip decode
		headers = response.info()
		if ('Content-Encoding' in headers and headers['Content-Encoding']) or \
    		('content-encoding' in headers and headers['content-encoding']):
			data = StringIO.StringIO(html)
			gz = gzip.GzipFile(fileobj = data)
			html = gz.read()
	
		print 'got html, response code %d'%response.code
		print 
		cookie.save(ignore_discard=True, ignore_expires=True)
		return html
	except urllib2.URLError as e:
		if hasattr(e, 'code'):
			print 'Error code:',e.code
		elif hasattr(e, 'reason'):
			print 'Reason:',e.reason
	finally:
			if response:
				response.close()

def get_response_from_url(url, proxy_str=None, referer_str=None, timeout = 10):
	ua = 'Mozilla/5.0 (Linux; Android 4.4.2; HM NOTE 1TD Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile MQQBrowser/6.8 TBS/036887 Safari/537.36 MicroMessenger/6.3.31.940 NetType/WIFI Language/zh_CN'
	request = urllib2.Request(url)
	request.add_header('User-agent', ua)
	if referer_str:
		request.add_header('Referer', referer_str)
	#cookie about
	cookie_file_name = 'cookie.txt'
	cookie = cookielib.MozillaCookieJar(cookie_file_name)
	cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
	cookie_handler=urllib2.HTTPCookieProcessor(cookie)
	
	if proxy_str :
		proxy_handler = urllib2.ProxyHandler({'http': proxy_str})
		cookie_opener = urllib2.build_opener(proxy_handler, cookie_handler)
	else:
		cookie_opener = urllib2.build_opener(cookie_handler)

	try:
		response = cookie_opener.open(request, timeout = timeout)
		#html = response.read()
		print 'got  response, code %d'%response.code
		cookie.save(ignore_discard=True, ignore_expires=True)
		return response
	except urllib2.URLError as e:
		if hasattr(e, 'code'):
			print 'Error code:',e.code
		elif hasattr(e, 'reason'):
			print 'Reason:',e.reason
	#finally:
	#		if response:
	#			response.close()


if __name__ == '__main__':
	
	url = 'http://www.gatherproxy.com/zh/'
	proxys = dict()
	
	pxy = '127.0.0.1:8087'
	#pxy = None


	#'http': 'http://127.0.0.1:8087',
    #'https': 'http://127.0.0.1:8087',
	html = get_html_from_url(url, proxy_str=pxy, timeout=20)
	print html
	#print unicode(html, "gb2312").encode("utf8")