# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-06-29 20:13
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checkout', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='street_address1',
            new_name='street_address_line_1',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='street_address2',
            new_name='street_address_line_2',
        ),
    ]
