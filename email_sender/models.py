# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models


class Subscriber(models.Model):
    email = models.EmailField(unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    birthday = models.DateField()

    def __str__(self):
        return self.email
    
    class Meta:
        verbose_name = 'Subscriber'
        verbose_name_plural = 'Subscribers'


class Email(models.Model):
    subject = models.CharField(max_length=200)
    body = models.TextField()
    subscribers = models.ManyToManyField(Subscriber, related_name='emails', blank=True, null=True)
    schedule_time = models.DateTimeField(blank=True, null=True)
    sent = models.BooleanField(default=False)

    class Meta:
            verbose_name = 'Email'
            verbose_name_plural = 'Emails'

    def __str__(self):
        return self.subject


class EmailOpen(models.Model):
    email = models.ForeignKey(Email, on_delete=models.CASCADE, related_name='opened_emails')
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE, related_name='opened_emails', blank=True, null=True)
    opened = models.BooleanField(default=False)
    opened_at = models.DateTimeField(blank=True, null=True)
    tracking_pixel_id = models.PositiveIntegerField(blank=True, null=True, unique=True)

    def __str__(self):
        return "{} - {} - {}".format(self.email, self.subscriber, self.opened_at)
    
    def save(self, *args, **kwargs):
        if not self.id:
            last_email = EmailOpen.objects.order_by('-tracking_pixel_id').first()
            self.tracking_pixel_id = 1 if last_email is None else last_email.tracking_pixel_id + 1

        super(EmailOpen, self).save(*args, **kwargs)