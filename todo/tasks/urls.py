from django.urls import path

from .views import TaskDetailViewSet, TaskViewSet


urlpatterns = [
    path('tasks/', TaskViewSet.as_view()),
    path('tasks/<int:pk>/', TaskDetailViewSet.as_view()),
]
