from ipaddress import IPv4Address

from django.db import models

# Create your models here.
DEFAULT_RESERVED_IPS = 2  # Network IP - Broadcast IP
MAX_MASK_SIZE = 32


class Subnet(models.Model):
    name = models.CharField(max_length=40)
    mask = models.PositiveIntegerField()
    network_id = models.GenericIPAddressField()
    vlan_id = models.PositiveIntegerField(null=True, blank=True)
    ip_end_range = models.GenericIPAddressField(null=True, blank=True)

    def save(self, *args, **kwargs):
        self.ip_end_range = str(IPv4Address(str(self.network_id)) + (2 ** (MAX_MASK_SIZE - self.mask)) - 1)
        super(Subnet, self).save(*args, **kwargs)

    @property
    def number_of_ips(self):
        return 2 ** (MAX_MASK_SIZE - self.mask)

    @property
    def utilization(self):
        return (self.number_of_ips_reserved / (self.number_of_ips - DEFAULT_RESERVED_IPS)) * 100

    @property
    def number_of_ips_reserved(self):
        return self.reservedip_set.count()

    @property
    def broadcast_ip(self):
        return self.ip_end_range

    def __str__(self):
        return self.name
