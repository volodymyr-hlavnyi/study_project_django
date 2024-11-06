from django.urls import path
from .views import (
    TaskCreateView,
    TaskListView,
    TaskStatsView,
    SubTaskListCreateView,
    SubTaskDetailUpdateDeleteView
)

urlpatterns = [
    path('create/', TaskCreateView.as_view(), name='task-create'),
    path('list/', TaskListView.as_view(), name='task-list'),
    path('stats/', TaskStatsView.as_view(), name='task-stats'),

    path('subtasks/', SubTaskListCreateView.as_view(), name='subtask-list-create'),
    path('subtasks/<int:pk>/', SubTaskDetailUpdateDeleteView.as_view(), name='subtask-detail-update-delete')

]