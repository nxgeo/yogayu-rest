from rest_framework import serializers

from yogalevels.serializers import YogaLevelRelatedSerializer
from yogaposes.models import YogaPose


class YogaPoseSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(source="image", read_only=True)
    yoga_level = YogaLevelRelatedSerializer(read_only=True)
    user_has_done = serializers.SerializerMethodField()

    class Meta:
        model = YogaPose
        exclude = ["image"]
        read_only_fields = ["name", "description", "first_reward_points"]

    def get_user_has_done(self, obj):
        user = self.context["request"].user.yoga_user
        return user.has_done_yoga_pose(obj.id)


class YogaPoseRelatedSerializer(serializers.ModelSerializer):
    yoga_level = YogaLevelRelatedSerializer(read_only=True)

    class Meta:
        model = YogaPose
        fields = ["id", "name", "yoga_level"]
        read_only_fields = ["name"]
