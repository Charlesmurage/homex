# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-10 09:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeground', '0002_remove_business_selling'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='selling',
            field=models.CharField(default='shoes', max_length=60),
        ),
    ]