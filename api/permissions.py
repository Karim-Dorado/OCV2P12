from rest_framework import permissions
from .models import Contract


class IsSaleEmployeeOrReadOnly(permissions.BasePermission):
    message = "Only a sale employee assigned to the client or a manager can make changes"

    def has_permission(self, request, view):
        if request.method == 'POST' and request.user.department == 'support':
            return False
        return True

    def has_object_permission(self, request, view, obj):

        if request.method in permissions.SAFE_METHODS:
            return True

        return (obj.sales_contact == request.user 
                or request.user.department == 'management'
                )


class IsSupportEmployeeOrReadOnly(permissions.BasePermission):
    message = "Only a sale/support employee assigned to the client or a manager can make changes"

    def has_permission(self, request, view):
        if request.method == 'POST' and request.user.department == 'support':
            return False
        return True

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            return True

        return (obj.support_contact == request.user 
                or obj.contract.client.sales_contact == request.user 
                or request.user.department == 'management'
                )
