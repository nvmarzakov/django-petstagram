from django.db import models
from django.template.defaultfilters import slugify


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
        blank=True,
    )

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f'{self.id}-{self.name}')

        return super().save(*args, **kwargs)
