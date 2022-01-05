from django.db import models
from techjobs_app.models.timestamp_mixin import TimestampMixin
from techjobs_app.models.job_tag_model import JobTagModel

JOB_STATUS_CHOICES = [
    ("IN_EVALUATION", "Em Avaliação"),
    ("CANCELLED", "Cancelada"),
    ("APPROVED", "Aprovada"),
    ("DISAPPROVED", "Reprovada"),
]

JOB_SOURCE_CHOICES = [
    ("FORM", "Preenchimento do formulário"),
    ("TWITTER", "Bot do twitter"),
    ("OTHER", "Chamada da API por outros"),
]


class JobModel(TimestampMixin):
    source = models.CharField("Origem", max_length=32, choices=JOB_SOURCE_CHOICES)
    title = models.CharField("Título", max_length=255)
    company_name = models.CharField("Nome da Empresa", max_length=255)
    recruiter_name = models.CharField("Nome Recrutador(a)", max_length=255)
    recruiter_contact_info = models.CharField(
        "Contato Recrutador(a)", max_length=255, blank=True
    )
    link = models.CharField("Link da vaga", max_length=2048, unique=True)
    tags = models.ManyToManyField(JobTagModel)
    salary_from = models.DecimalField(
        "Salário a partir de", max_digits=10, decimal_places=2
    )
    salary_to = models.DecimalField("Salário até", max_digits=10, decimal_places=2)
    current_status = models.CharField(
        "Status", max_length=32, choices=JOB_STATUS_CHOICES
    )
    location = models.CharField("Localidade", max_length=255, blank=True, db_index=True)

    # comments: defined on job_comment
