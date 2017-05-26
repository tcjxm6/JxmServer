# -*- coding=UTF-8 -*-
from bs4 import BeautifulSoup
import requests
from .Model import RealEstateModels 
import datetime
from django.utils import timezone
Top_100 = 'Top100'


def getHouseInfo():

	#深圳，长沙
	cityArr = ['cs','sz','gz','dg','huizhou','gy']
	cityName = ['长沙市','深圳市','广州市','东莞市','惠州市','贵阳市']
	for y in xrange(0,len(cityArr)):

		url = 'http://newhouse.'+cityArr[y]+'.fang.com/house/web/newhouse_sumall.php?page='
		
		for x in xrange(1,10):

			url2 = url + str(x)
			print '开始爬' + cityArr[y] + ':' + url2

			try:
				response = requests.get(url2,timeout=60)
				pass
			except Exception as e:
				print '获取超时'
				continue

			
			response.encoding = 'gb18030'
			html = response.text
			if response.status_code:
				analyzingResponse(html,Top_100,cityName[y])
				pass
			else :
				print '获取数据失败:' + url2
				pass
			pass
		pass
		print '爬' + cityName[y] + '结束'

	pass
	print '爬虫结束'

def houseSpider(url):

	for x in xrange(1,10):

		url = url + str(x)
		response = requests.get(url)
		response.encoding = 'gb18030'
		html = response.text
		if response.status_code:
			analyzingResponse(html,Top_100)
			pass
		pass

	pass


	 
def analyzingResponse(html,type,cityName):

	if type == Top_100:
		analyzingTop100(html,cityName)
		pass
	

	pass

def analyzingTop100(html,cityName):

	soup = BeautifulSoup(html, "lxml")
	listAreaArr = soup.find_all(class_="listArea")
	listArea = listAreaArr[0]
	clearfix = listArea.ul
	liArr = clearfix.find_all('li')

	for child in liArr:
		#解析每个节点
		analyzingTop100LiNode(child,cityName)
		pass
	pass


def analyzingTop100LiNode(child,cityName):
	province_name = '广东省'
	city_name = cityName
	regionalism_name = '未知区'
	address = '未知'
	house_name = '未知'
	avg_price = 0.0
	house_type = '未知'
	house_rent = '未知'
	house_href = ''
	source = 'www.fang.com'

	#获取楼盘名称
	houses = child.find_all(class_ = 'floatl')
	house = None
	if len(houses) > 0:
		house = houses[0]
		pass
	houseName = house.string
	house_name = navToString(houseName)

	#设置详情链接
	houseHref = house.get('href')
	if len(houseHref) > 0 and isinstance(houseHref,str):
		house_href = houseHref
		pass

	#设置区
	houseRegionalisms = child.find_all(class_ = 'floatr') 
	houseRegionalism = None
	if len(houseRegionalisms) > 0:
		houseRegionalism = houseRegionalisms[0]
		pass
	regionalismName = houseRegionalism.string
	regionalism_name = navToString(regionalismName)
	regionalism_name = regionalism_name.replace('[', '')
	regionalism_name = regionalism_name.replace(']', '')

	#设置地址
	addressNodes = child.find_all(class_ = 'address') 
	if len(addressNodes) > 0:
		addressNode = addressNodes[0]
		pass
	addressStr = addressNode.a.string
	address = navToString(addressStr)
	subEndIndex = address.find(']')
	if subEndIndex != -1:
		address = address[subEndIndex+1:]
		pass

	#设置住宅类型
	houseTypeNodes =  child.find_all(class_ = 'tag clearfix')
	if len(houseTypeNodes) > 0:
		houseTypes = houseTypeNodes[0]
		houseTypes = houseTypes.find_all('span')

		for x in xrange(0,len(houseTypes)):
			houseTypeNode = houseTypes[x]
			val = navToString(houseTypeNode.string)
			if val == '普通住宅':
				house_type = '住宅'
				pass
			elif val == '商业':
				house_type = '商业用房'
				pass
			pass
		pass
	
	if len(house_name) > 0:
		#获取楼盘价格
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
	# date = timezone.now();
	# django.util.timezone.now()
	date = datetime.datetime.now();
	model = RealEstateModels.RealEstate.objects.create_realEstate(province_name, city_name, regionalism_name, address, house_name, avg_price, house_type, house_rent, house_href, source,date)

	model.save()
	pass




