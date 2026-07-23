import os
import random
import uuid

from django.db import models
from django.core.exceptions import ValidationError

from PIL import Image
from pillow_heif import register_heif_opener


# HEIC va HEIF formatlarini Pillow uchun yoqamiz
register_heif_opener()


def validate_image_extension(value):

    allowed_extensions = [
        ".jpg",
        ".jpeg",
        ".png",
        ".webp",
        ".heic",
        ".heif",
    ]

    extension = os.path.splitext(
        value.name
    )[1].lower()

    if extension not in allowed_extensions:

        raise ValidationError(
            "Only JPG, JPEG, PNG, WEBP, HEIC and HEIF images are allowed."
        )


def menu_image_upload_path(instance, filename):

    unique_name = uuid.uuid4().hex

    return f"menu/{unique_name}.webp"


class MenuCategory(models.Model):

    name = models.CharField(
        max_length=100
    )

    class Meta:

        verbose_name = "Kategoriya"

        verbose_name_plural = "Kategoriyalar"

    def __str__(self):

        return self.name


class MenuItem(models.Model):

    category = models.ForeignKey(
        MenuCategory,
        on_delete=models.CASCADE,
        related_name="menu_items"
    )

    name = models.CharField(
        max_length=200
    )

    description = models.TextField()

    image = models.FileField(
        upload_to=menu_image_upload_path,
        validators=[
            validate_image_extension
        ]
    )

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    class Meta:

        verbose_name = "Taom"

        verbose_name_plural = "Taomlar"

    def __str__(self):

        return self.name

category = models.ForeignKey(
    MenuCategory,
    on_delete=models.CASCADE,
    related_name="menu_items",
    verbose_name="Kategoriya"
)

name = models.CharField(
    "Nomi",
    max_length=200
)

description = models.TextField(
    "Tavsif"
)

image = models.FileField(
    "Rasm",
    upload_to=menu_image_upload_path,
    validators=[
        validate_image_extension
    ]
)

price = models.DecimalField(
    "Narxi",
    max_digits=10,
    decimal_places=2
)