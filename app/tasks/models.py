from django.db import models

class Task(models.Model):
    
    title = models.CharField(max_length=200, null=False)
    description = models.TextField(null=True)
    created = models.DateTimeField(auto_now_add=True, null=False)
    completed = models.BooleanField(default=False, null=False)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return self.title

