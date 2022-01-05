from techjobs_app.models.job_model import JobModel
from .timestamp_mixin import TimestampMixin
from django.db import models
from django.contrib.auth.models import User


class JobCommentModel(TimestampMixin):
    job = models.ForeignKey(JobModel, on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
