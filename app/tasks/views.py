from django.shortcuts import render
from rest_framework import viewsets, permissions
from app.tasks.models import Task
from app.tasks.serializers import TasksSerializer


# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be created, viewed, edited or deleted.
    """
    permission_classes = [permissions.IsAuthenticated]
    queryset = Task.objects.all().order_by("created")
    serializer_class = TasksSerializer


    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)