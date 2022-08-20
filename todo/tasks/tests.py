import unittest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken


class APITest(unittest.TestCase):
    def setUp(self):
        user = User.objects.all().first()
        client = APIClient()
        token = RefreshToken.for_user(user)
        client.credentials(HTTP_AUTHORIZATION=f'Bearer {token.access_token}')
        self.client = client


    def test_get_tasks(self):
        response = self.client.get('/api/tasks-list/')
        self.assertEqual(response.status_code, 200)


    def test_create_task(self):
        data = {
            'description': 'wash hands',
            'expired_at': '2022-08-19T11:46:53.362Z',
            'user': 1,
        }
        response = self.client.post('/api/tasks-list/', data)
        self.assertEqual(response.status_code, 201)


    def test_put_task(self):
        tasks = self.client.get('/api/tasks-list/')
        content = tasks.data[0].items()
        id = list(content)[0][1]
        
        data = {
            'description': 'updated task',
            'expired_at': '2022-08-19T11:46:53.362Z',
            'user': 1,
        }
        response = self.client.put(f'/api/tasks-list/{id}/', data)
        self.assertEqual(response.status_code, 200)


    def test_remove_task(self):
        get_task = self.client.get('/api/tasks-list/')
        data = get_task.data[0].items()
        id = list(data)[0][1]

        response = self.client.delete(f'/api/tasks-list/{id}/')
        self.assertEqual(response.status_code, 204)
