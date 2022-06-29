from django.db import models
from django.contrib.auth.models import User


STATUS_CHOICES = (
    ('TO_DO', 'To do'),
    ('IN_PROGRESS', 'In progress'),
    ('FINISHED', 'Finished'),
)


class Task(models.Model):
    description = models.TextField(null=False, blank=False)
    status = models.CharField(max_length=25, choices=STATUS_CHOICES, default='TO_DO')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='tasks')
    created_at = models.DateTimeField(auto_now_add=True)
    expired_at = models.DateTimeField()

    def __str__(self):
        return f'{self.description}, {self.status}'
