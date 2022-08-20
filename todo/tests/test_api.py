import pytest


pytestmark = pytest.mark.django_db

class TestAPI:
    def test_get_tasks(self, client):
        client = client
        response = client.get('/api/tasks-list/')
        assert response.status_code == 200


    def test_create_task(self, client):
        client = client
        data = {
            'description': 'wash hands',
            'expired_at': '2022-08-19 11:46',
            'user': 1,
        }
        response = client.post('/api/tasks-list/', data=data, format='json')
        assert response.status_code == 201


    def test_update_task(self, client):
        client = client
        fake_data = {
            'description': 'wash hands',
            'expired_at': '2022-08-19 11:46',
            'user': 1,
        }
        client.post('/api/tasks-list/', data=fake_data)

        data = {
            'description': 'updated task',
            'expired_at': '2022-08-19T11:46:53.362Z',
            'user': 1,
        }
        response = client.put('/api/tasks-list/1/', data)
        assert response.status_code == 200


    def test_delete_task(self, client):
        client = client
        fake_data = {
            'description': 'wash hands',
            'expired_at': '2022-08-19 11:46',
            'user': 1,
        }
        client.post('/api/tasks-list/', data=fake_data)

        response = client.delete('/api/tasks-list/1/')
        assert response.status_code == 204
