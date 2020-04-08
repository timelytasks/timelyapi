from rest_framework import serializers
from app.projects.models import Project, Task
from app.users.serializers import UserSerializer
from rest_framework import serializers


class ProjectsSerializer(serializers.ModelSerializer):

    creator = serializers.ReadOnlyField(source="creator.username")
    shared_with = UserSerializer(many=True)
    type_of_project_name = serializers.CharField(source='get_type_of_project_display')

    class Meta:
        fields = (
            "id",
            "title",
            "type_of_project_name",
            "type_of_project",
            "description",
            "created",
            "due_date",
            "creator",
            "shared_with",
            "value",
            "initial_value",
            "completed",
        )
        model = Project


class TasksSerializer(serializers.ModelSerializer):

    creator = serializers.ReadOnlyField(source="creator.username")

    class Meta:
        fields = (
            "id",
            "title",
            "project",
            "description",
            "creator",
            "value",
            "shared_with",
            "completed",
            "created",
        )
        model = Task
