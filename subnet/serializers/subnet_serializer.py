from django.db.models import Q
from rest_framework import serializers

from subnet.models.subnet import Subnet
from subnet.services import get_last_subnet_ip


class SubnetSerializer(serializers.ModelSerializer):
    utilization = serializers.ReadOnlyField()

    # Check if subnet will overlap on other subnet ip ranges.

    def validate(self, attrs):
        subnet_end_ip = get_last_subnet_ip(attrs['network_id'], attrs['mask'])
        if Subnet.objects.filter((Q(network_id__gte=attrs['network_id']) & Q(network_id__lte=subnet_end_ip)) |
                                 (Q(network_id__lte=attrs['network_id'], ip_end_range__gte=attrs['network_id'])) |
                                 (Q(network_id__lte=subnet_end_ip, ip_end_range__gte=subnet_end_ip))
                                 ).exists():
            raise serializers.ValidationError("Subnet with this range already exists")
        return attrs

    # CASES
    #  Subnet ->
    # 192.168.0.0    ---> 192.168.0.10 ##
    # 192.168.0.9   ---> 192.168.0.50  ##
    #
    #
    # 192.168.0.10    ---> 192.168.0.20
    # 192.168.0.9   ---> 192.168.0.50
    class Meta:
        model = Subnet
        fields = '__all__'


class VlanUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Subnet
        fields = ['vlan']
