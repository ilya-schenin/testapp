from django.db import models
from django.contrib.auth.models import AbstractUser
from organization.models import Organization


class CustomUser(AbstractUser):
    phone = models.CharField(max_length=20, blank=True, null=True)
    organization = models.ForeignKey(Organization, on_delete=models.PROTECT, null=True, blank=True)

