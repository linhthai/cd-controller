from rest_framework import serializers

from vm.v1.serializers.base import BaseListSerializer
from vm.v1.models.InstanceTypes import InstanceTypes

class InstanceTypeList(serializers.ModelSerializer):
    created_date = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")
    modified_date = serializers.DateTimeField(format="%d-%m-%Y %H:%M:%S")

    class Meta:
        model = InstanceTypes
        fields = ('id', 'type_instances', 'created_date', 'modified_date', 'is_active')
