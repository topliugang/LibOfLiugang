import urllib
import urllib2 
import cookielib
import gzip
import StringIO

#download page html
#proxy_str: '127.0.0.1:8888'
#user-agent is for mobile phone
def get_html_from_url(url, proxy_str=None, referer_str=None, timeout=10, weixin=True, https=False ):
	print '----------------------------------------'
	print 'getting html from url:%s'%url
	request = urllib2.Request(url)

	#setting user_agent
	if weixin:
		ua = 'Mozilla/5.0 (Linux; Android 4.4.2; HM NOTE 1TD Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile MQQBrowser/6.8 TBS/036887 Safari/537.36 MicroMessenger/6.3.31.940 NetType/WIFI Language/zh_CN'
	else:
		ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
	request.add_header('User-agent', ua)
	#setting referer
	if referer_str:
		request.add_header('Referer', referer_str)
	#other headers
	request.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
	request.add_header('Accept-Encoding', 'gzip,deflate,sdch')
	request.add_header('Accept-Language', 'en-US,en;q=0.8')
	request.add_header('Connection', 'keep-alive')
	#request.add_header('Content-Type', 'multipart/form-data')
	#setting cookie, save to cookie.txt, in the same folder
	cookie_file_name = 'cookie.txt'
	cookie = cookielib.MozillaCookieJar(cookie_file_name)
	cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
	cookie_handler=urllib2.HTTPCookieProcessor(cookie)
	#setting proxy
	if proxy_str:
		proxy_type = 'http'
		if https:
			proxy_type = 'https'
		proxy_handler = urllib2.ProxyHandler({proxy_type: proxy_str})
		cookie_opener = urllib2.build_opener(proxy_handler, cookie_handler)
	else:
		cookie_opener = urllib2.build_opener(cookie_handler)
	try:
		#getting response
		response = cookie_opener.open(request, timeout = timeout)
		html = response.read()
		#info = response.info()
		#gzip decode
		headers = response.info()
		if ('Content-Encoding' in headers and headers['Content-Encoding']) or \
    		('content-encoding' in headers and headers['content-encoding']):
			data = StringIO.StringIO(html)
			gz = gzip.GzipFile(fileobj = data)
			html = gz.read()
	
		print 'got html, response code %d'%response.code
		print 
		#saving cookie
		cookie.save(ignore_discard=True, ignore_expires=True)
		return html#, info
	except Exception, e:
		print e

def post_html_from_url(url, data=None, proxy_str=None, referer_str=None, timeout=10, weixin=True, https=False ):
	print '----------------------------------------'
	print 'getting html from url:%s'%url
	encodeddata = urllib.urlencode(data)
	request = urllib2.Request(url, encodeddata)

	#setting user_agent
	if weixin:
		ua = 'Mozilla/5.0 (Linux; Android 4.4.2; HM NOTE 1TD Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile MQQBrowser/6.8 TBS/036887 Safari/537.36 MicroMessenger/6.3.31.940 NetType/WIFI Language/zh_CN'
	else:
		ua = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36'
	request.add_header('User-agent', ua)
	#setting referer
	if referer_str:
		request.add_header('Referer', referer_str)
	#other headers
	request.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
	request.add_header('Accept-Encoding', 'gzip,deflate,sdch')
	request.add_header('Accept-Language', 'en-US,en;q=0.8')
	request.add_header('Connection', 'keep-alive')
	request.add_header('Content-Type', 'multipart/form-data')
	#setting cookie, save to cookie.txt, in the same folder
	cookie_file_name = 'cookie.txt'
	cookie = cookielib.MozillaCookieJar(cookie_file_name)
	cookie.load('cookie.txt', ignore_discard=True, ignore_expires=True)
	cookie_handler=urllib2.HTTPCookieProcessor(cookie)
	#setting proxy
	if proxy_str:
		proxy_type = 'http'
		if https:
			proxy_type = 'https'
		proxy_handler = urllib2.ProxyHandler({proxy_type: proxy_str})
		cookie_opener = urllib2.build_opener(proxy_handler, cookie_handler)
	else:
		cookie_opener = urllib2.build_opener(cookie_handler)
	try:
		#getting response
		response = cookie_opener.open(request, timeout = timeout)
		html = response.read()
		#info = response.info()
		#gzip decode
		headers = response.info()
		if ('Content-Encoding' in headers and headers['Content-Encoding']) or \
    		('content-encoding' in headers and headers['content-encoding']):
			data = StringIO.StringIO(html)
			gz = gzip.GzipFile(fileobj = data)
			html = gz.read()
	
		print 'got html, response code %d'%response.code
		print 
		#saving cookie
		cookie.save(ignore_discard=True, ignore_expires=True)
		return html#, info
	except Exception, e:
		print e


def check_url_avalible(url, proxy_str=None, referer_str=None, timeout = 10, weixin=False):
	ua_list = [
	'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat',
	'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:48.0) Gecko/20100101 Firefox/48.0',
	'Mozilla/5.0 (Linux; Android 4.4.2; HM NOTE 1TD Build/KOT49H) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/37.0.0.0 Mobile MQQBrowser/6.8 TBS/036887 Safari/537.36 MicroMessenger/6.3.31.940 NetType/WIFI Language/zh_CN',
	'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
	'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36 MicroMessenger/6.5.2.501 NetType/WIFI WindowsWechat QBCore/3.43.27.400 QQBrowser/9.0.2524.400'		
	]


if __name__ == '__main__':
	
	pxy = '127.0.0.1:58418'
	pxy = '61.161.140.171:8080'
	pxy = '123.134.24.181:8998'

	url = 'http://www.up01.cc/category/2/8'
	url = 'http://ip138.com/'

	print get_html_from_url(url, timeout=20, proxy_str=pxy)
