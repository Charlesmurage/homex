# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Business

# Create your views here.
def welcome(request):
    business = Business.objects.all()
    return render(request,'home.html',{"business":business})
