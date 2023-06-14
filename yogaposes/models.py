from os.path import splitext

from django.db import models
from django.utils.text import slugify

from yogalevels.models import YogaLevel


def yoga_pose_image_folder(instance, filename):
    _, ext = splitext(filename)
    return f"yoga-pose/{slugify(instance.name)}{ext}"


class YogaPose(models.Model):
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(
        upload_to=yoga_pose_image_folder,
        max_length=70,
        blank=True,
        db_column="image_file_path",
    )
    first_reward_points = models.PositiveSmallIntegerField()
    yoga_level = models.ForeignKey(YogaLevel, on_delete=models.RESTRICT)

    class Meta:
        db_table = "yoga_pose"

    def __str__(self):
        return self.name
