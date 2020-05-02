from rest_framework import serializers
from app.projects.models import Project, Task
from app.users.serializers import UserSerializer


class ProjectsSerializer(serializers.ModelSerializer):

    creator = serializers.ReadOnlyField(source="creator.username")
    shared_with = UserSerializer(many=True, required=False)

    class Meta:
        fields = "__all__"
        model = Project


class TasksSerializer(serializers.ModelSerializer):

    creator = serializers.ReadOnlyField(source="creator.username")

    class Meta:
        fields = "__all__"
        model = Task
