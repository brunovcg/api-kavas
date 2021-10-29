from rest_framework.permissions import BasePermission


class SpecificDeveloper(BasePermission):
    def has_permission(self, request, view):
        return request.user.username == 'davis'