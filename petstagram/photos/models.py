# photos/models.py
from django.core.validators import MinLengthValidator
from django.db import models

from petstagram.pets.models import Pet
from petstagram.photos.validators import validate_file_less_than_5mb


# Create your models here.
class Photo(models.Model):
    MIN_DESCRIPTION_LENGTH = 10
    MAX_DESCRIPTION_LENGTH = 300

    MAX_LOCATION_LENGTH = 30

    # Requires media files to work correctly
    photo = models.ImageField(
        upload_to='mediafiles/pet_photos',
        null=False,
        blank=True,
        validators=(validate_file_less_than_5mb,),
    )

    description = models.CharField(
        # DB validation
        max_length=MAX_DESCRIPTION_LENGTH,
        # Django/python validation, not DB validation
        validators=(
            MinLengthValidator(MIN_DESCRIPTION_LENGTH),
        ),
        null=True,
        blank=True,
    )

    location = models.CharField(
        max_length=MAX_LOCATION_LENGTH,
        null=True,
        blank=True,
    )

    publication_date = models.DateTimeField(
        # Automatically sets current date on 'save' (update or create)
        auto_now_add=True,
        null=False,
        blank=True,
    )

    # One-to-one relations

    # One-to-many relations

    # Many-to-many relations
    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True,
    )
