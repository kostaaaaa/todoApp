from django.contrib import admin
from .models import Task


class TaskAdmin(admin.ModelAdmin):
    list_display = (
        'description',
        'status',
        'expired_at',
        'user',
    )
    readonly_fields = ('created_at',)


admin.site.register(Task, TaskAdmin)
