from django.db import models

from users.models import YogaUser
from yogaposes.models import YogaPose


class YogaHistory(models.Model):
    user = models.ForeignKey(YogaUser, on_delete=models.CASCADE)
    yoga_pose = models.ForeignKey(YogaPose, on_delete=models.RESTRICT)
    earned_points = models.PositiveSmallIntegerField()
    completed_at = models.DateTimeField()

    class Meta:
        db_table = "yoga_history"
