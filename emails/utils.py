from __future__ import unicode_literals
import json
import requests
from django.conf import settings
from emails.models import Subscriber


def get_email_data():
    subscribers = Subscriber.objects.all()
    result = list()
    for user in subscribers:
        result.append(
            {
                'name': user.name + ' ' + user.surname,
                'birthday': user.birthday.strftime('%d.%m.%Y'),
            }
        )
    return result


def get_data_log():
    data = requests.get('https://api.mailgun.net/v3/%s/events' % settings.MAILGUN_SERVER_NAME,
                        auth=('api', settings.MAILGUN_ACCESS_KEY))
    return json.loads(data.content)