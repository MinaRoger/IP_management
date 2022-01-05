from rest_framework import serializers


class IpDetailsSerializer(serializers.Serializer):
    ip = serializers.IPAddressField()
