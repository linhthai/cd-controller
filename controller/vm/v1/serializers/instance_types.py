from rest_framework import serializers
from rest_framework import pagination

from django.db.models.query import QuerySet

from vm.v1.serializers.base import BaseListSerializer
from vm.v1.models.InstanceTypes import InstanceTypes


class InstanceTypeList(serializers.ModelSerializer):
    # type_instances = serializers.CharField(source='get_type_instances_display')
    created_date = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    modified_date = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")

    class Meta:
        model = InstanceTypes
        fields = ('id', 'type_instances', 'type_instances_name' , 'created_date', 'modified_date', 'is_active')


def custom_serialize_instancetype(obj_list):
    output = None
    try:
        if isinstance(obj_list, InstanceTypes) is True:
            output = obj_list.to_dict()
        elif isinstance(obj_list, QuerySet):
            output = []
            for e in obj_list:
                output.append(e.to_dict())
    except KeyError:
        pass
    except TypeError:
        pass
    return output
