# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2019-07-10 12:08
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homeground', '0005_remove_comment_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='business',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='homeground.Business'),
        ),
    ]
