from django.contrib import admin

from apps.todo.models import Todo

# Register your models here.
@admin.register(Todo)
class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'descriptions', 'is_complated', 'created_at', 'image')
    search_fields = ('title', 'descriptions')
