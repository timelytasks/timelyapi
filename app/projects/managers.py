from django.db import models
from django.db.models import Q


class GenericManager(models.Manager):
    def owner_or_shared_with(self, user_id):
        return (
            self.filter(Q(created_by=user_id) | Q(shared_with=user_id))
            .distinct()
            .order_by("created_at")
        )
