from django.db import models
from techjobs_app.models.job_model import JobModel

from techjobs_app.models.timestamp_mixin import TimestampMixin

BROADCAST_TYPE_CHOICES = [("DISCORD", "Discord"), ("EMAIL", "Email")]


class BroadcastLogModel(TimestampMixin):
    type = models.CharField(
        "Modal de envio", max_length=32, choices=BROADCAST_TYPE_CHOICES
    )
    title = models.CharField("Título", max_length=255)
    content = models.TextField("Conteúdo")
    target = models.CharField("Alvos", max_length=255, null=True)
    related_job = models.ForeignKey(JobModel, null=True, on_delete=models.CASCADE)
