from django.shortcuts import render
from django.db.models import Q
from rest_framework.exceptions import PermissionDenied
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
        import ipdb; ipdb.set_trace(context=10)
        if serializer.data.get("project") in self.request.user.project_set.all():
            serializer.save(creator=self.request.user)
        else:
            serializer.data = None
            return PermissionDenied()

    def get_queryset(self):
        """
        Gets all tasks that have been created by or shared with someone
        """
        query_shared = self.request.user.task_set.all()
        query_creator = Task.objects.filter(creator=self.request.user)
        full_query = query_creator | query_shared

        return full_query.distinct().order_by("created")
