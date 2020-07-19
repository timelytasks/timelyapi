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


class ProjectEndpointsTest(TestCase):
    def setUp(self):
        self.api = APIClient()
        self.user = User.objects.create_user(username="user", password="@user123")
        self.api.login(username="user", password="@user123")
        self.project = Project.objects.create(title="Project 1", created_by=self.user)

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
            title="Project example", created_by=self.user, value=0
        )
        Task.objects.create(
            title="Task 1",
            description="Example task",
            created_by=self.user,
            project=self.project,
        )

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

    def test_task_create_adds_project_value(self):
        """
        Tests if whenever task created has monetary value, it reflects on project
        """
        self.project = Project.objects.get(id=self.project.id)
        self.assertEqual(self.project.value.amount, 0)
        task = {
            "title": "Value 10",
            "description": "No description",
            "created_by": self.user.id,
            "project": self.project.id,
            "value": 10,
        }
        self.api.post("/api/v1/tasks/", task)
        self.project = Project.objects.get(id=self.project.id)
        self.assertEqual(self.project.value.amount, 10)

    def test_task_update_adds_project_value(self):
        """
        Tests if whenever task gets updated, it's monetary value is reflects on project
        """
        self.project = Project.objects.get(id=self.project.id)
        self.assertEqual(self.project.value.amount, 0)
        task = {
            "title": "Value 10",
            "description": "No description",
            "created_by": self.user.id,
            "project": self.project.id,
            "value": 10,
        }
        created_data = self.api.post("/api/v1/tasks/", task)
        task_id = created_data.data["id"]
        self.project = Project.objects.get(id=self.project.id)
        self.assertEqual(self.project.value.amount, 10)

        task["value"] = 5
        created_data = self.api.patch(f"/api/v1/tasks/{task_id}/", task)
        self.project = Project.objects.get(id=self.project.id)
        self.assertEqual(self.project.value.amount, 5)
