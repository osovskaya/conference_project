# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-08 12:25
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conference', '0004_blog_conference_message_speaker'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='author',
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
    ]
