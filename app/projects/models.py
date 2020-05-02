from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from djmoney.models.fields import MoneyField


class Project(models.Model):

    title = models.CharField(max_length=200, null=False)
    description = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True, null=False)
    due_date = models.DateTimeField(null=True)
    creator = models.ForeignKey(
        "auth.User", related_name="projects", on_delete=models.CASCADE
    )
    # shared_with = models.ManyToManyField("auth.User", blank=True)
    value = MoneyField(
        max_digits=10, decimal_places=2, default_currency=settings.CURRENCY, null=True
    )
    initial_value = MoneyField(
        max_digits=10, decimal_places=2, default_currency=settings.CURRENCY, null=True
    )
    # tasks = models.ManyToManyField("tasks.Task", blank=True)
    completed = models.BooleanField(default=False, null=False)

    TASK = 1
    BUDGET = 2
    DIARY = 3

    class TypeOfProject(models.TextChoices):
        TASK = "TK", _("Task project")
        FINANCE = "FN", _("Finance project")
        DIARY = "DR", _("Diary project")

    type_of_project = models.CharField(
        max_length=2, choices=TypeOfProject.choices, default=TypeOfProject.TASK
    )

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return self.title


class Task(models.Model):

    title = models.CharField(max_length=200, null=False)
    description = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True, null=False)
    due_date = models.DateTimeField(null=True)
    creator = models.ForeignKey(
        "auth.User", related_name="creator", on_delete=models.CASCADE
    )
    shared_with = models.ManyToManyField("auth.User", blank=True)
    project = models.ForeignKey(
        "projects.Project", related_name="project", on_delete=models.CASCADE, null=True
    )
    value = MoneyField(
        max_digits=10, decimal_places=2, default_currency=settings.CURRENCY, null=True
    )
    completed = models.BooleanField(default=False, null=False)

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return self.title
