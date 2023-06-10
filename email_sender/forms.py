# -*- coding: utf-8 -*-
from django import forms
from .models import Subscriber, Email


class EmailForm(forms.ModelForm):
    subscribers = forms.ModelMultipleChoiceField(
        queryset=Subscriber.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=False
    )
    SCHEDULE_CHOICES = (
        (0, 'Без выбора'),
        (1, 'Через минуту'),
        (5, 'Через 5 минут'),
        (15, 'Через 15 минут'),
        (30, 'Через полчаса'),
        (60, 'Через час'),
        (120, 'Через 2 часа'),
        (1440, 'Через день'),
        (4320, 'Через 3 дня'),
    )
    schedule_delay = forms.ChoiceField(
        choices=SCHEDULE_CHOICES,
        required=False
    )

    class Meta:
        model = Email
        fields = ['subject', 'body', 'subscribers', 'schedule_delay']
