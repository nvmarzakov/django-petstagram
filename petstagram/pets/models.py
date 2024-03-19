from django.db import models


# Create your models here.
class Pet(models.Model):
    MAX_NAME = 30

    name = models.CharField(
        max_length=MAX_NAME,
        blank=False,
        null=False,
    )

    personal_photo = models.URLField(
        blank=False,
        null=False,
    )

    slug = models.SlugField(
        unique=True,
        null=False,
        blank=False,
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )
