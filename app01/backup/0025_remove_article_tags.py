# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-18 08:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0024_auto_20170718_0838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='tags',
        ),
    ]