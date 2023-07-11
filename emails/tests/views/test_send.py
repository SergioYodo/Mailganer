import pytest
from django.test import Client
from django.urls import reverse


@pytest.fixture()
def send_email_mock(mocker):
    return mocker.patch('emails.views.send_email.delay')


def test_send(send_email_mock):
    response = Client().get(reverse('send'))
    assert response.status_code == 302
    send_email_mock.assert_called_once()
