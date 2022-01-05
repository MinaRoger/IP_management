from django.contrib import admin

from subnet.models import Subnet, ReservedIp

# Register your models here.

admin.site.register(ReservedIp)
admin.site.register(Subnet)
