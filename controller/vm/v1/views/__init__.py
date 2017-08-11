from rest_framework import status
from rest_framework.views import APIView

from vm.exceptions import InvalidParamsException
from vm.exceptions import V1Exception

class BaseView(APIView):
    serializer_class = None

    def validate_query_params(self, request):
        serializer = self.serializer_class(data=request.POST)
        try:
            if not serializer.is_valid():
                raise InvalidParamsException()
            return serializer
        except Exception as ex:
            print(ex)
            raise V1Exception("Error")
