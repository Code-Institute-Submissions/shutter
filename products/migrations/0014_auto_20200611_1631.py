# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-11 16:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0013_auto_20200611_1630'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'ordering': ['photo_type']},
        ),
    ]