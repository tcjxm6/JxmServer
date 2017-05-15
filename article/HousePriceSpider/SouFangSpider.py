# -*- coding=UTF-8 -*-
from bs4 import BeautifulSoup
import requests
from .Model import RealEstateModels 


Top_100 = 'Top100'


def getHouseInfo():

	for x in xrange(1,10):
		url = 'http://newhouse.sz.fang.com/house/web/newhouse_sumall.php?page=' + str(x)
		response = requests.get(url)
		response.encoding = 'gb18030'
		html = response.text
		if response.status_code:
			analyzingResponse(html,Top_100)
			pass
		pass
	
	

	pass

	


	 
def analyzingResponse(html,type):

	if type == Top_100:
		analyzingTop100(html)
		pass
	

	pass

def analyzingTop100(html):

	soup = BeautifulSoup(html, "lxml")
	listAreaArr = soup.find_all(class_="listArea")
	listArea = listAreaArr[0]
	clearfix = listArea.ul
	liArr = clearfix.find_all('li')

	for child in liArr:

		province_name = '广东省'
		city_name = '深圳市'
		regionalism_name = '未知区'
		address = '未知'
		house_name = '未知'
		avg_price = 0.0
		house_type = '未知'
		house_rent = '未知'
		house_href = ''
		source = 'www.fang.com'

		houses = child.find_all(class_ = 'floatl')
		house = None
		if len(houses) > 0:
			house = houses[0]
			pass
		houseName = house.string
		house_name = navToString(houseName)
		if len(house_name) > 0:
			
			prices = child.find_all(class_ = 'price')
			if len(prices) > 0:
				priceVal = prices[0].span.string
				unicode_string = unicode(priceVal)
				priceStr = unicode_string.encode("utf-8")
				pass
			

			# safe_float(priceStr)
			if priceStr.isdigit():
				avg_price = float(priceStr)
				pass
			

			archiveData(province_name, city_name, regionalism_name, address, house_name, avg_price, house_type, house_rent, house_href, source)
			des = unicode(houseName).encode("utf-8")
			print '保存成功:' + des

			pass
		
		else:
			print house_name + '-保存失败'
		pass
	pass



def navToString(navVal):
	return unicode(navVal).encode("utf-8")
	pass

def archiveData(province_name,
				city_name,
				regionalism_name,
				address,house_name,
				avg_price,
				house_type,
				house_rent,
				house_href,
				source,
				):
	model = RealEstateModels.RealEstate.objects.create_realEstate(province_name, city_name, regionalism_name, address, house_name, avg_price, house_type, house_rent, house_href, source)
	model.save()
	pass




