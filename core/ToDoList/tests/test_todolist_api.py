from rest_framework.test import APIClient
from django.urls import reverse
from accounts.models import User
import pytest

@pytest.fixture
def common_user():
    user= User.object.create_user(email="system@user.com", password="Pp123!@#")
    return user


@pytest.mark.django_db
class TestTodolistApi():
    client = APIClient()

    def test_get_tasks_successfully(self, common_user):

        url = reverse("tasks:tasks-api-v1:task-list")
        user = common_user
        self.client.force_login(user=user)
        response = self.client.get(url)
        assert response.status_code == 200
    
    
    def test_create_task_successfully(self, common_user):

        url = reverse("tasks:tasks-api-v1:task-list")
        data = {
            'email': 'system@user.com',
            'task': 'test task :)'
        }
        user = common_user
        self.client.force_login(user=user)
        response = self.client.post(url, data)
        assert response.status_code == 201
    

    def test_get_tasks_unauthrized(self):

        url = reverse("tasks:tasks-api-v1:task-list")
        response = self.client.get(url)
        assert response.status_code == 401


    def test_create_task_badrequest(self, common_user):

        url = reverse("tasks:tasks-api-v1:task-list")
        data = {
            'task': 'test task :)'
        }
        user = common_user
        self.client.force_login(user=user)
        response = self.client.post(url, data)
        assert response.status_code == 400




@pytest.mark.django_db
class TestTodolistDetailApi():
    client = APIClient()

    def test_get_detail_task_successfully(self, common_user):
        
        url = reverse("tasks:tasks-api-v1:task-detail", kwargs={'pk':1})
        url_create = reverse("tasks:tasks-api-v1:task-list")
        data = {
            'email': 'system@user.com',
            'task': 'test task :)'
        }
        user = common_user
        self.client.force_login(user=user)
        response = self.client.post(url_create, data)
        assert response.status_code == 201
        response = self.client.get(url)
        assert response.status_code == 200


    def test_edit_detail_task_successfully(self, common_user):
        
        url = reverse("tasks:tasks-api-v1:task-detail", kwargs={'pk':1})
        url_create = reverse("tasks:tasks-api-v1:task-list")
        data = {
            'email': 'system@user.com',
            'task': 'test task :)'
        }
        edit_data = {
            'email': 'system@user.com',
            'task': 'task edited'
        }
        user = common_user
        self.client.force_login(user=user)
        response = self.client.post(url_create, data)
        assert response.status_code == 201
        response = self.client.put(url, edit_data)
        assert response.status_code == 200
    
    
    def test_delete_detail_task_successfully(self, common_user):
        
        url = reverse("tasks:tasks-api-v1:task-detail", kwargs={'pk':1})
        url_create = reverse("tasks:tasks-api-v1:task-list")
        data = {
            'email': 'system@user.com',
            'task': 'test task :)'
        }
        user = common_user
        self.client.force_login(user=user)
        response = self.client.post(url_create, data)
        assert response.status_code == 201
        response = self.client.delete(url)
        assert response.status_code == 204

    
    def test_get_detail_task_notfound(self, common_user):
        
        url = reverse("tasks:tasks-api-v1:task-detail", kwargs={'pk':1})
        user = common_user
        self.client.force_login(user=user)
        response = self.client.get(url)
        assert response.status_code == 404

    
    def test_edit_detail_task_badrequest(self, common_user):
        
        url = reverse("tasks:tasks-api-v1:task-detail", kwargs={'pk':1})
        url_create = reverse("tasks:tasks-api-v1:task-list")
        data = {
            'email': 'system@user.com',
            'task': 'test task :)'
        }
        edit_data = {
            'task': 'task edited'
        }
        user = common_user
        self.client.force_login(user=user)
        response = self.client.post(url_create, data)
        assert response.status_code == 201
        response = self.client.put(url, edit_data)
        assert response.status_code == 400