from rest_framework import serializers
from app.projects.models import Project
from app.tasks.serializers import TasksSerializer
from app.users.serializers import UserSerializer


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
