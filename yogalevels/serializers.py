from rest_framework import serializers

from yogalevels.models import YogaLevel


class YogaLevelSerializer(serializers.ModelSerializer):
    image_url = serializers.ImageField(source="image", read_only=True)

    class Meta:
        model = YogaLevel
        exclude = ["image"]
        read_only_fields = ["name", "description", "minimum_points"]


class YogaLevelRelatedSerializer(serializers.ModelSerializer):
    class Meta:
        model = YogaLevel
        fields = ["id", "name"]
        read_only_fields = ["name"]
