from django.test import TestCase
from django.apps import apps
from app.users.apps import UsersConfig
from django.contrib.auth.models import User


class TaskTest(TestCase):
    # def setUp(self):
    #     admin = User.objects.create_user("admin")
    #     Task.objects.create(title="Task 1", description="Example task", creator=admin)

    def test_apps(self):
        self.assertEqual(UsersConfig.name, "users")
        self.assertEqual(apps.get_app_config("users").name, "app.users")
