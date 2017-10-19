# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-17 08:37
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('webapp', '0007_auto_20171017_0848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='konserter',
            name='teknikere',
        ),
        migrations.AddField(
            model_name='konserter',
            name='teknikere',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
