from django.utils import timezone

from rest_framework import status
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.pagination import PageNumberPagination
from .models import Task, SubTask
from .serializers import (
    TaskSerializer,
    SubTaskSerializer,
    SubTaskCreateSerializer)
from django.db.models import Count, Q


class TaskCreateView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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


class SubTaskListCreateView(generics.ListCreateAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskCreateSerializer

    def get_serializer_class(self):
        if self.request.method == 'POST':
            return SubTaskCreateSerializer
        return SubTaskSerializer


class SubTaskDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = SubTask.objects.all()
    serializer_class = SubTaskCreateSerializer

    def get_serializer_class(self):
        if self.request.method in ['PUT', 'PATCH']:
            return SubTaskCreateSerializer
        return SubTaskSerializer
