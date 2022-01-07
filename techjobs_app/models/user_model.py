from django.contrib.auth.models import AbstractUser
from django.db import models


class UserModel(AbstractUser):
    gh_oauth_state = models.CharField(null=True, max_length=255)
    gh_oauth_code = models.CharField(null=True, max_length=255)
    gh_oauth_timestamp = models.DateTimeField(null=True)
