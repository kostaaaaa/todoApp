from django.urls import path

from .views import TaskDetailViewSet, TaskViewSet


urlpatterns = [
    path('tasks-list/', TaskViewSet.as_view()),
    path('tasks-list/<int:pk>/', TaskDetailViewSet.as_view()),
]
