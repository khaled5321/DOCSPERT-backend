from rest_framework.permissions import BasePermission, SAFE_METHODS


class AuthorPermission(BasePermission):
    """
    Authors should be able to view and read books, and edit their own books and pages
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.is_author:
            return True

    def has_object_permission(self, request, view, obj):
        if obj.author != request.user:
            return False

        return True


class ReaderPermission(BasePermission):
    """
    Readers should only be able to view and read books
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.method in SAFE_METHODS:
            return True
