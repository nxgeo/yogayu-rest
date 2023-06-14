from django.db import transaction
from rest_framework import serializers

from yogahistories.models import YogaHistory
from yogalevels.models import YogaLevel
from yogaposes.models import YogaPose
from yogaposes.serializers import YogaPoseRelatedSerializer


class YogaPosePKField(serializers.PrimaryKeyRelatedField):
    def get_queryset(self):
        user = self.context["request"].user.yoga_user
        return YogaPose.objects.filter(
            yoga_level__minimum_points__lte=user.total_points
        )


class YogaHistorySerializer(serializers.ModelSerializer):
    user_id = serializers.PrimaryKeyRelatedField(read_only=True)
    yoga_pose_id = YogaPosePKField(write_only=True)
    yoga_pose = YogaPoseRelatedSerializer(read_only=True)

    class Meta:
        model = YogaHistory
        exclude = ["user"]
        read_only_fields = ["earned_points"]

    @transaction.atomic
    def create(self, validated_data):
        user = self.context["request"].user.yoga_user

        yoga_pose = validated_data["yoga_pose_id"]

        if user.has_done_yoga_pose(yoga_pose.id):
            earned_points = 0
        else:
            earned_points = yoga_pose.first_reward_points
            user.total_points += earned_points

            updated_user_yoga_level = YogaLevel.objects.filter(
                minimum_points__lte=user.total_points
            ).last()

            if user.yoga_level != updated_user_yoga_level:
                user.yoga_level = updated_user_yoga_level

            user.save()

        return YogaHistory.objects.create(
            user=user,
            yoga_pose=yoga_pose,
            earned_points=earned_points,
            completed_at=validated_data["completed_at"],
        )
