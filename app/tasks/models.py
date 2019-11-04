from django.db import models
from django.conf import settings
from djmoney.models.fields import MoneyField
from app.projects.models import Project


class Task(models.Model):

    title = models.CharField(max_length=200, null=False)
    description = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True, null=False)
    due_date = models.DateTimeField(null=True)
    creator = models.ForeignKey(
        "auth.User", related_name="tasks", on_delete=models.CASCADE
    )
    shared_with = models.ManyToManyField("auth.User", blank=True)
    # project = models.ForeignKey(
    #     "projects.Project", related_name="project", on_delete=models.CASCADE
    # )
    value = MoneyField(
        max_digits=10, decimal_places=2, default_currency=settings.CURRENCY, null=True
    )
    completed = models.BooleanField(default=False, null=False)

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return self.title
