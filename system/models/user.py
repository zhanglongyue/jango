from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin, Group
from django.db import models
from django.utils.translation import gettext_lazy as _

from system.models.base import BaseModel
from system.models.organization import Organization
from system.models.role import Role


class User(AbstractBaseUser, PermissionsMixin, BaseModel):
    username = models.CharField(max_length=20, unique=True)
    nickname = models.CharField(max_length=32)
    phone = models.CharField(max_length=11, null=True, unique=True)
    email = models.CharField(max_length=320, null=True)
    avatar = models.ImageField(upload_to='avatar/', default="avatar/admin.jpg")
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, related_name='user')

    roles = models.ManyToManyField(
        Role,
        verbose_name=_('roles'),
        blank=True,
        help_text=_(
            'Roles owned by this user.'
        ),
        related_name="user_set",
        related_query_name="user",
    )

    groups = models.ManyToManyField(
        Group,
        verbose_name=_('groups'),
        blank=True,
        help_text=_(
            'The groups this user belongs to. A user will get all permissions '
            'granted to each of their groups.'
        ),
        related_name="user_set",
        related_query_name="user",
    )

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'sys_user'
