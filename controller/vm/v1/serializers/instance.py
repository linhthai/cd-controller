from rest_framework import serializers
from rest_framework import pagination

from django.db.models.query import QuerySet

from vm.v1.serializers.base import BaseListSerializer
from vm.v1.models.Instance import Instance


class InstanceList(serializers.ModelSerializer):
    # type_instances = serializers.CharField(source='get_type_instances_display')
    created_date = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    modified_date = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")

    class Meta:
        model = Instance
        fields = ('id', 'instance_name', 'ip_address','instance_type', 'status','description', 'created_date', 'modified_date', 'is_active')


def custom_serialize_instance(obj_list):
    output = None
    try:
        if isinstance(obj_list, Instance) is True:
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
