from rest_framework.permissions import BasePermission, SAFE_METHODS


class AuthorPermission(BasePermission):
    """
    Authors should be able to view and read books, and edit their own books and pages
    """

    def has_permission(self, request, view):
        return request.user.is_author

    def has_object_permission(self, request, view, obj):
        # if request.user.is_authenticated and request.method in SAFE_METHODS:
        #     return True

        return obj.author == request.user


class ReaderPermission(BasePermission):
    """
    Readers should only be able to view and read books
    """

    def has_permission(self, request, view):
        return request.user.is_authenticated and request.method in SAFE_METHODS

    # def has_object_permission(self, request, view, obj):
    #     return super().has_object_permission(request, view, obj)
