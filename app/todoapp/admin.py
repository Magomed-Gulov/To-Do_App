from django.contrib import admin

from .models import TodoListItem


class TodoListItemAdmin(admin.ModelAdmin):
    fields = ['pub_date', 'question_text']

admin.site.register(TodoListItem, TodoListItemAdmin)