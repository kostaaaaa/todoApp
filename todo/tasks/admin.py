from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'description',
        'status',
        'todo_until',
    )
    readonly_fields = ('user', 'created_at',)


admin.site.register(Task, TaskAdmin)
