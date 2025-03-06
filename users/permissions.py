from rest_framework.permissions import BasePermission,SAFE_METHODS

class IsVendor(BasePermission):
    """
    Custom permission to allow only vendors to create or manage products.
    """

    def has_permission(self, request, view):
        return request.user and request.user.is_authenticated and request.user.is_vendor

class IsOwnerOrReadOnly(BasePermission):
    """
    Custom permission to only allow owners of an object to edit or delete it.
    """
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return obj.user == request.user  # Only the owner can modify/delete

