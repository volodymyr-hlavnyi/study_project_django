from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthenticatedOrReadOnly(BasePermission):
    """
    Custom permission to only allow authenticated users to edit it.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated
