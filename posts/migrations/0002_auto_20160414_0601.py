# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-14 06:01
from __future__ import unicode_literals

from django.db import migrations
import redactor.fields


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='body',
            field=redactor.fields.RedactorField(),
        ),
    ]
