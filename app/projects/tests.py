from app.projects.apps import ProjectsConfig
from unittest.mock import MagicMock
from django.test import TestCase
from django.apps import apps
from datetime import datetime
from app.projects.views import TaskViewSet
from app.projects.models import Task
from app.projects.models import Project
from django.contrib.auth.models import User
from rest_framework.test import APIClient


class ProjectTest(TestCase):
    def setUp(self):
        self.api = APIClient()
        self.user = User.objects.create_user(username="user", password="@user123")
        self.api.login(username="user", password="@user123")
        self.project = Project.objects.create(title="Project 1", creator=self.user)

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
            "created",
            "due_date",
            "creator_id",
            "value_currency",
            "value",
            "initial_value_currency",
            "initial_value",
            "completed",
            "type_of_project",
        ]
        for att in attributes:
            self.assertIn(att, list(vars(project)))

    def test_create_project_minimal(self):
        """
        Tests if project creation with minimal fields is working properly
        """
        project = {"title": "project"}
        response = self.api.post("/api/v1/projects/", project)
        self.assertEqual(response.status_code, 201)

    def test_create_project_maximum(self):
        """
        Tests if project creation with minimal fields is working properly
        """
        project = {
            "title": "project",
            "description": "p1",
            "due_date": datetime.now(),
            "value_currency": "BRL",
            "value": "10",
        }
        response = self.api.post("/api/v1/projects/", project)
        self.assertEqual(response.status_code, 201)


class TasksTest(TestCase):
    def setUp(self):
        self.api = APIClient()
        self.user = User.objects.create_user(username="user", password="@user123")
        self.api.login(username="user", password="@user123")
        self.project = Project.objects.create(
            title="Project example", creator=self.user
        )
        Task.objects.create(
            title="Task 1",
            description="Example task",
            creator=self.user,
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

    def test_tasks_not_visible_without_login(self):
        """
        Tests if tasks are unavailable for anonymous users
        """
        self.api.logout()
        response = self.api.get("/api/v1/tasks/")
        self.assertEqual(response.status_code, 403)

    def test_task_without_project(self):
        """
        Tests if task can be created without project
        """
        task = {"title": "task without project", "description": "No description"}
        response = self.api.post("/api/v1/tasks/", task)
        self.assertEqual(response.status_code, 201)
        for key, data in task.items():
            self.assertEqual(response.data.get(key), data)

    def test_task_not_visible_for_everyone(self):
        """
        Tests if task is invisible for unauthorized people
        """
        task = {"title": "task without project", "description": "No description"}
        self.api.post("/api/v1/tasks/", task)

        User.objects.create_user(username="anotheruser", password="@user123")
        self.api.logout()
        self.api.login(username="anotheruser", password="@user123")
        response = self.api.get("/api/v1/tasks/")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, [])

    def test_task_visible_for_shared_people(self):
        """
        Tests if task is visible for people that have access to it
        """
        user = User.objects.create_user(username="anotheruser", password="@user123")

        task = {
            "title": "task without project",
            "description": "No description",
            "shared_with": [user.pk],
        }
        self.api.post("/api/v1/tasks/", task)

        self.api.logout()
        self.api.login(username="anotheruser", password="@user123")
        response = self.api.get("/api/v1/tasks/")

        self.assertEqual(response.status_code, 200)
        response_task = response.data[0]
        for key, data in task.items():
            self.assertEqual(response_task.get(key), data)
