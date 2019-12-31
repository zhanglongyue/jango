from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel


class Organization(MPTTModel):
    name = models.CharField(max_length=20)
    desc = models.CharField(max_length=255, null=True, blank=True)
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name='children')
    deleted = models.IntegerField(default=0)
    maximum_users = models.IntegerField(null=True, blank=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'sys_organization'

    class MPTTMeta:
        order_insertion_by = ['id']

    def __str__(self):
        return self.name

