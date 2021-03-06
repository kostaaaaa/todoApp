from datetime import datetime
from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend

from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(generics.ListCreateAPIView):
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ('status',)

    def get_queryset(self):
        now = datetime.now()
        user = self.request.user
        return Task.objects.filter(user=user, expired_at__gte=now)


class TaskDetailViewSet(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TaskSerializer

    def get_queryset(self):
        user = self.request.user
        return Task.objects.filter(user=user)
