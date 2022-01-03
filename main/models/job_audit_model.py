from django.db import models

from main.models.job_model import JOB_STATUS_CHOICES
from .timestamp_mixin import TimestampMixin
from django.contrib.auth.models import User


class JobAuditModel(TimestampMixin):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    from_status = models.CharField(
        "Do status", max_length=32, choices=JOB_STATUS_CHOICES, null=True
    )
    to_status = models.CharField(
        "Para o status", max_length=32, choices=JOB_STATUS_CHOICES
    )
