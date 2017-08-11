import json

from rest_framework.views import APIView

from vm.response import response_data_with_page, response_message
from vm.exceptions import V1Exception

from vm.v1.views import BaseView
from vm.v1.modules.instance_types import InstanceTypesFunction
from vm.v1.serializers.instance_types import InstanceTypeList, custom_serialize_instancetype, InstanceTypes 
# from vm.v1.models import InstanceTypes
from vm.v1.paging.instance_types import CustomInstanceTypesPaginator as Paging

class instancetypes_get(APIView):
    serializer_class = InstanceTypeList

    def get(self, request):
        # for key in request.GET:
        #     print(key)
        #     value = request.GET[key]
        #     print(value)
        try:
            page =request.GET.get('page')
        except Exception as ex:
            page = 1
        try:
            itf_driver = InstanceTypesFunction()
            data = itf_driver.get_all()
            if not data:
                return response_message("Data is empty !!!")
            paging = Paging()
            response_paging = paging.paginate_queryset(data, request)
            serializer = InstanceTypeList(response_paging, many=True)

            data_response = paging.get_data_response(serializer.data)
            return response_data_with_page(data_response)
        except Exception as ex:
            print(ex)
            raise V1Exception("Error")

class instancetypes_update(BaseView):
    serializer_class = InstanceTypeList

    def post(self, request):
        try:
            # serializer = self.validate_query_params(request)
            param = {
                    'id':                   request.POST.get('id'),
                    'type_instances':       request.POST.get('type_instances'),
                    'type_instances_name':  request.POST.get('type_instances_name'),
                    'created_date':         request.POST.get('created_date'),
                    'modified_date':        request.POST.get('modified_date'),
                    'is_active':            request.POST.get('is_active'),
                }
            if param['id']:
                itf_driver = InstanceTypesFunction()
                update_obj = itf_driver.update(**param)
                if update_obj:
                    serializer = InstanceTypeList(update_obj)
                    return response_data_with_page(serializer.data)
            return response_message("Success")
        except Exception as ex:
            print(ex)
            raise V1Exception("Error")

class instancetypes_create(BaseView):
    serializer_class = InstanceTypeList

    def post(self, request):
        try:
            param = {
                    'type_instances':       request.POST.get('type_instances'),
                    'type_instances_name':  request.POST.get('type_instances_name'),
                    'created_date':         request.POST.get('created_date'),
                    'modified_date':        request.POST.get('modified_date'),
                    'is_active':            request.POST.get('is_active'),
                }
            if param['type_instances']:
                itf_driver = InstanceTypesFunction()
                create_obj = itf_driver.create(**param)
                if create_obj:
                    serializer = InstanceTypeList(update_obj)
                    return response_data_with_page(serializer.data)
                return response_message("Success")
        except Exception as ex:
            print(ex)
            raise V1Exception("Error")