# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-16 08:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0002_realestate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='realestate',
            name='date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
