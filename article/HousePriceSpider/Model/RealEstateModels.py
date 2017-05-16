# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import time
# from datetime import timedelta
import datetime
# Create your models here.
class RealEstateManager(models.Manager):
	"""docstring for PersonManager"""
	def create_realEstate(self, province_name,
					city_name,
					regionalism_name,
					address,house_name,
					avg_price,
					house_type,
					house_rent,
					house_href,
					source,
					date):
		realEstate = self.create(province_name=province_name,
							city_name=city_name,
							regionalism_name=regionalism_name,
							address=address,house_name=house_name,
							avg_price=avg_price,
							house_type=house_type,
							house_rent=house_rent,
							house_href=house_href,
							source=source,
							date=date)

		return realEstate


class RealEstate(models.Model):

	#//省
	province_name = models.CharField(max_length=20)
	#//市
	city_name = models.CharField(max_length=20)
	#//区
	regionalism_name = models.CharField(max_length=20)
	#//地址
	address = models.CharField(max_length=50)
	#//楼盘名称
	house_name = models.CharField(max_length=20)
	#//平均售价
	avg_price = models.DecimalField(max_digits=10,decimal_places=2)
	#//房产类型  普通住宅，商业
	house_type = models.CharField(max_length=20)
	#//可售平方范围
	house_rent = models.CharField(max_length=20)
	#//链接
	house_href = models.CharField(max_length=20)
	#//来源
	source = models.CharField(max_length=20)
	#//保存日期
	date = models.DateTimeField(null=True,blank=True)


	objects = RealEstateManager()