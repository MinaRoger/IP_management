from rest_framework import generics

from subnet.models import ReservedIp
from subnet.serializers import ReservedIpSerializer


class ReserveIpView(generics.CreateAPIView):
    """This end point is used to reserve IP to a specific subnet."""

    queryset = ReservedIp.objects.all()
    serializer_class = ReservedIpSerializer
    permission_classes = []
    authentication_classes = []
