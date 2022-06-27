from django.urls import path

from .views import TaskDetailViewSet, TaskViewSet


urlpatterns = [
    path('task-list/', TaskViewSet.as_view()),
    path('task-list/<int:pk>/', TaskDetailViewSet.as_view()),
]
