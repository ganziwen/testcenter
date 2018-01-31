# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-12-21 09:21
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apitest', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testcase',
            name='extract',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='suite_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='apitest.TestSuite'),
        ),
        migrations.AlterField(
            model_name='testcase',
            name='variables',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='testsuite',
            name='suite_name',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='testsuite',
            name='suite_request',
            field=models.CharField(blank=True, max_length=500),
        ),
        migrations.AlterField(
            model_name='testsuite',
            name='suite_variables',
            field=models.CharField(blank=True, max_length=500),
        ),
    ]