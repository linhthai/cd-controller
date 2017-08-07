from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.response import Response

class V1Exception(APIException):
    message = 'Error'
    status_code = status.HTTP_400_BAD_REQUEST

    def __init__(self, detail=None, response=None, status=None):
        if response is None:
            response = self.message
        self.response = response
        if detail is None:
            detail = self.message
        if status is None:
            status = self.status_code
        self.detail = detail
        self.status = status

    def __str__(self):
        return self.detail

    def __unicode__(self):
        return self.detail


class MissingParamsException(V1Exception):
    message = 'Missing param(s)'
    status_code = status.HTTP_400_BAD_REQUEST


class InvalidParamsException(V1Exception):
    message = 'Invalid param(s)'
    status_code = status.HTTP_400_BAD_REQUEST
