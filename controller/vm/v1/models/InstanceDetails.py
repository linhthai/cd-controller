from django.db import models
from .Instance import Instance


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, db_index=True)

    class Meta:
        abstract = True

class InstanceDetails(BaseModel):

    instance = models.ForeignKey(Instance)
    mac_address = models.CharField(max_length=255, null=True)
    os = models.CharField(max_length=64, null=True)
    os_version = models.CharField(max_length=128, null=True)
    core_cpu = models.IntegerField(default=4 )
    total_memory = models.BigIntegerField(default=0)
    volume_size = models.BigIntegerField(default=0)

    class Meta:
        index_together = ['os', 'core_cpu']

    def __str__(self):
        return self.title

