from rest_framework.permissions import BasePermission

class IsSeller(BasePermission):
    def has_permission(self, request, view):
        if request.user.groups.filter(name='seller').exists():
            return True
