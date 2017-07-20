# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-20 05:10
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_attribute_node_record'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
