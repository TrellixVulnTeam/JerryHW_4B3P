# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-04-16 11:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jack', '0002_auto_20180416_1058'),
    ]

    operations = [
        migrations.CreateModel(
            name='Introduction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('phone_number', models.CharField(max_length=10)),
                ('birthday', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=15)),
            ],
        ),
        migrations.RemoveField(
            model_name='food',
            name='restaurant',
        ),
        migrations.DeleteModel(
            name='Food',
        ),
        migrations.DeleteModel(
            name='Restaurant',
        ),
    ]
