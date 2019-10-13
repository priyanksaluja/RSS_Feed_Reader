# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-12 16:47
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('googlenews', '0005_auto_20191010_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed',
            name='published_date',
            field=models.DateTimeField(max_length=150),
        ),
        migrations.AlterField(
            model_name='feed_details',
            name='last_updated',
            field=models.CharField(default=datetime.datetime(2019, 10, 12, 16, 47, 6, 722955), max_length=150),
        ),
    ]
