from django.shortcuts import render
from rest_framework import viewsets, permissions
from app.tasks.models import Task
from app.tasks.serializers import TasksSerializer
from app.tasks.permissions import IsOwnerOrIsSharedWith


# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be created, viewed, edited or deleted.
    """

    permission_classes = [permissions.IsAuthenticated, IsOwnerOrIsSharedWith]
    serializer_class = TasksSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def get_queryset(self):
        return Task.objects.filter(creator=self.request.user).order_by("created")
