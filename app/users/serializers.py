from django.contrib.auth.models import User
from app.tasks.models import Task
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "username", "first_name")
