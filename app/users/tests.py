from django.test import TestCase
from django.apps import apps
from app.tasks.models import Task
from app.tasks.apps import TasksConfig
from django.contrib.auth.models import User

class TaskTest(TestCase):
    def setUp(self):
        admin = User.objects.create_user("admin")
        Task.objects.create(title="Task 1", description="Example task", creator=admin)

    def test_apps(self):
        self.assertEqual(TasksConfig.name, "tasks")
        self.assertEqual(apps.get_app_config("tasks").name, "app.tasks")

    def test_task_attribute(self):
        task = Task.objects.get(title="Task 1")
        attributes = ["_state", "id", "title", "description", "created", "completed"]
        for att in attributes:
            self.assertIn(att, list(vars(task)))
        self.assertEqual(task.description, "Example task")
