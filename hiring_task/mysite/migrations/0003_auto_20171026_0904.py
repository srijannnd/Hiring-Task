# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 09:04
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0002_auto_20171026_0901'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Orders',
            new_name='Order',
        ),
    ]
