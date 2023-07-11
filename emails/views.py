from __future__ import unicode_literals
from django.shortcuts import redirect
from django.views.generic import TemplateView
from emails.tasks import send_email


class HomeView(TemplateView):
    template_name = 'emails/home.html'


def send(request):
    send_email.delay()
    return redirect('home')
