from django.db import models
from .InstanceTypes import InstanceTypes

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, db_index=True)

    class Meta:
        abstract = True

class Instance(BaseModel):

    instance_name = models.TextField(max_length=128, null=True)
    ip_address = models.IPAddressField(null=True)
    hostname = models.CharField(max_length=64, null=True)
    instance_type = models.ForeignKey(InstanceTypes)


    def __str__(self):
        return self.instance_name
