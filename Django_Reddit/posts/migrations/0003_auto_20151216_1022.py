# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-16 10:22
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0002_post_post_header'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='post_header',
            field=models.CharField(default='First Post', max_length=200),
        ),
    ]
