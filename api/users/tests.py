from django.contrib.auth.models import User

from rest_framework.status import HTTP_200_OK, HTTP_201_CREATED, HTTP_400_BAD_REQUEST, HTTP_403_FORBIDDEN

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


class ProfileTest(BaseAPITest):

    url = 'profile'

    def test_get_profile(self):
        data = self.get_and_check_status(self.url, HTTP_200_OK)
        self.assertEqual(data['username'], self.user.username)

    def test_profile_not_available_for_anonymous_users(self):
        self.client.logout()
        self.get_and_check_status(self.url, HTTP_403_FORBIDDEN)

    def test_profile_update(self):
        new_name = 'New name'
        data = {'first_name': new_name}
        self.assertNotEqual(self.user.first_name, new_name)

        self.patch_and_check_status(self.url, data, HTTP_200_OK)

        user = User.objects.get(pk=self.user.pk)
        self.assertEqual(user.first_name, 'New name')

