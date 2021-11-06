from rest_framework import permissions	


class IsOwnerOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request,
        # so we'll always allow GET, HEAD or OPTIONS requests.
        # print("&&&&&&&&&&&&&&&&&&&&&&&&&",request.user)
        print("HAS OBJECT PERMISION")
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions are only allowed to the owner of the snippet.
        return obj.owner == request.user

    def has_permission(self, request, view):
        print("HAS PERMISION")
        return super().has_permission(request, view)