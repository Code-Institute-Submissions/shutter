# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-05 16:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0008_product_port_or_land'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='author',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='product',
            name='photo_type',
            field=models.CharField(choices=[('Lifestyle', 'Lifestyle'), ('Product', 'Product'), ('Nature', 'Nature')], default='Lifestyle', max_length=100),
        ),
    ]