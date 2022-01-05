from django.urls import path

from subnet.views import SubnetListCreateView, SubnetUpdateVlanView, ReserveIpView, IpDetailsView

app_name = "subnet"

urlpatterns = [

    path('', SubnetListCreateView.as_view(), name='subnet'),
    path('<int:pk>', SubnetUpdateVlanView.as_view(), name='subnet_details'),
    path('reserve-ip', ReserveIpView.as_view(), name='reserve_ip'),
    path('ip-details', IpDetailsView.as_view(), name='ip_details')
]
