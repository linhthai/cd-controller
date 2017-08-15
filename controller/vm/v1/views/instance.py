import json

from rest_framework.views import APIView

from vm.response import response_data_with_page, response_message
from vm.exceptions import V1Exception

from vm.v1.views import BaseView
from vm.v1.modules.instance import InstanceFunction
from vm.v1.serializers.instance import InstanceList, custom_serialize_instance 
from vm.v1.paging.instance import CustomInstancePaginator as Paging


class instance_get(APIView):
    def get(self, request):
        try:
            insf_driver = InstanceFunction()
            data = insf_driver.get()
            if not data:
                return response_message("Data is empty !!!")
            paging = Paging()
            response_paging = paging.paginate_queryset(data, request)
            serializer = InstanceList(response_paging, many=True)

            data_response = paging.get_data_response(serializer.data)
            return response_data_with_page(data_response)
        except Exception as ex:
            print(ex)
            raise V1Exception("Error")

class instance_create(BaseView):
    def post(self, request):
        try:
            param = {
                'instance_name':       request.POST.get('instance_name'),
                'ip_address':       request.POST.get('ip_address'),
                'description':       request.POST.get('description'),
                'instance_type':        request.POST.get('instance_type'),
                'status':               request.POST.get('status'),
                'created_date':         request.POST.get('created_date'),
                'modified_date':        request.POST.get('modified_date'),
                'is_active':            request.POST.get('is_active'),
            }
            if param['ip_address'] and param['instance_type']:
                insf_driver = InstanceFunction()
                create_obj = insf_driver.create(**param)
                if create_obj:
                    serializer = InstanceList(create_obj)
                    return response_data_with_page(serializer.data)
                return response_message("Success")
        except Exception as ex:
            print(ex)
            raise V1Exception("Error")