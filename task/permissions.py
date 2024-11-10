from datetime import datetime

from rest_framework.permissions import BasePermission, SAFE_METHODS


class IsAuthenticatedOrReadOnly(BasePermission):
    """
    Custom permission to only allow authenticated users to edit it.
    """

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated


def IsOwnerOrReadOnly(BasePermission):
    """
    Разрешает редактирование объектов только их владельцам, остальным - только чтение.
    """

    def has_object_permission(self, request, view, obj):
        # Все пользователи могут просматривать
        if request.method in SAFE_METHODS:
            return True
        # Только владелец может изменять объект
        return obj.owner == request.user


class IsAdminOrOwner(BasePermission):
    def has_object_permission(self, request, view, obj):
        # Все пользователи могут просматривать
        if request.method in ['GET', 'HEAD', 'OPTIONS']:
            return True
        # Только администратор или владелец может изменять объект
        return request.user.is_staff or obj.owner == request.user

    class IsWorkHour(BasePermission):
        def has_object_permission(self, request, view, obj):
            current_hour = datetime.now().hour
            # Допустим, рабочие часы с 9 до 18
            return 9 <= current_hour < 18
