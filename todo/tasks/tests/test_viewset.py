from rest_framework import status

from datetime import datetime, timedelta

from tasks.models import Task


DEFAULT_ROUTE = '/api/tasks/'


class TestTaskViewSet:
    def test_get_tasks(self, client):
        response = client.get(DEFAULT_ROUTE)
        assert response.status_code == status.HTTP_200_OK

    def test_create_task(self, user, client):
        tasks_count_before = Task.objects.count()
        data = {
            'description': 'wash hands',
            'expired_at': datetime.now() + timedelta(days=1),
            'user': user.id,
        }
        response = client.post(DEFAULT_ROUTE, data=data)
        tasks_count_after = Task.objects.count()
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['description'] == data['description']
        assert tasks_count_before == tasks_count_after - 1

    def test_update_task(self, user, client, task):
        data = {
            'description': 'updated task',
            'expired_at': datetime.now() + timedelta(days=1),
            'user': user.id,
        }
        response = client.put(DEFAULT_ROUTE + f'{task.id}/', data)
        assert response.status_code == status.HTTP_200_OK
        assert response.data['description'] == data['description']

    def test_delete_task(self, client, task):
        tasks_count_before = Task.objects.count()
        response = client.delete(DEFAULT_ROUTE + f'{task.id}/')
        tasks_count_after = Task.objects.count()
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert tasks_count_before == tasks_count_after + 1
