from django.db.models import Q, Sum
from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response
from app.projects.models import Project, Task
from app.projects.serializers import ProjectsSerializer, TasksSerializer
from app.projects.permissions import IsOwnerOrIsSharedWithProject, IsOwnerOrIsSharedWithTask


class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows projects to be created, viewed, edited or deleted.
    """

    permission_classes = [permissions.IsAuthenticated, IsOwnerOrIsSharedWithProject]
    serializer_class = ProjectsSerializer

    def perform_create(self, serializer):
        serializer.save(creator=self.request.user)

    def get_queryset(self):
        """
        Gets all projects that have been created by or shared with someone
        """
        query_shared = self.request.user.project_set.all()
        query_creator = Project.objects.filter(creator=self.request.user)
        full_query = query_creator | query_shared

        return full_query.distinct().order_by("created")

    @action(detail=True, methods=['get'])
    def summary(self, request, pk=None):
        """
        Custom action that gets project's summary, such as total of tasks,
        completed tasks and other attributes

        Very useful for having a fast insight about the project's current status.
        Also great for building a dashboard.
        """
        project = Project.objects.get(pk=pk)
        # get total tasks, complete, total money balance, income, expenses
        total_tasks = Task.objects.filter(project_id=project.id).count()
        completed_tasks = Task.objects.filter(project_id=project.id).filter(completed=True).count()
        value_spent = Task.objects.filter(project_id=project.id).aggregate(Sum('value'))

        summary_data = {
            "total tasks": total_tasks,
            "completed tasks": completed_tasks,
        }
        return Response(summary_data)


class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be created, viewed, edited or deleted.
    """

    permission_classes = [permissions.IsAuthenticated, IsOwnerOrIsSharedWithTask]
    serializer_class = TasksSerializer

    # def perform_create(self, serializer):
    #     import ipdb; ipdb.set_trace()
    #     if serializer.data.get("project") in self.request.user.project_set.all():
    #         serializer.save(creator=self.request.user)
    #     else:
    #         # serializer.data = None
    #         return PermissionDenied()

    def get_queryset(self):
        """
        Gets all tasks that have been created by or shared with someone
        """
        query_shared = self.request.user.task_set.all()
        query_creator = Task.objects.filter(creator=self.request.user)
        full_query = query_creator | query_shared

        return full_query.distinct().order_by("created")
