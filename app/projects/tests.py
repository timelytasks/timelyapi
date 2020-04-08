from app.projects.apps import ProjectsConfig
from unittest.mock import MagicMock
from django.test import TestCase
from django.apps import apps
from app.projects.apps import TasksConfig
from app.projects.views import TaskViewSet
from app.projects.models import Task
from app.projects.models import Project
from django.contrib.auth.models import User


class ProjectTest(TestCase):
    def test_apps(self):
        self.assertEqual(ProjectsConfig.name, "projects")
        self.assertEqual(apps.get_app_config("projects").name, "app.projects")


class TasksTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user("user")
        self.project = Project.objects.create(title="Project example", creator=user)
        Task.objects.create(
            title="Task 1", description="Example task", creator=user, project=project
        )

    # models.py
    def test_task_attribute(self):
        """
        Test all task's attributes
        """
        task = Task.objects.get(title="Task 1")
        attributes = [
            "_state",
            "id",
            "title",
            "description",
            "created",
            "completed",
            "creator_id",
        ]
        for att in attributes:
            self.assertIn(att, list(vars(task)))
        self.assertEqual(task.description, "Example task")

    # models.py
    def test_task_str_(self):
        """
        Tests if task's __str__ returns it's title
        """
        task = Task.objects.get(title="Task 1")
        self.assertEqual(str(task), "Task 1")

    # apps.py
    def test_apps(self):
        """
        Tests tasks app for bettter code coverage I guess...
        This test does nothing but improve code coverage.
        """
        self.assertEqual(TasksConfig.name, "tasks")
        self.assertEqual(apps.get_app_config("tasks").name, "app.tasks")

    def test_task_permissions(self):
        """
        Tests if permissions are granted correctly
        """
        new_user = User.objects.create_user("new_user")
        self.assertEqual()
        
    # def test_queryset_returns_task_created_by_user(self):
    # user = User.objects.get(username="user")
    # request = MagicMock()
    # request.user.return_value = user
    # print(request.user, user, type(user))
    # self.assertEqual(TaskViewSet.get_queryset(request), True)
