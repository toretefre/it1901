# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-09-19 18:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Band',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('navn', models.CharField(max_length=200)),
                ('kostnad', models.IntegerField()),
                ('utstyr', models.TextField()),
                ('sjanger', models.CharField(max_length=100)),
                ('info', models.TextField()),
                ('rating', models.IntegerField()),
                ('manager', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Bestilling',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dato', models.DateTimeField(blank=True, null=True)),
                ('band', models.CharField(max_length=200)),
                ('scene', models.CharField(max_length=200)),
                ('godkjent', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Konserter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('scene', models.CharField(max_length=200)),
                ('teknikere', models.TextField()),
                ('konsert', models.CharField(max_length=200)),
                ('dato', models.DateTimeField(blank=True, null=True)),
                ('band', models.CharField(max_length=200)),
                ('festival', models.CharField(max_length=200)),
            ],
        ),
    ]
