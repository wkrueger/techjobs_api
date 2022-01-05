from django.db import models

from techjobs_app.models.timestamp_mixin import TimestampMixin

TAG_TYPES_CHOICES = [
    ("CONTRACT_TYPE", "Tipo de contratação"),
    ("EXPERIENCE", "Experiência"),
    ("WORK_LOCATION", "Local de Trabalho"),
    ("TECHNOLOGY", "Tecnologia"),
    ("ROLE", "Tipo de Cargo"),
    ("OTHER", "Outras tags"),
]


class JobTagModel(TimestampMixin):
    name = models.CharField(max_length=255, unique=True)
    type = models.CharField(max_length=64, choices=TAG_TYPES_CHOICES)

    # um guest pode entrar com novas tags mas estas só valerão para aquela vaga,
    # não aparecendo como opção predefinida nos próximos forms
    show_in_options = models.BooleanField(default=False)
