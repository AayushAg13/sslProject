# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-14 06:11
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20180413_1829'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Finance',
            new_name='Account',
        ),
    ]
