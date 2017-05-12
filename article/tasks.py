from __future__ import absolute_import
from .HousePriceSpider import SouFangSpider
import logging
from celery import task
from celery.utils.log import get_task_logger
from celery.schedules import crontab


@task
def HouseSpider(x, y):
    print 'begin'
    SouFangSpider.getHouseInfo()
    pass


@task
def test_celery(x, y):
    
    
    return x + y


@task
def test_multiply(x, y):
    
    print 88
    return x * y