from rest_framework import serializers


class BaseListSerializer(serializers.Serializer):
    page = serializers.IntegerField(min_value=1, default=1, required=False)
    limit = serializers.IntegerField(min_value=1, max_value=1000, required=False)
