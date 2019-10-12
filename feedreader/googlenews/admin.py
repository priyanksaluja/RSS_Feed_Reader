# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Feed_details, Feed

admin.site.register(Feed)
admin.site.register(Feed_details)