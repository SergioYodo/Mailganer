import pytest
from emails.utils import get_email_data


@pytest.mark.django_db
def test_get_email_data(subscribers_factory):
    subscribers_factory.create_batch(10)
    assert len(get_email_data()) == 10
