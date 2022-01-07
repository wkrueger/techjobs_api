from techjobs_app.models.job_model import JobModel
from .timestamp_mixin import TimestampMixin
from django.db import models
from .user_model import UserModel


class JobCommentModel(TimestampMixin):
    job = models.ForeignKey(JobModel, on_delete=models.CASCADE)
    created_by = models.ForeignKey(UserModel, on_delete=models.CASCADE)
    content = models.TextField()
