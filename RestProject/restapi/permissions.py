from rest_framework import permissions

# class: IsOwnerOrAdmin
# Permite edicao de uma ocorrencia a um admin (staff) ou ao owner da mesma.

class IsOwnerOrAdmin(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.owner == request.user or request.user.is_staff
