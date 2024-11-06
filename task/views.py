from django.utils import timezone

from rest_framework import status
from rest_framework import generics
from rest_framework import filters
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework.decorators import action
from django_filters.rest_framework import DjangoFilterBackend
from .models import Task, SubTask, Category
from .serializers import (
    TaskCreateSerializer,
    SubTaskCreateSerializer,
    TaskSerializer,
    CategoryCreateSerializer
)
from django.db.models import Count, Q
# task/pagination.py
from rest_framework.pagination import PageNumberPagination


class TaskCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'deadline']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']
    ordering = ['-created_at']


class TaskListView(generics.ListAPIView):
    serializer_class = TaskSerializer
    pagination_class = PageNumberPagination

    def get_queryset(self):
        queryset = Task.objects.all()
        status = self.request.query_params.get('status', None)
        deadline = self.request.query_params.get('deadline', None)
        if status is not None:
            queryset = queryset.filter(status=status)
        if deadline is not None:
            queryset = queryset.filter(deadline__lte=deadline)
        return queryset


class TaskStatsView(APIView):
    def get(self, request, *args, **kwargs):
        total_tasks = Task.objects.count()
        status_counts = Task.objects.values('status').annotate(count=Count('status'))
        overdue_tasks = Task.objects.filter(deadline__lt=timezone.now()).count()

        stats = {
            'total_tasks': total_tasks,
            'status_counts': status_counts,
            'overdue_tasks': overdue_tasks
        }
        return Response(stats)


# class SubTaskListCreateView(generics.ListCreateAPIView):
#     queryset = SubTask.objects.all()
#     serializer_class = SubTaskCreateSerializer
#
#     def get_serializer_class(self):
#         if self.request.method == 'POST':
#             return SubTaskCreateSerializer
#         return SubTaskSerializer

class SubTaskListCreateView(generics.ListCreateAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskCreateSerializer
    pagination_class = PageNumberPagination
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['status', 'deadline']
    search_fields = ['title', 'description']
    ordering_fields = ['created_at']
    ordering = ['-created_at']


# class SubTaskDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = SubTask.objects.all()
#     serializer_class = SubTaskCreateSerializer
#
#     def get_serializer_class(self):
#         if self.request.method in ['PUT', 'PATCH']:
#             return SubTaskCreateSerializer
#         return SubTaskSerializer

class SubTaskDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskCreateSerializer


class TaskDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoryCreateSerializer

    @action(detail=True, methods=['get'])
    def count_tasks(self, request, pk=None):
        category = self.get_object()
        task_count = Task.objects.filter(category=category).count()
        return Response({'task_count': task_count})
