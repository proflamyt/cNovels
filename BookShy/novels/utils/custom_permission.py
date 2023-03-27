from rest_framework import permissions


class CanReadBook(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.can_read
        