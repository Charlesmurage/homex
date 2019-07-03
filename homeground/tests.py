# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from .models import Resident,Business,tags

# Create your tests here.
class ResidentTestClass(TestCase):
    def setUp(self):
        self.charles= Resident(first_name = 'charles', last_name = 'maina')

    def test_instance(self):
        self.assertTrue(isinstance(self.charles,Resident))

    def test_save_method(self):
        self.charles.save_resident()
        resident = Resident.objects.all()
        self.assertTrue(len(resident) > 0)