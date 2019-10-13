# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from datetime import datetime


class Feed(models.Model):
    title = models.CharField(max_length=300, null=False, blank=False)
    link = models.CharField(max_length=300, null=False, blank=False)
    published_date = models.DateTimeField (max_length=150, null=False, blank=False)
    source = models.CharField(max_length=100, null=False, blank=False)

    def __str__(self):
        return self.title


class Feed_details(models.Model):
    feed_url = models.CharField(max_length=300, null=False, blank=False)
    feed_source = models.CharField(max_length=100, null=False, blank=False)
    last_updated = models.CharField(max_length=150, default=datetime.now())
    message = models.CharField(max_length=300, null=False, blank=False, default='Dummy message')
    status = models.CharField(max_length=10, null=False, blank=False)