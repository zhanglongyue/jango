from crum import get_current_user
from django.db import models


class BaseModel(models.Model):

    deleted = (
        (0, '未删除'),
        (1, '已删除'),
    )

    created_time = models.DateTimeField(auto_now_add=True)
    created_by = models.IntegerField(editable=False, blank=True, null=True)
    updated_time = models.DateTimeField(auto_now=True)
    updated_by = models.IntegerField(editable=False, blank=True, null=True)
    deleted = models.IntegerField(default=0, choices=deleted)

    class Meta:
        abstract = True

    def save(self, *args, **kwargs):
        user = get_current_user()
        if not self.pk:
            self.created_by = user.pk
        else:
            self.updated_by = user.pk
        super(BaseModel, self).save(*args, **kwargs)

