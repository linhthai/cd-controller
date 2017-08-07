from rest_framework import status
from rest_framework.views import APIView

class BaseView(APIView):
    serializer_class = None

    def validate_query_params(self, request):
        serializer = self.serializer_class(data=request.GET)
        if not serializer.is_valid():
            return None
        return serializer
