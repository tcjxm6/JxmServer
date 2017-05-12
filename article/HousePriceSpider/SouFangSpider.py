# -*- coding=UTF-8 -*-
from bs4 import BeautifulSoup
import requests


def getHouseInfo():
	response = requests.get('http://newhouse.sz.fang.com/house/web/newhouse_sumall.php?page=2')
	response.encoding = 'gb18030'
	html = response.text


	soup = BeautifulSoup(html, "lxml")
	listAreaArr = soup.find_all(class_="listArea")
	listArea = listAreaArr[0]
	clearfix = listArea.ul
	liArr = clearfix.find_all('li')
	for child in liArr:
		houses = child.find_all(class_ = 'floatl')
		house = None
		if houses.count > 0:
			house = houses[0]
			pass
		houseName = house.string
		print houseName
		# print unicode(houseName).encode('UTF-8')
		prices = child.find_all(class_ = 'price')
		priceVal = prices[0].span.string
		print priceVal
		pass


	 







