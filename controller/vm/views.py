from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import status
from rest_framework.views import APIView

from vm.response import response_message
from vm.exceptions import MissingParamsException
from vm.exceptions import V1Exception


# Create your views here.
class Test(APIView):
    def get(self, request):
        return response_message("Hello, world. You're at the polls index.")