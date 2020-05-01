from rest_framework import permissions


# please read the message_for_reviewer in BASE_DIR
class IsAdminOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.method in permissions.SAFE_METHODS:
            return True
        return bool(request.user and request.user.is_staff)


class IsAdminorMe(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            if request.path == '/api/v1/users/me/':
                return True
            return bool(request.user.is_staff or request.user.role == 'admin')