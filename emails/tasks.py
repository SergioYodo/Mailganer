from __future__ import unicode_literals
import datetime
import pytz
from django.conf import settings
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from core.celery_app import app
from emails.models import TrackedEmail
from emails.utils import get_data_log, get_email_data


@app.task
def send_email():
    data = get_email_data()
    rendered = render_to_string('emails/email.html', {'users': data})
    plain_message = strip_tags(rendered)
    send_mail(subject='Subject', message=plain_message, from_email=settings.EMAIL_FROM,
              recipient_list=[settings.EMAIL_TO],
              html_message=rendered)


@app.task
def get_logs():
    data = get_data_log()
    for item in data['items']:
        TrackedEmail.objects.update_or_create(email=item['recipient'],
                                              message_id=item['message']['headers']['message-id'],
                                              status=item['event'],
                                              timestamp=datetime.datetime.fromtimestamp(item['timestamp'],
                                                                                        tz=pytz.timezone(
                                                                                            settings.TIME_ZONE)))