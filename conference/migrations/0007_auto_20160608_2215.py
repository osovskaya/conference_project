# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-08 19:15
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0006_auto_20160608_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='conference',
            name='user',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='company',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
