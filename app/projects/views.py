from django.db.models import Q, Sum
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from app.projects.models import Project, Task
from app.projects.serializers import ProjectsSerializer, TasksSerializer
from app.projects.permissions import (
    IsOwnerOrIsSharedWithProject,
    IsOwnerOrIsSharedWithTask,
)


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows projects to be created, viewed, edited or deleted.
    """

    permission_classes = [permissions.IsAuthenticated, IsOwnerOrIsSharedWithProject]
    serializer_class = ProjectsSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def perform_update(self, serializer):
        serializer.save(modified_by=self.request.user)

    # def get_object(self):
    #     return Project.objects.get(id=self.request.user.id)

    def get_queryset(self):
        """
        Gets all projects that have been created by or shared with someone
        """
        return Project.objects.owner_or_shared_with(self.request.user)

    @action(detail=True, methods=["get"])
    def summary(self, request, pk=None):
        """
        Custom action that gets project's summary, such as total of tasks,
        completed tasks and other attributes

        Very useful for having a fast insight about the project's current status.
        Also great for building a dashboard.
        """
        # get total tasks, complete, total money balance, income, expenses
        project = Project.objects.get(pk=pk)
        total_tasks = Task.objects.filter(project_id=project.id).count()
        completed_tasks = (
            Task.objects.filter(project_id=project.id).filter(completed=True).count()
        )
        value_spent = Task.objects.filter(project_id=project.id).aggregate(Sum("value"))

        summary_data = {
            "total tasks": total_tasks,
            "completed tasks": completed_tasks,
            "value_spent": value_spent,
        }
        return Response(summary_data)


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be created, viewed, edited or deleted.
    """

    permission_classes = [permissions.IsAuthenticated, IsOwnerOrIsSharedWithTask]
    serializer_class = TasksSerializer

    def perform_create(self, serializer):
        serializer.save(created_by=self.request.user)

    def get_queryset(self):
        """
        Gets all tasks that have been created by or shared with someone
        """
        return Task.objects.owner_or_shared_with(self.request.user)
