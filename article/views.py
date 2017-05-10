# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.db import models
from models import Person
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
	

