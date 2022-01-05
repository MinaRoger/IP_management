from rest_framework import serializers

from subnet.models.reserved_ip import ReservedIp


class ReservedIpSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReservedIp
        fields = '__all__'

    # Check if ip is in range of subnet

    def validate(self, attrs):
        if attrs['ip'] == attrs['subnet'].network_id or attrs['ip'] == attrs['subnet'].broadcast_ip:
            raise serializers.ValidationError("You cant assign IP to reserved ips")
        if attrs['ip'] < attrs['subnet'].network_id or attrs['ip'] > attrs['subnet'].broadcast_ip:
            raise serializers.ValidationError("Invalid Ip")
        return attrs
