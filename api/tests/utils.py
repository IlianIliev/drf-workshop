from django.test import TestCase
from rest_framework.test import APIClient, APIRequestFactory

from users.factories import UserFactory


API_BASE_URL = 'api'


REQUEST_FACTORY = APIRequestFactory()


class BaseAPIClient(APIClient):

    def request(self, **kwargs):
        if 'PATH_INFO' in kwargs and not kwargs['PATH_INFO'].startswith('/{}/'.format(API_BASE_URL)):
            kwargs['PATH_INFO'] = '/{}/{}'.format(API_BASE_URL, kwargs['PATH_INFO'])
        return super().request(**kwargs)


class BaseAPITest(TestCase):
    client_class = BaseAPIClient

    DO_SETUP = True

    def setUp(self):
        if self.DO_SETUP:
            self.longMessage = True
            self.password = 'password'
            self.user = UserFactory.create(
                email='tester@example.com', username='tester@example.com', password=self.password)
            self.user2 = UserFactory.create(
                email='tester2@example.com', username='tester2@example.com', password=self.password)
            self.login_user(self.user)

    def login_user(self, user):
        self.client.login(username=user.email, password='password')

    def get_request_context(self):
        request = REQUEST_FACTORY.request()
        request.user = self.user
        return {
            'request': request
        }

    def _request_and_check_status(self, method_name, url, expected_status, data=None, full_response=False):
        method = getattr(self.client, method_name)
        response = method(url, data, format='json')
        self.assertEqual(expected_status, response.status_code, getattr(response, 'data', None))
        if full_response:
            return response
        return getattr(response, 'data', None)

    def get_and_check_status(self, url, expected_status, data=None, full_response=False):
        return self._request_and_check_status('get', url, expected_status, data, full_response=full_response)

    def post_and_check_status(self, url, data, expected_status, full_response=False):
        return self._request_and_check_status('post', url, expected_status, data, full_response=full_response)

    def delete_and_check_status(self, url, expected_status, full_response=False):
        return self._request_and_check_status('delete', url, expected_status, full_response=full_response)

    def patch_and_check_status(self, url, data, expected_status, full_response=False):
        return self._request_and_check_status('patch', url, expected_status, data, full_response=full_response)

    def serializer_fields_check(self, serializer):
        self.assertEqual(self.expected_fields, set(serializer.data.keys()), 'Serializer keys differ from the expected')
