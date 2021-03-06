# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-23 09:03
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usermanager', '0003_auto_20170723_0842'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='menu',
            name='parent',
        ),
        migrations.RemoveField(
            model_name='permission',
            name='menu',
        ),
        migrations.AlterUniqueTogether(
            name='permission2action2role',
            unique_together=set([]),
        ),
        migrations.RemoveField(
            model_name='permission2action2role',
            name='action',
        ),
        migrations.RemoveField(
            model_name='permission2action2role',
            name='permission',
        ),
        migrations.RemoveField(
            model_name='permission2action2role',
            name='role',
        ),
        migrations.RemoveField(
            model_name='user2role',
            name='role',
        ),
        migrations.RemoveField(
            model_name='user2role',
            name='user',
        ),
        migrations.DeleteModel(
            name='Action',
        ),
        migrations.DeleteModel(
            name='Menu',
        ),
        migrations.DeleteModel(
            name='Permission',
        ),
        migrations.DeleteModel(
            name='Permission2Action2Role',
        ),
        migrations.DeleteModel(
            name='Role',
        ),
        migrations.DeleteModel(
            name='User',
        ),
        migrations.DeleteModel(
            name='User2Role',
        ),
    ]
