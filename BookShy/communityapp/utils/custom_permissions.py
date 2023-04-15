from rest_framework.permissions import BasePermission

class CanEditField(BasePermission):
    """
    Custom permission class to allow only users with permission to edit a particular field to edit it.
    """
    def has_object_permission(self, request, view, obj):
        # Check if the field being updated is allowed to be edited by the user
        return obj.creator == request.user or request.user in obj.admins