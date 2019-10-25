from django.test import TestCase
from django.apps import apps
from app.users.apps import UsersConfig


class UserTest(TestCase):
    def test_apps(self):
        self.assertEqual(UsersConfig.name, "users")
        self.assertEqual(apps.get_app_config("users").name, "app.users")
