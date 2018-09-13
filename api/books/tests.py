from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_204_NO_CONTENT

from api.tests.utils import BaseAPITest

from authors.factories import AuthorFactory
from books.factories import BookFactory
from books.models import Book


class BooksTest(BaseAPITest):
    url = 'books/'

    def test_list_books(self):
        BookFactory()
        BookFactory()

        data = self.get_and_check_status(self.url, HTTP_200_OK)
        self.assertEqual(data['count'], 2)

    def test_create_book(self):
        zelazny = AuthorFactory(name='Roger Zelazny')
        sheckley = AuthorFactory(name='Robert Sheckley')

        data = {
            'title': 'Bring Me the Head of Prince Charming',
            'set_authors': [zelazny.pk, sheckley.pk],
            'description': (
                'Every millennium a big contest is waged between the forces of good, and the forces of evil, a '
                'contest that determines the turn of events in the upcoming millennium...'
            )
        }

        result = self.post_and_check_status(self.url, data, HTTP_201_CREATED)

        book = Book.objects.get(pk=result['id'])

        self.assertEqual(book.title, data['title'])
        self.assertEqual(list(book.authors.all()), [zelazny, sheckley])

    def test_update_book(self):
        zelazny = AuthorFactory(name='Roger Zelazny')
        sheckley = AuthorFactory(name='Robert Sheckley')
        pratchett = AuthorFactory(name='Terry Pratchett')

        book = Book.objects.create(title='Bring Me the Head of Prince Charming')
        book.authors.add(zelazny, pratchett)

        url = '{}{}/'.format(self.url, book.pk)

        self.patch_and_check_status(url, {'set_authors': [zelazny.pk, sheckley.pk]}, HTTP_200_OK)

        book = Book.objects.get(pk=book.pk)
        self.assertEqual(list(book.authors.all()), [zelazny, sheckley])

    def test_delete_book(self):
        book = BookFactory()
        url = '{}{}/'.format(self.url, book.pk)
        self.delete_and_check_status(url, HTTP_204_NO_CONTENT)

        self.client.logout()

        book = BookFactory()
        url = '{}{}/'.format(self.url, book.pk)
        self.delete_and_check_status(url, HTTP_204_NO_CONTENT)





