from django.db import models
from .Instance import Instance

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, db_index=True)

    class Meta:
        abstract = True

class InstanceGroup(BaseModel):
    instance = models.ForeignKey(Instance)
    instance_group_name = models.TextField(max_length=128, null=False)
    note = models.TextField(max_length=255, null=True)


    def __str__(self):
        return self.instance_group_name