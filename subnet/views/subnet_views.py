from rest_framework import generics

from subnet.models import Subnet
from subnet.serializers import SubnetSerializer, VlanUpdateSerializer


class SubnetListCreateView(generics.ListCreateAPIView):
    """
           get:
           This api is used to return a list of subnets.

           post:
           This api is used to post a new subnet.
    """

    queryset = Subnet.objects.all()
    authentication_classes = []
    permission_classes = []
    serializer_class = SubnetSerializer


class SubnetUpdateVlanView(generics.RetrieveUpdateDestroyAPIView):
    """
           get:
           This api is used to return a retrieve a subnet.

           put:
           This api is used to update/delete vlan id.

           delete:
           This api is used to delete subnet.

    """
    queryset = Subnet.objects.all()
    authentication_classes = []
    permission_classes = []

    def get_serializer_class(self):
        if self.request is None:
            return SubnetSerializer
        if self.request.method == "GET":
            return SubnetSerializer
        return VlanUpdateSerializer

    serializer_class = VlanUpdateSerializer
