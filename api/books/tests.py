from rest_framework.status import HTTP_200_OK

from api.tests.utils import BaseAPITest

from books.factories import BookFactory


class BooksTest(BaseAPITest):
    url = 'books/'

    def test_list_books(self):
        BookFactory()
        BookFactory()

        data = self.get_and_check_status(self.url, HTTP_200_OK)
        self.assertEqual(data['count'], 2)
