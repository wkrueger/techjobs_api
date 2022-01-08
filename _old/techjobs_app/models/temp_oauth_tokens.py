from techjobs_app.models.timestamp_mixin import TimestampMixin
from django.db import models


class TempOauthTokens(TimestampMixin):
    state = models.CharField(max_length=255, unique=True)
    code = models.CharField(max_length=255)
    token = models.CharField(max_length=255)
