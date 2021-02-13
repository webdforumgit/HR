from django.core.validators import validate_email
from django.core.exceptions import ValidationError
from rest_framework import permissions

class BlocklistPermission(permissions.BasePermission):
    """
    Global permission check for blocked IPs.
    """

    def has_permission(self, request, view):
        # print(request.headers)
        try:
            validate_email(request.headers.get('C-A-H'))
            return True
        except ValidationError:
            return  False

