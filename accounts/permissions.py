from rest_framework import permissions


class AuthorPermission(permissions.BasePermission):
    """
    Authors should be able to view, read, and edit their own books and pages
    """

    def has_permission(self, request, view):
        pass

    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(request, view, obj)


class ReaderPermission(permissions.BasePermission):
    """
    Readers should only be able to view and read books
    """

    def has_permission(self, request, view):
        pass

    def has_object_permission(self, request, view, obj):
        return super().has_object_permission(request, view, obj)
