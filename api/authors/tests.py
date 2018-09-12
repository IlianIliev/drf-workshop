from rest_framework.status import HTTP_200_OK
from api.tests.utils import BaseAPITest

from authors.factories import AuthorFactory


class AuthorsTest(BaseAPITest):
    base_url = 'authors/'

    def test_get_list_of_authors(self):
        data = self.get_and_check_status(self.base_url, HTTP_200_OK)
        self.assertEqual(data['count'], 0)

        AuthorFactory()
        AuthorFactory()

        data = self.get_and_check_status(self.base_url, HTTP_200_OK)
        self.assertEqual(data['count'], 2)

