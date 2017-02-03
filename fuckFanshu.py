import mylib
	

if __name__ == "__main__":
	url = 'http://m.trqyjt.com/detail.html?aid=1226304&uid=1041850&r=35MRH7'	
	url2 = 'http://qfen.bombadd.com/html/sdk/uid/1041850/aid/1226304/domain/m.trqyjt.com?url=http%3A%2F%2Fm.trqyjt.com%2Fdetail.html%3Faid%3D1226304%26uid%3D1041850%26r%3D35MRH7'
	url3 = 'http://kitty.gan-xing.com/wall/alist/vid/1041850/aid/1226304'
	url4 = 'http://qfen.bombadd.com/html/jjcontent/aid/1226304/uid/1041850?callback=success_jsonpCallback'

	proxy_str = '218.247.161.37:80'
	#get_html_from_url(url, proxy_str = proxy_str)
	#get_html_from_url(url2)
	#get_html_from_url(url3)
	#get_html_from_url(url4)
	mylib.get_html_from_url(url)