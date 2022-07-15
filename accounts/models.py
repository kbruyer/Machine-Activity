from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    shift = models.PositiveIntegerField(null=True, blank=True)
    badge = models.TextField(null=True, blank=True)
