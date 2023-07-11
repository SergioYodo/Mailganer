import pytest
from pytest import register

from emails.tests.factories import SubscribersFactory

register(SubscribersFactory)


@pytest.fixture()
def user(user_factory):
    return user_factory()


@pytest.fixture()
def admin(user_factory):
    return user_factory(is_staff=True)