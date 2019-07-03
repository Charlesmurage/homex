# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Resident(models.Model):
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)

    def __str__(self):
        return self.first_name

    class Meta:
        ordering = ['first_name']

class tags(models.Model):
    name = models.CharField(max_length =30)

    def __str__(self):
        return self.name

class Business(models.Model):
    title = models.CharField(max_length =40)
    selling = models.CharField(max_length =60)
    resident = models.ForeignKey(Resident)
    tags = models.ManyToManyField(tags)    
