from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        if request.method in permissions.SAFE_METHODS:
            return True

        # The instance must have an ForeignKey to the user model named `owner`,
        # but we actually use `owner_id` to avoid the extra DB call to fetch the user object
        return obj.owner_id == request.user.pk
