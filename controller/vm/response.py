import json

from django.http import HttpResponse
from django.http import JsonResponse
from rest_framework import status
from rest_framework.decorators import renderer_classes
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response


@renderer_classes((JSONRenderer,))
def response_data(data=""):
    status_code = status.HTTP_200_OK
    result = {
        'status': status_code,
        'message': "Success",
        'data': data
    }
    return Response(result, status=status_code, content_type="application/json")

@renderer_classes((JSONRenderer,))
def response_message(message=""):
    status_code = status.HTTP_200_OK
    result = {
        'status': status_code,
        'message': message,
    }
    return Response(result, status=status_code, content_type="application/json")
