from os.path import splitext

from django.db import models
from django.utils.text import slugify


def yoga_level_image_folder(instance, filename):
    _, ext = splitext(filename)
    return f"yoga-level/{slugify(instance.name)}{ext}"


class YogaLevel(models.Model):
    name = models.CharField(max_length=30, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to=yoga_level_image_folder,
        max_length=50,
        blank=True,
        db_column="image_file_path",
    )
    minimum_points = models.PositiveSmallIntegerField(unique=True)

    class Meta:
        db_table = "yoga_level"
        ordering = ["minimum_points"]

    def __str__(self):
        return self.name
