from django.db import models
from django.contrib.auth.models import AbstractUser


class BaseModel(models.Model):

    # active_status = models.BooleanField(default=True)
    # created_by = models.CharField(max_length=100, default='default-admin')
    created_at = models.DateField(auto_now_add=True, null=True, blank=True)
    # modified_by = models.CharField(max_length=50, default='default-admin')
    updated_at = models.DateField(auto_now_add=True, null=True, blank=True)

    class Meta:
        abstract = True

class Roles(BaseModel):
    role = models.CharField(max_length=100)

    def __str__(self):
        return self.role

class MyUser(AbstractUser, BaseModel):
    # role = models.ForeignKey(Roles, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.email}'
    