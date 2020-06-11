from django.db import models
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from djmoney.models.fields import MoneyField


class Project(models.Model):

    title = models.CharField(max_length=200, null=False)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    modified_at = models.DateTimeField(auto_now=True, null=False)

    due_date = models.DateTimeField(null=True)
    created_by = models.ForeignKey(
        "auth.User", related_name="created_project",on_delete=models.CASCADE
    )
    modified_by = models.ForeignKey(
        "auth.User", related_name="modified_project", on_delete=models.SET_NULL, null=True
    )
    shared_with = models.ManyToManyField("auth.User", blank=True)
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
        ordering = ["created_at"]

    def __str__(self):
        return self.title


class Task(models.Model):

    title = models.CharField(max_length=200, null=False)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=False)
    modified_at = models.DateTimeField(auto_now=True, null=False)
    due_date = models.DateTimeField(null=True)
    created_by = models.ForeignKey(
        "auth.User", related_name="created_task",on_delete=models.CASCADE
    )
    modified_by = models.ForeignKey(
        "auth.User", related_name="modified_task", on_delete=models.SET_NULL, null=True
    )
    shared_with = models.ManyToManyField("auth.User", blank=True)
    project = models.ForeignKey(
        "projects.Project", related_name="task", on_delete=models.CASCADE, null=True
    )
    value = MoneyField(
        max_digits=10, decimal_places=2, default_currency=settings.CURRENCY, null=True
    )
    completed = models.BooleanField(default=False, null=False)

    class Meta:
        ordering = ["created_at"]

    def __str__(self):
        return self.title
