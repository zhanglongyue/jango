from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.db import models

from system.models.organization import Organization


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=20, unique=True)
    nickname = models.CharField(max_length=32)
    phone = models.CharField(max_length=11, null=True, unique=True)
    email = models.CharField(max_length=320, null=True)
    avatar = models.ImageField(upload_to='avatar/', default="avatar/admin.jpg")
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    is_superuser = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)

    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, related_name='user')

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = 'sys_user'




