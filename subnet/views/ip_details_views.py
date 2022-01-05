from rest_framework import generics
from rest_framework.response import Response

from subnet.models import ReservedIp
from subnet.serializers import IpDetailsSerializer


class IpDetailsView(generics.GenericAPIView):
    """This end point is used to retrieve given ip details."""

    queryset = ReservedIp.objects.all()
    serializer_class = IpDetailsSerializer
    permission_classes = []
    authentication_classes = []

    def get(self, request):
        serializer = self.serializer_class(data=request.query_params)
        serializer.is_valid(raise_exception=True)
        reserved_ip = ReservedIp.objects.filter(ip=serializer.validated_data['ip'])
        is_used = reserved_ip.exists()
        parent = ""
        if is_used:
            parent = reserved_ip.first().subnet.name
        return Response({"is_used": is_used, "parent": parent})
