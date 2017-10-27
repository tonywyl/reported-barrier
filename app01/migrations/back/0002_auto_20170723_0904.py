# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-23 09:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='blog',
        ),
        migrations.RemoveField(
            model_name='article',
            name='category',
        ),
        migrations.RemoveField(
            model_name='article',
            name='tags',
        ),
        migrations.AlterUniqueTogether(
            name='article2tag',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='article2tag',
            name='article',
        ),
        migrations.RemoveField(
            model_name='article2tag',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='articledetail',
            name='article',
        ),
        migrations.RemoveField(
            model_name='blog',
            name='user',
        ),
        migrations.RemoveField(
            model_name='category',
            name='blog',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='article',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='reply',
        ),
        migrations.RemoveField(
            model_name='comment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='tag',
            name='blog',
        ),
        migrations.AlterUniqueTogether(
            name='updown',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='updown',
            name='article',
        ),
        migrations.RemoveField(
            model_name='updown',
            name='user',
        ),
        migrations.AlterUniqueTogether(
            name='userfans',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='userfans',
            name='follower',
        ),
        migrations.RemoveField(
            model_name='userfans',
            name='user',
        ),
        migrations.RemoveField(
            model_name='userinfo',
            name='fans',
        ),
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Article2Tag',
        ),
        migrations.DeleteModel(
            name='ArticleDetail',
        ),
        migrations.DeleteModel(
            name='Blog',
        ),
        migrations.DeleteModel(
            name='Category',
        ),
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.DeleteModel(
            name='Tag',
        ),
        migrations.DeleteModel(
            name='UpDown',
        ),
        migrations.DeleteModel(
            name='UserFans',
        ),
        migrations.DeleteModel(
            name='UserInfo',
        ),
    ]
