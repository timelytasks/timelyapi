from app.projects.apps import ProjectsConfig
from unittest.mock import MagicMock
from django.test import TestCase
from django.apps import apps
from datetime import datetime
from app.projects.views import ProjectViewSet, TaskViewSet
from app.projects.models import Task
from app.projects.models import Project
from django.contrib.auth.models import User
from rest_framework.test import APIClient, APIRequestFactory, force_authenticate
from rest_framework.reverse import reverse


class ProjectTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="user", password="@user123")
        self.project = Project.objects.create(title="Project 1", created_by=self.user)

    def test_apps(self):
        self.assertEqual(ProjectsConfig.name, "projects")
        self.assertEqual(apps.get_app_config("projects").name, "app.projects")

    def test_project_str_(self):
        """
        Tests if project's __str__ returns it's title
        """
        project = Project.objects.get(title="Project 1")
        self.assertEqual(str(project), "Project 1")

    # models.py
    def test_project_attribute(self):
        """
        Test all project's attributes
        """
        project = Project.objects.get(title="Project 1")
        attributes = [
            "_state",
            "id",
            "title",
            "description",
            "created_at",
            "due_date",
            "created_by_id",
            "value_currency",
            "value",
            "initial_value_currency",
            "initial_value",
            "completed",
            "type_of_project",
        ]
        for att in attributes:
            self.assertIn(att, list(vars(project)))

    # def test_project_viewset_get(self):
    #     factory = APIRequestFactory()
    #     view = ProjectViewSet.as_view(actions={"get": "retrieve"})
    #     project = Project(title="test1", created_by=self.user)
    #     project.save()

    #     request = factory.get(reverse("projects-list", args=(project.pk,)))
    #     force_authenticate(request, user=self.user)
    #     test = view(request)
    #     self.assertEqual(test.status_code, 200)


class TasksTest(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="user", password="@user123")
        self.project = Project.objects.create(
            title="Project example", created_by=self.user, value=0
        )
        Task.objects.create(
            title="Task 1",
            description="Example task",
            created_by=self.user,
            project=self.project,
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
            "created_at",
            "completed",
            "created_by_id",
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

    def test_task_updates_project_value(self):
        """
        Tests if whenever task created, updated or deleted has monetary value, it reflects on project
        """
        self.assertEqual(self.project.value.amount, 0)
        Task.objects.create(
            title="Value 10",
            description="Test value",
            created_by=self.user,
            project=self.project,
            value=10,
        )
        self.assertEqual(self.project.value.amount, 10)
