from rest_framework import serializers
from . import models


class TasksSerializer(serializers.HyperlinkedModelSerializer):

    creator = serializers.ReadOnlyField(source="creator.username")
    class Meta:
        fields = ("id", "title", "description", "creator","completed", "created", "url")
        model = models.Task
