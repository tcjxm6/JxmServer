# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from models import Person
from HousePriceSpider.Model import RealEstateModels
import json
from django.views.decorators.csrf import csrf_exempt
import time
import datetime 
from django.core import serializers

# from . import models
	

def hello(request):
	

	person = Person.objects.create_person("jxm","1020410202")
	person.save()

	li = Person.objects.all()
	
	# person = Person(name="jxm",num=("1020410202"))

	return HttpResponse(str(li))


def allPerson(request):

	li = Person.objects.all()
	str1 = ''
	arr = []
	for person in li:
		arr.append(person.name)  

	
		
	# rd = render(request, 'first.html', {}, content_type='text/html; charset=utf-8')

	return HttpResponse(json.dumps(arr),content_type='application/json')


@csrf_exempt
def saveRealEstate(request):

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
	model = RealEstateModels.RealEstate.objects.create_realEstate(province_name, city_name, regionalism_name, address, house_name, avg_price, house_type, house_rent, house_href, source)
	
	print request.body
	# model.save()
	
	dic = {}
	dic['house_name'] = model.house_name
	return HttpResponse(json.dumps(dic),content_type='application/json')




# beginTime:
# endTime:
# size:
# page:
#
@csrf_exempt
def queryTop100(request):

	print type(request.body) 
	jsDic = None
	dic = {}
   	try:
   		jsDic = json.loads(request.body, encoding='utf-8')
   	except Exception as e:
   		print Exception
	
	if jsDic == None:
		dic['success'] = False
		dic['msg'] = '解析JSON失败'
		return HttpResponse(json.dumps(dic),content_type='application/json')
		pass


	print jsDic

	try:
		beginTimeStr = jsDic['beginTime']
		endTimeStr = jsDic['endTime']
		size = jsDic['size']
		page = jsDic['page']
		
		pass
	except Exception as e:
		print Exception
		dic['success'] = False
		dic['msg'] = '提交参数缺失'
		return HttpResponse(json.dumps(dic),content_type='application/json')

	city = jsDic.get('city',None)


	sortBy = dic.get('sort','regionalism_name')



	if sortBy == 'price':
		sortBy = 'avg_price'
		pass
	else :
		sortBy = 'regionalism_name'
		pass
		

	
	beginTime = datetime.datetime.strptime(beginTimeStr,"%Y-%m-%d %H:%M:%S") 
	endTime = datetime.datetime.strptime(endTimeStr,"%Y-%m-%d %H:%M:%S") 

	models = models = RealEstateModels.RealEstate.objects.filter(date__range=(beginTime, endTime)).order_by('regionalism_name')
	if city != None:
		models = models.filter(city_name=city).order_by('regionalism_name')
		pass
	

#[(page-1)*size : size * page]
	houseNameArr = []
	dataDic = {}

	for x in xrange(0,len(models)):
		model = models[x]


		modelDic = dataDic.get(model.house_name,{})

		if modelDic :
			pass
		else :
			modelDic['province_name'] = model.province_name
			modelDic['city_name'] = model.city_name
			modelDic['regionalism_name'] = model.regionalism_name
			modelDic['address'] = model.address
			modelDic['house_name'] = model.house_name
			modelDic['house_type'] = model.house_type
			modelDic['house_rent'] = model.house_rent
			modelDic['house_href'] = model.house_href
			modelDic['source'] = model.source
			modelDic['source2'] = None
			houseNameArr.append(model.house_name)
			pass
		
		prices = modelDic.get('avg_prices',{})
		prices[model.date.strftime('%Y-%m-%d %H:%M:%S')] = float(model.avg_price)
		modelDic['avg_prices'] = prices
		# modelDic['avg_price'] = float(model.avg_price)
		# modelDic['date'] = model.date.strftime('%Y-%m-%d %H:%M:%S');
		
		dataDic[model.house_name] = modelDic
		pass

	responseData = []
	for x in xrange((page-1)*size,size * page):
		if x >= len(houseNameArr) or x < 0:
			break
			pass
		responseData.append(dataDic[houseNameArr[x]])
		pass

	dic['success'] = True
	dic['data'] = responseData
	return HttpResponse(json.dumps(dic,encoding="UTF-8",ensure_ascii=False),content_type='application/json')
	pass

