# Generated by Django 3.0.5 on 2020-06-11 19:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('projects', '0003_auto_20200506_1731'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='shared_with',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
