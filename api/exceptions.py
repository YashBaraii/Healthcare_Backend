from rest_framework.views import exception_handler
from rest_framework.response import Response
from rest_framework import status


def custom_exception_handler(exc, context):
    response = exception_handler(exc, context)

    if response is not None:
        custom_response_data = {
            "error": True,
            "status_code": response.status_code,
            "message": response.data,
        }
        return Response(custom_response_data, status=response.status_code)

    return response
