# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2023-06-10 11:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('email_sender', '0011_emailopen_subscriber'),
    ]

    operations = [
        migrations.AlterField(
            model_name='email',
            name='tracking_pixel_id',
            field=models.PositiveIntegerField(blank=True, null=True, unique=True),
        ),
    ]
