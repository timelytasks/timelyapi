from rest_framework import serializers
from . import models


class TasksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        fields = (
            'id',
            'title',
            'description',
            'completed',
            'created',
            'url',
        )
        model = models.Task
