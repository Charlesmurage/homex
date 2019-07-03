# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Resident,Business,tags

# Register your models here.
admin.site.register(Resident)
admin.site.register(Business)
admin.site.register(tags)