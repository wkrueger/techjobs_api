from sqlalchemy import Column, String, Table, ForeignKey

from app.db.base_class import Base
from app.db_models.mixins.timestamp_mixin import TimestampMixin

JOB_SOURCE_CHOICES = [
    ("FORM", "Preenchimento do formulário"),
    ("TWITTER", "Bot do twitter"),
    ("OTHER", "Chamada da API por outros"),
]

JOB_STATUS_CHOICES = [
    ("IN_EVALUATION", "Em Avaliação"),
    ("CANCELLED", "Cancelada"),
    ("APPROVED", "Aprovada"),
    ("DISAPPROVED", "Reprovada"),
]

jobs_tags_table = Table('job_tag', Base.metadata,

    Column('job_id', ForeignKey())
)


class Job(Base, TimestampMixin):
    source = Column(String, length=32, nullable=False)
    title = Column(String, index=True, nullable=False)
    company_name = Column(String, nullable=False)
    recruiter_name = Column(String, nullable=False)
    recruiter_contact_info = Column(String, nullable=True)
    link = Column(String, length=2048, unique=True)
