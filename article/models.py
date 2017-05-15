# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class PersonManager(models.Manager):
	"""docstring for PersonManager"""
	def create_person(self, name,num):
		person = self.create(name=name,num=num)
		return person


class Person(models.Model):
	name = models.CharField(max_length=30)
	num = models.CharField(max_length=20)

	objects = PersonManager()


