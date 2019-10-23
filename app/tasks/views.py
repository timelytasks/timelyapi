from django.shortcuts import render
from rest_framework import viewsets
from .models import Task
from .serializers import TasksSerializer


# Create your views here.
class TaskViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows tasks to be viewed or edited.
    """
    queryset = Task.objects.all().order_by('created')
    serializer_class = TasksSerializer
