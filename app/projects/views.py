from django.shortcuts import render
from django.db.models import Q
from rest_framework import viewsets, permissions
from app.projects.models import Project
from app.projects.serializers import ProjectsSerializer
from app.projects.permissions import IsOwnerOrIsSharedWith


# Create your views here.
class ProjectViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows projects to be created, viewed, edited or deleted.
    """

    permission_classes = [permissions.IsAuthenticated, IsOwnerOrIsSharedWith]
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
