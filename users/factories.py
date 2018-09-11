import factory

from django.contrib.auth.models import User

from faker import Factory


faker = Factory.create()


class UserFactory(factory.DjangoModelFactory):
    first_name = factory.LazyAttribute(lambda x: faker.first_name())
    last_name = factory.LazyAttribute(lambda x: faker.last_name())

    class Meta:
        model = User
