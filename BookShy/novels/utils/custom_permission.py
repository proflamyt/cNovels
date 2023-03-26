from rest_framework import permissions


class CanReadBook(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.objects.get(user=request.user).can_read
        