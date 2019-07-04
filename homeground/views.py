# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import Business
from django.contrib.auth.decorators import login_required
from .forms import NewBusinessForm


def welcome(request):
    business = Business.objects.all()
    return render(request,'home.html',{"business": business})

@login_required(login_url='/accounts/login/')
def new_business(request):
    current_user = request.current_user
    if request.method =='POST':
        form = NewBusinessForm(request.POST, request.FILES)

        if form.is_valid():
            business = form.save(commit=False)
            business.resident = current_user
            business.save()
        return redirect('welcome')


    else:
        form = NewBusinessForm()
    return render(request, 'new_business.html', {"form":form})
    
