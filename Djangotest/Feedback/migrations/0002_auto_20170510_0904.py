# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-05-10 03:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Feedback', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='faculty',
            name='joining_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='faculty',
            name='relieved_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
