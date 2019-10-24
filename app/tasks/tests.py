from django.test import TestCase
from app.tasks.models import Task


# Create your tests here.
class TaskTest(TestCase):
    def setUp(self):
        Task.objects.create(title="Task 1", description="Example task")

    def test_task_attribute(self):
        task = Task.objects.get(title="Task 1")
        attributes = ["_state", "id", "title", "description", "created", "completed"]
        for att in attributes:
            self.assertIn(att, list(vars(task)))
        self.assertEqual(task.description, "Example task")
