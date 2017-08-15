from django.db import models
from .InstanceTypes import InstanceTypes

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, db_index=True)

    class Meta:
        abstract = True


class Instance(BaseModel):
    INS_STT_INIT = 1
    INS_STT_UP = 2
    INS_STT_DOWN = 4
    INSTANCE_STATUS = (
        (INS_STT_INIT, "INIT"),
        (INS_STT_UP, "UP"),
        (INS_STT_DOWN, "DOWN"),
    )

    instance_name = models.TextField(max_length=128, null=True)
    ip_address = models.IPAddressField(null=True)
    description = models.CharField(max_length=256, null=True)
    instance_type = models.ForeignKey(InstanceTypes)
    status = models.IntegerField(choices=INSTANCE_STATUS, default=INS_STT_INIT, null=True)

    class Meta:
        unique_together = ("ip_address", "instance_type")

    def __str__(self):
        return self.instance_name

    def to_dict(self):
        return {
            'id' : self.id,
            'instance_name' :   self.instance_name,
            'ip_address' :      self.ip_address,
            'description' :     self.description,
            'instance_type' :   self.instance_type,
            'status':           self.status,
            'created_date' :    self.created_date,
            'modified_date' :   self.modified_date,
            'is_active' :       self.is_active,
        }