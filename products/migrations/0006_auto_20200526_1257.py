# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-05-26 12:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0005_product_prdouct_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='prdouct_id',
            field=models.CharField(default='shutter#', max_length=20),
        ),
    ]
