# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-26 09:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mysite', '0004_auto_20171026_0909'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='per_product_price',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=20, null=True),
        ),
    ]
