# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
from tinymce.models import HTMLField

# Create your models here.
class Resident(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    phone_number = models.CharField(max_length =10, blank =True)
    resident_image = models.ImageField(upload_to = 'residents/', blank =True)

    def __str__(self):
        return self.first_name

    def save_resident(self):
        self.save()

    class Meta:
        ordering = ['first_name']

class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Business(models.Model):
    title = models.CharField(max_length =40)
    selling = models.CharField(max_length =60)
    post = HTMLField
    resident = models.ForeignKey(User,on_delete=models.CASCADE)
    tags = models.ManyToManyField(tags)  
    business_image = models.ImageField(upload_to = 'businesses/', blank =True)  
