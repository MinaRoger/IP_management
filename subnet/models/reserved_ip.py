from django.db import models


class ReservedIp(models.Model):
    ip = models.GenericIPAddressField()
    name = models.CharField(max_length=100)
    subnet = models.ForeignKey("subnet.Subnet",
                               on_delete=models.CASCADE)

    def __str__(self):
        return self.ip
