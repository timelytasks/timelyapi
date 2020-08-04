from django_filters import rest_framework as filters
from app.projects.models import Task


class TaskFilter(filters.FilterSet):
    class Meta:
        model = Task
        fields = {
            "title": ["exact"],
            "due_date": ["exact", "year__gt", "year__lt"],
            "value": ["exact", "lt", "gt"],
            "project": ["exact"],
            "completed": ["exact"],
            # 'price': ['lt', 'gt'],
            # 'release_date': ['exact', 'year__gt'],
        }
