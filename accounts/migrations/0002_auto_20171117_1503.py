# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-17 15:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='image',
            field=models.ImageField(blank=True, default='avatars/images.png', null=True, upload_to='avatars'),
        ),
    ]