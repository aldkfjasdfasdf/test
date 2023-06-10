# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import (
    Subscriber,
    Email,
    EmailOpen
)


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    pass


@admin.register(Email)
class EmailAdmin(admin.ModelAdmin):
    list_display = ('subject', 'sent')


@admin.register(EmailOpen)
class EmailOpenAdmin(admin.ModelAdmin):
    list_display = ('email', 'opened', 'opened_at')