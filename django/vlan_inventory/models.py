from django.db import models


class VLAN(models.Model):
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=256)

    def __str__(self):
        return "VLAN: " + self.name

    class Meta:
        managed = True
        db_table = 'VLAN'
