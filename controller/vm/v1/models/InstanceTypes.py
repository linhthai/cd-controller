from django.db import models

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, db_index=True)

    class Meta:
        abstract = True

class InstanceTypes(BaseModel):
    VM = "VM"
    EC2 = "EC2"
    AZURE = "AZURE"
    GCL = "GCL"

    TYPE_VM=(
        (VM, "Virturl Machine"),
        (EC2, "Amazon Web Service"),
        (AZURE, "Cloud Computing Platform"),
        (GCL, "Google Cloud Platform"),
    )


    type_instances = models.CharField(max_length=16,choices=TYPE_VM, default=VM, null=True)
