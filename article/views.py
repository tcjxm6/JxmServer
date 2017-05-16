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
# province_name = models.CharField(max_length=20)
# 	#//市
# 	city_name = models.CharField(max_length=20)
# 	#//区
# 	regionalism_name = models.CharField(max_length=20)
# 	#//地址
# 	address = models.CharField(max_length=50)
# 	#//楼盘名称
# 	house_name = models.CharField(max_length=20)
# 	#//平均售价
# 	avg_price = models.DecimalField(max_digits=10,decimal_places=2)
# 	#//房产类型  普通住宅，商业
# 	house_type = models.CharField(max_length=20)
# 	#//可售平方范围
# 	house_rent = models.CharField(max_length=20)
# 	#//链接
# 	house_href = models.CharField(max_length=20)
# 	#//来源
# 	source = models.CharField(max_length=20)
# 	#//保存日期
# 	date 

	print jsDic
	beginTimeStr = jsDic['beginTime']
	endTimeStr = jsDic['endTime']
	size = jsDic['size']
	page = jsDic['page']
	beginTime = datetime.datetime.strptime(beginTimeStr,"%Y-%m-%d %H:%M:%S") 
	endTime = datetime.datetime.strptime(endTimeStr,"%Y-%m-%d %H:%M:%S") 

	models = RealEstateModels.RealEstate.objects.filter(date__range=(beginTime, endTime))[(page-1)*size : size * page]

	arr = []

	for x in xrange(0,len(models)):
		model = models[x]
		modelDic = {}
		modelDic['province_name'] = model.province_name
		modelDic['city_name'] = model.city_name
		modelDic['regionalism_name'] = model.regionalism_name
		modelDic['address'] = model.address
		modelDic['house_name'] = model.house_name
		modelDic['avg_price'] = float(model.avg_price)
		modelDic['house_type'] = model.house_type
		modelDic['house_rent'] = model.house_rent
		modelDic['house_href'] = model.house_href
		modelDic['source'] = model.source
		modelDic['date'] = model.date.strftime('%Y-%m-%d %H:%M:%S');
		arr.append(modelDic)
		print type(model.date)
		pass


	dic['success'] = True
	dic['data'] = arr
	return HttpResponse(json.dumps(dic,encoding="UTF-8",ensure_ascii=False),content_type='application/json')
	pass

