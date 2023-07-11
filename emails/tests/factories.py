import factory

from emails.models import Subscribers


class SubscribersFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Subscribers

    name = factory.Faker('first_name')
    surname = factory.Faker('last_name')
    birthday = factory.Faker('date')
