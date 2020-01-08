from django.contrib.auth.models import Group
from django.db import models
from django.utils.translation import gettext_lazy as _
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

from system.models.role import Role
from .base import BaseModel


class Group(Group, MPTTModel, BaseModel):
    desc = models.CharField(max_length=255, null=True, blank=True)
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name=_('children'))

    roles = models.ManyToManyField(
        Role,
        verbose_name=_('roles'),
        blank=True,
    )

    class Meta:
        db_table = 'sys_group'
