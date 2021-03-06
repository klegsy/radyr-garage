# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-09 10:08
from __future__ import unicode_literals

from decimal import Decimal
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=30)),
                ('last_name', models.CharField(default='', max_length=30)),
                ('email', models.EmailField(default='', max_length=254)),
                ('telephone', models.CharField(default='', max_length=11)),
                ('house_num', models.CharField(max_length=3, null=True)),
                ('street_name', models.CharField(max_length=35, null=True)),
                ('city', models.CharField(max_length=20, null=True)),
                ('postcode', models.CharField(max_length=9, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30)),
                ('last_name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=254)),
                ('telephone', models.CharField(max_length=11)),
                ('employee', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('labour_time', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=5)),
                ('total_price', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
                ('issue_date', models.DateField(null=True)),
                ('due_date', models.DateField(null=True)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.Customer')),
            ],
        ),
        migrations.CreateModel(
            name='Parts',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('part_name', models.CharField(max_length=15)),
                ('part_price', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=5)),
                ('quantity', models.PositiveSmallIntegerField(default=1)),
            ],
        ),
        migrations.CreateModel(
            name='Tyres',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manufacture', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=30)),
                ('size', models.CharField(max_length=10)),
                ('energy_rating', models.CharField(max_length=2)),
                ('no_in_stock', models.PositiveSmallIntegerField()),
                ('price', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=5)),
            ],
        ),
        migrations.CreateModel(
            name='Vehicle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registration', models.CharField(max_length=7)),
                ('manufacture', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=30)),
                ('MOT_date', models.DateField()),
                ('service_date', models.DateField()),
                ('mileage', models.PositiveIntegerField()),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='system.Customer')),
                ('tyre_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.Tyres')),
            ],
        ),
        migrations.AddField(
            model_name='invoice',
            name='parts',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='system.Parts'),
        ),
    ]
