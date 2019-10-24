from django.test import TestCase
from django.apps import apps
from app.projects.apps import ProjectsConfig


class ProjectTest(TestCase):

    def test_apps(self):
        self.assertEqual(ProjectsConfig.name, 'projects')
        self.assertEqual(apps.get_app_config('projects').name, 'app.projects')
