# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-03 01:17
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_remove_product_rating'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.CharField(default='', max_length=1000),
            preserve_default=False,
        ),
    ]
