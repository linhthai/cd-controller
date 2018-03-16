from django.db import models


class BaseModel(models.Model):
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True, db_index=True)

    class Meta:
        abstract = True


class Projects(BaseModel):
    uuid = models.CharField(db_index=True, max_length=255)
    name = models.CharField(max_length=63, null=True)
    key = models.CharField(max_length=16, null=True, db_index=True)
    owner = models.CharField(max_length=63, null=True)
    description = models.TextField(max_length=255, null=True)
    is_private = models.BooleanField(default=True, db_index=True)

    class Meta:
        unique_together = ("uuid", "is_private")