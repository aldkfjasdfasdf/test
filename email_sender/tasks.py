# -*- coding: utf-8 -*-
from smtplib import SMTPDataError
from celery.task import task
from django.utils import timezone
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings

from .models import Email, EmailOpen

@task
def send_emails():
    emails = Email.objects.filter(sent=False)

    for email in emails:
        if email.schedule_time and timezone.now() < email.schedule_time:
            continue

        subscribers = email.subscribers.all()
        email_recipients = [subscriber.email for subscriber in subscribers]

        for subscriber in subscribers:
            try:
                email_open = EmailOpen.objects.create(
                    email=email,
                    subscriber=subscriber,
                )

                context = {
                    'subject': email.subject,
                    'body': email.body,
                    'subscriber': subscriber,
                    'email_open': email_open,
                }

                content = render_to_string('email/email_template.html', context)

                email_message = EmailMultiAlternatives(
                    subject=email.subject,
                    body='',  # Пустое тело, так как контент в виде HTML будет задан через `attach_alternative`
                    from_email=settings.DEFAULT_FROM_EMAIL,
                    to=[subscriber.email]
                )
                email_message.attach_alternative(content, "text/html")
                
                email_message.send()
                email.sent = True  # Обновляем поле sent только после успешной отправки
                email.save()
                        
            except SMTPDataError as e:
                print(e)
                continue
