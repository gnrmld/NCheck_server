# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-02 13:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='is_validated',
        ),
        migrations.AddField(
            model_name='transaction',
            name='is_valid',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='product',
            field=models.ManyToManyField(related_name='product', to='product.Product'),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='shopper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction', to='shopper.Shopper'),
        ),
    ]
