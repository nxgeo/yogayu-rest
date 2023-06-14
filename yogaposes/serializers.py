from rest_framework import serializers

from yogalevels.serializers import YogaLevelRelatedSerializer
from yogaposes.models import YogaPose


class YogaPoseSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(source="image", read_only=True)
    yoga_level = YogaLevelRelatedSerializer(read_only=True)

    class Meta:
        model = YogaPose
        exclude = ["image"]
        read_only_fields = ["name", "description", "first_reward_points"]


class YogaPoseRelatedSerializer(serializers.ModelSerializer):
    yoga_level = YogaLevelRelatedSerializer(read_only=True)

    class Meta:
        model = YogaPose
        fields = ["id", "name", "yoga_level"]
        read_only_fields = ["name"]
