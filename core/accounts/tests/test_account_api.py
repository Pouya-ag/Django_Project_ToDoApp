from rest_framework.test import APIClient
from django.urls import reverse
from accounts.models import User
import pytest


@pytest.fixture
def common_user():
    user= User.object.create_user(email="system@user.com", password="Pp123!@#")
    return user


@pytest.mark.django_db
class TestAccountApi():
    client = APIClient()

    def test_login_successfully(self):

        url = reverse("accounts:api-v1:login")
        response = self.client.get(url)
        assert response.status_code == 200


    def test_register_successfully(self):

        url = reverse("accounts:api-v1:register")
        data = {
            'email': 'test@test.com',
            'password': 'Pp123!@#',
            'password1': 'Pp123!@#',
        }
        response = self.client.post(url,data)
        assert response.status_code == 201
    
    
    def test_register_fail(self):

        url = reverse("accounts:api-v1:register")
        data = {
            'email': 'test@test.com',
            'password': 'Pp123!@#',
            'password1': 'Pp123!@',
        }
        response = self.client.post(url,data)
        assert response.status_code == 400


    def test_change_password_successfully(self, common_user):

        url = reverse("accounts:api-v1:change-password")
        data = {
            'old_password': 'Pp123!@#',
            'new_password': 'Pp123!@#ed',
            'new_password1': 'Pp123!@#ed',
        }
        user = common_user
        self.client.force_login(user=user)
        response = self.client.put(url,data)
        assert response.status_code == 200
    
    
    def test_change_password_fail(self, common_user):

        url = reverse("accounts:api-v1:change-password")
        data = {
            'old_password': 'Pp123!@',
            'new_password': 'Pp123!@#ed',
            'new_password1': 'Pp123!@#ed',
        }
        user = common_user
        self.client.force_login(user=user)
        response = self.client.put(url,data)
        assert response.status_code == 400