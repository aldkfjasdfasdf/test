# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils import timezone
from django.shortcuts import render
from django.http import JsonResponse

from .models import EmailOpen
from .forms import EmailForm

def create_email(request):
    if request.method == 'POST' and request.is_ajax():
        form = EmailForm(request.POST)
        if form.is_valid():
            email = form.save(commit=False)
            schedule_delay = int(form.cleaned_data['schedule_delay'])
            email.schedule_time = timezone.now() + timezone.timedelta(minutes=schedule_delay)
            email.save()
            
            subscribers = form.cleaned_data['subscribers']
            email.subscribers.set(subscribers)
            return JsonResponse(
                {
                    'success': True
                }
            )
        else:
            return JsonResponse(
                {
                    'success': False
                }
            )
    else:
        context = {
            'form': EmailForm()
        }
        return render(request, 'create_email.html', context)


def tracking_pixel_view(request, tracking_pixel_id):
    try:
        email_opened = EmailOpen.objects.get(tracking_pixel_id=tracking_pixel_id)
        email_opened.opened = True
        email_opened.opened_at = timezone.now()
        email_opened.save()
    except EmailOpen.DoesNotExist:
        pass
