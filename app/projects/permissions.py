from rest_framework import permissions
import logging


class IsOwnerOrIsSharedWith(permissions.BasePermission):
    """
    Custom permission to only allow owners or people with
    shared permission of an object to edit it.
    """

    def has_object_permission(self, request, view, obj):
        # Write permissions for people who have a shared status
        if obj in request.user.project_set.all():
            return True

        # Write permissions are allowed to the owner of the snippet.
        return obj.creator == request.user
