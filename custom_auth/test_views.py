import pytest
from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth import get_user_model
from rest_framework import status


class BaseCustomAuthViewsTestCase(APITestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(email='test_user@email.com', password='test_password')


class LoginViewTests(BaseCustomAuthViewsTestCase):
    def setUp(self):
        super().setUp()
        self.url = reverse('api-login')
        self.client.force_login(self.user)

    @pytest.mark.django_db
    def test_login(self):
        data = {'email': 'test_user@email.com', 'password': 'test_password'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    @pytest.mark.django_db
    def test_login_invalid_credentials(self):
        data = {'email': 'test_user@email.com', 'password': 'wrong_password'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @pytest.mark.django_db
    def test_login_with_missing_email(self):
        data = {'password': 'test_password'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    @pytest.mark.django_db
    def test_login_with_missing_password(self):
        data = {'email': 'test_user'}
        response = self.client.post(self.url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class LogoutViewTests(BaseCustomAuthViewsTestCase):
    def setUp(self):
        super().setUp()
        self.client.login(email='test_user@email.com', password='test_password')
        self.url = reverse('api-logout')

    def test_logout(self):
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'detail': 'Successfully logged out.'})

    def test_logout_without_authentication(self):
        self.client.logout()
        response = self.client.post(self.url)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class SessionViewTests(BaseCustomAuthViewsTestCase):
    def setUp(self):
        super().setUp()
        self.client.login(email='test_user@email.com', password='test_password')
        self.url = reverse('api-session')

    def test_get_session(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'isAuthenticated': True})

    def test_get_session_without_authentication(self):
        self.client.logout()
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class WhoIAmViewTests(BaseCustomAuthViewsTestCase):
    def setUp(self):
        super().setUp()
        self.url = reverse('api-whoami')

    def test_get_whoiam_authenticated(self):
        self.client.force_login(self.user)
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json(), {'email': self.user.email})

    def test_get_whoiam_unauthenticated(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.json(), {'isAuthenticated': False})
