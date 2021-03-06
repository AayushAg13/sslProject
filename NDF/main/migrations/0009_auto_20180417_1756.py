# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-17 17:56
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0008_auto_20180417_1755'),
    ]

    operations = [
        migrations.AlterField(
            model_name='labs',
            name='department',
            field=models.CharField(choices=[('BioSciences and Bioengineering', 'BioSciences and Bioengineering'), ('Chemistry', 'Chemistry'), ('Chemical Engineering', 'Chemical Engineering'), ('Civil Engineering', 'Civil Engineering'), ('Computer Science and Engineering', 'Computer Science and Engineering'), ('Design', 'Design'), ('Electronics and Electrical Engineering', 'Electronics and Electrical Engineering'), ('Electronics and Communication Engineering', 'Electronics and Communication Engineering'), ('Humanities & Social Sciences', 'Humanities & Social Sciences'), ('Mathematics', 'Mathematics'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Physics', 'Physics'), ('Center for Energy', 'Center for Energy')], max_length=250),
        ),
    ]
