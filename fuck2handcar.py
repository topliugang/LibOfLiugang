import requests
from bs4 import BeautifulSoup
import json



def main():
	base_url = 'http://www.che168.com'
	main_list_url = 'http://www.che168.com/china/list/'
	brand_list_url = 'http://www.che168.com/handler/usedcarlistv5.ashx?action=brandlist&area=china&brand=&ls=&spec=&minPrice=0&maxPrice=0&minRegisteAge=0&maxRegisteAge=0&MileageId=0&disp=&stru=&gb=0&color=&source=0&listview=0&sell=1&newCar=0&credit=0&sort=0&page=1&ex=cd0t0p0w0ru0e0sa1o0i0g0nfzlk0v0a0b0m0_0y0x0h'

	r = requests.get(brand_list_url)
	# html_file = open('brand_list.html', 'w')
	# html_file.write(r.text)
	# html_file.close()
	# html = open('brand_list.html', 'r').read()
	brand_list_json_str = r.text
	brand_list_json_content = json.loads(brand_list_json_str)

	#brand_list_json_content is list
	for brand in brand_list_json_content:
		brand_id = brand['id']
		brand_letter = brand['letters']
		brand_name = brand['name']
		brand_pinyin = brand['pinyin']
		brand_seriesurl = brand['seriesurl']
		brand_url = brand['url']

		
		brand_full_url = base_url+brand_url
		r = requests.get(brand_full_url)


		brand_soup = BeautifulSoup(r.text, 'html.parser')
		chexi = brand_soup.find('div', class_='condition-list fn-clear fn-hide', id='series')
		chexings = chexi.find_all('dl', class_='model-list fn-clear')
		for chexing in chexings:
			chexing_class_name = chexing.find('dt').text
			print chexing_class_name
			for chexing_a in chexing.find_all('a'):
				chexing_url = chexing_a['href']
				chexing_name = chexing_a.text
				chexing_full_url = base_url+chexing_url
				print chexing_name
				print chexing_full_url

				r = requests.get(chexing_full_url)
				html_file = open('htmls/fuck%s.html'%chexing_name, 'w')
				html_file.write(r.text)
				html_file.close()


def fuck(url):
	r = requests.get(url)
	print r.text
	soup = BeautifulSoup(r.text, 'html.parser')
	print soup.find_all('a', _class='page-item-next')



if __name__ == '__main__':
	#main()
	fuck('http://www.che168.com/china/aodi/aodia4/#pvareaid=100512')


