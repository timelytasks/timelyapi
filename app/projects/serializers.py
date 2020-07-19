from rest_framework import serializers
from app.projects.models import Project, Task
from app.users.serializers import UserSerializer


class TasksSerializer(serializers.ModelSerializer):

    created_by = serializers.ReadOnlyField(source="created_by.username")

    class Meta:
        fields = "__all__"
        model = Task


class ProjectsSerializer(serializers.ModelSerializer):

    created_by = serializers.ReadOnlyField(source="created_by.username")
    shared_with = UserSerializer(many=True, required=False)
    tasks = TasksSerializer(many=True, required=False)

    class Meta:
        fields = "__all__"
        model = Project
