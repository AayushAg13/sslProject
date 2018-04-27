# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-04-15 04:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_deptadmin_labs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Stud_Lab_Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lab_update_time', models.DateTimeField(blank=True, null=True)),
                ('lab_dues', models.BooleanField(default=False)),
                ('lab_remarks', models.CharField(blank=True, max_length=1000)),
                ('lab', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Labs')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Student')),
            ],
        ),
    ]
