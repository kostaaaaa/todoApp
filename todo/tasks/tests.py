from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from rest_framework_simplejwt.tokens import RefreshToken

from datetime import datetime, timedelta

from tasks.models import Task


DEFAULT_ROUTE = '/api/tasks/'


class TaskApiTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='test')
        self.client = APIClient()
        token = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token.access_token}')
        self.task = Task.objects.create(
            description = 'wash hands',
            expired_at = datetime.now() + timedelta(days=1),
            user = self.user,
            )

    def test_get_tasks(self):
        response = self.client.get(DEFAULT_ROUTE)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_task(self):
        tasks_count_before = Task.objects.count()
        data = {
            'description': 'wash hands',
            'expired_at': datetime.now() + timedelta(days=1),
            'user': self.user.id,
        }
        response = self.client.post(DEFAULT_ROUTE, data)
        tasks_count_after = Task.objects.count()
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(tasks_count_before, tasks_count_after - 1)

    def test_put_task(self):
        data = {
            'description': 'updated task',
            'expired_at': datetime.now() + timedelta(days=1),
            'user': self.user.id,
        }
        response = self.client.put(DEFAULT_ROUTE + f'{self.task.id}/', data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['description'], data['description'])

    def test_delete_task(self):
        tasks_count_before = Task.objects.count()
        response = self.client.delete(DEFAULT_ROUTE + f'{self.task.id}/')
        tasks_count_after = Task.objects.count()
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(tasks_count_before, tasks_count_after + 1)
