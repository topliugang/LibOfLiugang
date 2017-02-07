 # -*- coding:utf-8 -*- 

import requests
from bs4 import BeautifulSoup
import json

#修改python的defaultcoding至utf-8来解决写入unicode到文件的报错
import sys
reload(sys)                         
sys.setdefaultencoding('utf-8')    

base_url = 'http://www.che168.com'
main_list_url = 'http://www.che168.com/china/list/'
car_make_list_url = 'http://www.che168.com/handler/usedcarlistv5.ashx?action=brandlist&area=china&brand=&ls=&spec=&minPrice=0&maxPrice=0&minRegisteAge=0&maxRegisteAge=0&MileageId=0&disp=&stru=&gb=0&color=&source=0&listview=0&sell=1&newCar=0&credit=0&sort=0&page=1&ex=cd0t0p0w0ru0e0sa1o0i0g0nfzlk0v0a0b0m0_0y0x0h'

#返回一个json字符串
#return [{'name':name, 'url':url}]
def get_car_make_list():
	r = requests.get(car_make_list_url)
	car_make_list = []
	for car_make in json.loads(r.text):
		#car_make_id = car_make['id']
		#car_make_letter = car_make['letters']
		name = car_make['name']
		#car_make_pinyin = car_make['pinyin']
		#seriesurl = car_make['seriesurl']
		url = car_make['url']
		car_make_list.append({'name':name, 'url':url})
	return car_make_list

#从页面抓取model list
#return [{'name':car_model_name, 'url':car_model_url, 'type':car_type_name}]
def get_car_model_list(car_make_name, car_make_url):
	r = requests.get(car_make_url)
	soup = BeautifulSoup(r.text, 'html.parser')
	car_type_block_tag = soup.find('div', class_='condition-list fn-clear fn-hide', id='series')
	car_model_list = []
	if car_type_block_tag:
		car_types_tag = car_type_block_tag.find_all('dl', class_='model-list fn-clear')
		for car_type_tag in car_types_tag:
			car_type_name = car_type_tag.find('dt').text
			for car_model_tag in car_type_tag.find_all('a'):
				car_model_url = car_model_tag['href']
				car_model_name = car_model_tag.text
				car_model_list.append({'name':car_model_name, 'url':car_model_url, 'type':car_type_name})
	return car_model_list
	

def main():
	for car_make in get_car_make_list():
		car_make_name = car_make['name']
		car_make_sub_url = car_make['url']
		car_make_url = base_url+car_make_sub_url
		for car_model in get_car_model_list(car_make_name, car_make_url):
			print car_model['name']
			print car_model['url']
			print car_model['type']
			print'----------'
			print


def fuck(url):
	r = requests.get(url)
	print r.text
	soup = BeautifulSoup(r.text, 'html.parser')
	print soup.find_all('a', _class='page-item-next')



if __name__ == '__main__':
	main()



