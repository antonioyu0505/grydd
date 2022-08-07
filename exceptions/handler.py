import logging
from rest_framework.views import exception_handler
from .models import UnauthorizedAccess

def custom_exception_handler(exc, context):
    # Call REST framework's default exception handler first,
    # to get the standard error response.
    response = exception_handler(exc, context)

    # Now add the HTTP status code to the response.
    if isinstance(exc, UnauthorizedAccess):
        logging.error(f"Original error detail and callstack: {exc}")
        # TODO: Send email to administrator
        
    return response