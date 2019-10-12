# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .tasks import import_data
from .models import Feed


def index(request):
    try:
        posts = Feed.objects.all().order_by('-published_date')
        warning=False
    except:
        posts = ""
        warning = True

    context = {
        'posts': posts,
        'warning': warning
    }
    return render(request, 'googlenews/index.html', context)