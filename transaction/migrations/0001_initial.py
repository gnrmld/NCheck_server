# -*- coding: utf-8 -*-
# Generated by Django 1.9.9 on 2016-09-02 18:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '__first__'),
        ('shopper', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('total_price', models.IntegerField()),
                ('payment_id', models.CharField(max_length=100)),
                ('is_valid', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='TransactionDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='transaction.Transaction')),
            ],
        ),
        migrations.AddField(
            model_name='transaction',
            name='product',
            field=models.ManyToManyField(related_name='product', through='transaction.TransactionDetails', to='product.Product'),
        ),
        migrations.AddField(
            model_name='transaction',
            name='shopper',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction', to='shopper.Shopper'),
        ),
    ]
