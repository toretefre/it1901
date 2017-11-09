# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-11-09 11:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0017_auto_20171031_0959'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='band',
            options={'verbose_name_plural': 'Band'},
        ),
        migrations.AlterModelOptions(
            name='bestilling',
            options={'verbose_name_plural': 'Bestillinger'},
        ),
        migrations.AlterModelOptions(
            name='konserter',
            options={'verbose_name_plural': 'Konserter'},
        ),
        migrations.AlterModelOptions(
            name='tekniske_behov',
            options={'verbose_name_plural': 'Tekniske behov'},
        ),
        migrations.AddField(
            model_name='band',
            name='kontakt_info',
            field=models.TextField(default='00000000'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='band',
            name='previous_concerts',
            field=models.TextField(default='Ingen'),
        ),
        migrations.AlterField(
            model_name='band',
            name='sjanger',
            field=models.CharField(default='undefined', max_length=100),
        ),
        migrations.AlterField(
            model_name='bestilling',
            name='pris',
            field=models.PositiveIntegerField(),
        ),
        migrations.AlterField(
            model_name='konserter',
            name='publikumsantall',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='konserter',
            name='solgtebilletter',
            field=models.PositiveIntegerField(blank=True, default=0, null=True),
        ),
    ]
