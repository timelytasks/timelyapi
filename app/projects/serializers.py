from rest_framework import serializers
from app.projects.models import Project
from app.tasks.serializers import TasksSerializer


class ProjectsSerializer(serializers.ModelSerializer):

    creator = serializers.ReadOnlyField(source="creator.username")
    # tasks = TasksSerializer(required=False, many=True)

    class Meta:
        fields = (
            "id",
            "title",
            "description",
            "created",
            "tasks",
            "due_date",
            "creator",
            "shared_with",
            "value",
            "initial_value",
            "completed",
        )
        model = Project
