from django.contrib.auth.models import Permission
from django.db import models
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from django.utils.translation import gettext_lazy as _

from .base import BaseModel


class RoleManager(models.Manager):

    use_in_migrations = True

    def get_by_natural_key(self, name):
        return self.get(name=name)


class Role(MPTTModel, BaseModel):
    name = models.CharField(_('name'), max_length=150, unique=True)
    desc = models.CharField(max_length=255, null=True, blank=True)
    parent = TreeForeignKey('self', on_delete=models.PROTECT, null=True, blank=True, related_name=_('children'))

    permissions = models.ManyToManyField(
        Permission,
        verbose_name=_('permissions'),
        blank=True,
    )

    objects = RoleManager()

    REQUIRED_FIELDS = []

    class MPTTMeta:
        order_insertion_by = ['id']

    class Meta:
        db_table = 'sys_role'
        verbose_name = _('role')
        verbose_name_plural = _('roles')

    def __str__(self):
        return self.name

