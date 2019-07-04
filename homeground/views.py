# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Business
from django.contrib.auth.decorators import login_required


def welcome(request):
    business = Business.objects.all()
    return render(request,'home.html',{"business": business})

@login_required(login_url='/accounts/login/')
def business(request, business_id):
    
    return render(request,'home.html')
