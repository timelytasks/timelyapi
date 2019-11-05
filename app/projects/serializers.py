from rest_framework import serializers
from app.projects.models import Project
from app.tasks.serializers import TasksSerializer
from app.users.serializers import UserSerializer


class ProjectsSerializer(serializers.ModelSerializer):

    creator = serializers.ReadOnlyField(source="creator.username")
    shared_with = UserSerializer(many=True)

    class Meta:
        fields = (
            "id",
            "title",
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
