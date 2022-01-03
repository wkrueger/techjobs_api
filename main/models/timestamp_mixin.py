from django.db import models

# https://stackoverflow.com/questions/3429878/automatic-creation-date-for-django-model-form-objects
class TimestampMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True, db_index=True)

    class Meta:
        abstract = True
