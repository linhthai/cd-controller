from rest_framework.views import APIView

from vm.v1.managers.instancetypes import InstanceTypesFunction
from vm.response import response_data, response_message
from vm.exceptions import V1Exception
from vm.v1.serializers.instance_type import InstanceTypeList

class instancetypes_get(APIView):
    serializer_class = InstanceTypeList

    def get(self, request):
        try:
            itf_driver = InstanceTypesFunction()
            data = itf_driver.get_all()
            if not data:
                return response_message("Data is empty !!!")
            response_serializer = InstanceTypeList(data, many=True)
            return response_data(response_serializer.data)
        except Exception as ex:
            print(ex)
            raise V1Exception("Error")
