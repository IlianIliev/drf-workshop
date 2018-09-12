import factory

from faker import Factory

from authors.factories import AuthorFactory
from books.models import Book


faker = Factory.create()


class BookFactory(factory.DjangoModelFactory):
    title = factory.LazyAttribute(lambda x: faker.sentence())
    description = factory.LazyAttribute(lambda x: faker.text())

    class Meta:
        model = Book

    @factory.post_generation
    def authors(self, create, extracted, **kwargs):
        if not create:
            return

        if not extracted:
            extracted = [AuthorFactory(), ]

        for author in extracted:
            self.authors.add(author)
