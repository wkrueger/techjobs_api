from django.db import models

from techjobs_app.models.job_model import JOB_STATUS_CHOICES
from .timestamp_mixin import TimestampMixin
from .user_model import UserModel


class JobAuditModel(TimestampMixin):
    created_by = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    from_status = models.CharField(
        "Do status", max_length=32, choices=JOB_STATUS_CHOICES, null=True
    )
    to_status = models.CharField(
        "Para o status", max_length=32, choices=JOB_STATUS_CHOICES
    )
