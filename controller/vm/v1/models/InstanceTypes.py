from django.db import models

class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, db_index=True)

    class Meta:
        abstract = True

class InstanceTypes(BaseModel):
    # VM = "VM"
    # EC2 = "EC2"
    # AZURE = "AZURE"
    # GCL = "GCL"

    # TYPE_VM=(
    #     (VM, "Virturl Machine"),
    #     (EC2, "Amazon Web Service"),
    #     (AZURE, "Cloud Computing Platform"),
    #     (GCL, "Google Cloud Platform"),
    # )

    type_instances = models.CharField(max_length=16, null=True)
    type_instances_name = models.CharField(max_length=128, null=True)

    def to_dict(self):
        return {
            'id' : self.id,
            'type_instances' : self.type_instances,
            'type_instances_name' : self.type_instances_name,
            'created_date' : self.created_date,
            'modified_date' : self.modified_date,
            'is_active' : self.is_active,
        }