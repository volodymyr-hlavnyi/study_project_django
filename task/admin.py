from django.contrib import admin
from .models import Task, SubTask, Category

@admin.register(Task)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    search_fields = ('title',)

@admin.register(SubTask)
class SubTaskAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at', 'task')
    search_fields = ('title', 'task__title')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)