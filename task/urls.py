from rest_framework.routers import DefaultRouter
from django.urls import path
from .views import (
    CategoryViewSet,
    TaskStatsView,
    SubTaskListCreateView,
    SubTaskDetailUpdateDeleteView, TaskListCreateView, TaskDetailUpdateDeleteView, LoginView, LogoutView, RegisterView,
    PrivateView, UserTaskListView, UserSubTaskListView
)

from django.urls import path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

router = DefaultRouter()
router.register(r'categories', CategoryViewSet, basename='category')

urlpatterns = [

    path('tasks/', TaskListCreateView.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetailUpdateDeleteView.as_view(), name='task-detail-update-delete'),

    path('stats/', TaskStatsView.as_view(), name='task-stats'),

    path('subtasks/', SubTaskListCreateView.as_view(), name='subtask-list-create'),
    path('subtasks/<int:pk>/', SubTaskDetailUpdateDeleteView.as_view(), name='subtask-detail-update-delete'),

    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('api/login/', LoginView.as_view(), name='login'),
    path('api/logout/', LogoutView.as_view(), name='logout'),
    path('api/register/', RegisterView.as_view(), name='register'),
    path('private/', PrivateView.as_view(), name='private'),

    path('user/tasks/', UserTaskListView.as_view(), name='user-task-list'),
    path('user/subtasks/', UserSubTaskListView.as_view(), name='user-subtask-list'),

]
