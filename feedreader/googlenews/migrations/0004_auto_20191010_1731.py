# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-10-10 12:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('googlenews', '0003_auto_20191010_1610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feed_details',
            name='last_updated',
            field=models.CharField(max_length=150),
        ),
    ]