from rest_framework.exceptions import PermissionDenied

class UnauthorizedAccess(PermissionDenied):
    default_detail = "You don't have the required permissions to access this site."
    default_code = "unauthorized_access"