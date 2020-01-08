from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from .base import BaseModel


class Organization(MPTTModel, BaseModel):
    name = models.CharField(max_length=150)
    desc = models.CharField(max_length=255, null=True, blank=True)
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children')

    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'sys_organization'

    class MPTTMeta:
        order_insertion_by = ['id']

    def __str__(self):
        return self.name
