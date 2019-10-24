from django.contrib.auth.models import User
from app.tasks.models import Task
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    tasks = serializers.PrimaryKeyRelatedField(many=True, queryset=Task.objects.all())

    class Meta:
        model = User
        fields = ['id', 'username', 'tasks']