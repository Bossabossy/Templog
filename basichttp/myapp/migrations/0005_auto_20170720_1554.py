# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-07-20 08:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0004_auto_20170720_1529'),
    ]

    operations = [
        migrations.AlterField(
            model_name='node',
            name='node_name',
            field=models.CharField(max_length=10, unique=True),
        ),
    ]