from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile"""

    def has_object_permission(self, request, view, obj):
        """Check user if trying to edit their own profile"""
        # Check if a safe method (methods that don't make changes: ex: GET)
        if request.method in permissions.SAFE_METHODS:
            return True

        # Check the authenticated user matches de same id with the object to edit
        return obj.id == request.user.id
