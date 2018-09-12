import factory

from faker import Factory

from authors.models import Author


faker = Factory.create()


class AuthorFactory(factory.DjangoModelFactory):
    name = factory.LazyAttribute(lambda x: '{} {}'.format(faker.first_name(), faker.last_name()))
    date_of_birth = factory.LazyAttribute(lambda x: faker.date_of_birth())
    website = factory.LazyAttribute(lambda x: faker.url())
    bio = factory.LazyAttribute(lambda x: faker.text())
    class Meta:
        model = Author
