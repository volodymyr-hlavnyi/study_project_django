from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import (
    CategoryViewSet,
    TaskStatsView,
    SubTaskListCreateView,
    SubTaskDetailUpdateDeleteView, TaskListCreateView, TaskDetailUpdateDeleteView
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')


urlpatterns = [
    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailUpdateDeleteView.as_view(), name='task-detail-update-delete'),
    path('stats/', TaskStatsView.as_view(), name='task-stats'),
    path('subtasks/', SubTaskListCreateView.as_view(), name='subtask-list-create'),
    path('subtasks/<int:pk>/', SubTaskDetailUpdateDeleteView.as_view(), name='subtask-detail-update-delete'),
]
