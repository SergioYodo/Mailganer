import pytest

from emails.tasks import send_email


@pytest.mark.django_db
def test_send_email(subscribers_factory, mailoutbox, settings):
    subscribers_factory.create_batch(10)
    send_email()

    assert len(mailoutbox) == 1
    mail = mailoutbox[0]
    assert mail.subject == 'Subject'
    assert mail.to == [settings.EMAIL_TO]