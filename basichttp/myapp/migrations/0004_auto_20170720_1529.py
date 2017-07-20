# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2017-07-20 08:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_room_time'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Room',
        ),
        migrations.AddField(
            model_name='record',
            name='attr',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='myapp.Attribute'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='attribute',
            name='attribute',
            field=models.CharField(max_length=5),
        ),
        migrations.AlterField(
            model_name='node',
            name='node_name',
            field=models.CharField(max_length=10),
        ),
    ]
