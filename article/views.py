# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from models import Person
from HousePriceSpider.Model import RealEstateModels
import json


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
	

	model.save()
	
	dic = {}
	dic['house_name'] = model.house_name
	return HttpResponse(json.dumps(dic),content_type='application/json')
