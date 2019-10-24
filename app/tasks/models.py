from django.db import models


class Task(models.Model):

    title = models.CharField(max_length=200, null=False)
    description = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True, null=False)
    completed = models.BooleanField(default=False, null=False)
    creator = models.ForeignKey('auth.User', related_name='tasks', on_delete=models.CASCADE)

    class Meta:
        ordering = ["created"]

    def __str__(self):
        return self.title
