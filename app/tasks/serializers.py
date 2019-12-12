from rest_framework import serializers
from app.tasks.models import Task


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
