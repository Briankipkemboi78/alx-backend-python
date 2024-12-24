from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow the owner of a message or conversation to edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        # Allow read-only methods
        if request.method in permissions.SAFE_METHODS:
            return True

        # Allow only the owner to edit or delete
        return obj.user == request.user