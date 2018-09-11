from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST

from api.tests.utils import BaseAPITest


class SignupTest(BaseAPITest):
    url = 'users/signup'

    DO_SETUP = False

    def test_signup(self):
        data = {
            'email': 'user@example.org',
            'username': 'user',
            'password': 'ASD123asd'
        }

        self.post_and_check_status(self.url, data, HTTP_201_CREATED)

    def test_signup_with_invalid_data(self):
        data = {
            'email': 'user',
            'username': 'user',
        }

        response = self.post_and_check_status(self.url, data, HTTP_400_BAD_REQUEST)

        self.assertTrue('email' in response)
        self.assertTrue('password' in response)
        self.assertFalse('username' in response)


class LoginTest(BaseAPITest):
    DO_SETUP = True
    url = 'users/login'

    def test_login(self):


        data = {
            'username': self.user.username,
            'password': self.password
        }

        self.post_and_check_status(self.url, data, HTTP_200_OK)
