from django.db.models.signals import post_save
from django.dispatch import receiver


@receiver(post_save, sender="subnet.Subnet")
def reserve_default_ips(sender, **kwargs):
    from subnet.models import Subnet, ReservedIp

    subnet: Subnet = kwargs.get("instance")
    created: bool = kwargs.get("created")

    if created:
        ReservedIp.objects.create(ip=subnet.network_id, name="Network IP", subnet=subnet)
        ReservedIp.objects.create(ip=subnet.ip_end_range, name="BroadCast IP", subnet=subnet)
