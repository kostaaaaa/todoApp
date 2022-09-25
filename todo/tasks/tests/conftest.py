import pytest
from django.contrib.auth.models import User
from rest_framework.test import APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from datetime import datetime, timedelta

from tasks.models import Task


@pytest.fixture
def user(db):
    user, _ = User.objects.get_or_create(username='testcase')
    return user


@pytest.fixture
def client(db, user):
    client = APIClient()
    token = RefreshToken.for_user(user)
    client.credentials(HTTP_AUTHORIZATION=f'Bearer {token.access_token}')
    return client


@pytest.fixture
def task(db, user):
    return Task.objects.create(
        description = 'wash hands',
        expired_at = datetime.now() + timedelta(days=1),
        user = user,
    )
