from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError as DjangoValidationError
from django.db import IntegrityError
from rest_framework import serializers
from rest_framework.settings import api_settings

from users.models import User, YogaUser
from yogalevels.serializers import YogaLevelRelatedSerializer


class YogaUserSerializer(serializers.ModelSerializer):
    yoga_level = YogaLevelRelatedSerializer(read_only=True)

    class Meta:
        model = YogaUser
        fields = ["total_points", "yoga_level"]
        read_only_fields = ["total_points"]


class UserSerializer(serializers.ModelSerializer):
    profile_picture_url = serializers.ImageField(
        source="profile_picture", read_only=True
    )
    yoga_user = YogaUserSerializer(read_only=True)

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "name",
            "profile_picture",
            "profile_picture_url",
            "is_active",
            "created_at",
            "yoga_user",
        ]
        read_only_fields = ["is_active"]
        extra_kwargs = {"profile_picture": {"write_only": True}}

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        yoga_user_fields = ret.pop("yoga_user")
        ret.update(yoga_user_fields)
        return ret


class UserCreateSerializer(UserSerializer):
    password = serializers.CharField(
        max_length=128, write_only=True, style={"input_type": "password"}
    )
    re_password = serializers.CharField(
        max_length=128, write_only=True, style={"input_type": "password"}
    )

    class Meta(UserSerializer.Meta):
        fields = UserSerializer.Meta.fields + ["password", "re_password"]

    default_error_messages = {
        "password_mismatch": "The two password fields did not match.",
        "cannot_create_user": "Unable to create user account.",
    }

    def validate(self, data):
        password = data["password"]
        re_password = data.pop("re_password")

        user = User(**data)

        try:
            validate_password(password, user)
        except DjangoValidationError as e:
            serializer_error = serializers.as_serializer_error(e)
            raise serializers.ValidationError(
                {"password": serializer_error[api_settings.NON_FIELD_ERRORS_KEY]}
            )

        if password != re_password:
            self.fail("password_mismatch")

        return data

    def create(self, validated_data):
        try:
            user = User.objects.create_user(is_yoga_user=True, **validated_data)
        except IntegrityError:
            self.fail("cannot_create_user")

        return user


class UserPasswordChangeSerializer(serializers.Serializer):
    current_password = serializers.CharField(
        write_only=True, style={"input_type": "password"}
    )
    new_password = serializers.CharField(
        max_length=128, write_only=True, style={"input_type": "password"}
    )
    re_new_password = serializers.CharField(
        max_length=128, write_only=True, style={"input_type": "password"}
    )

    default_error_messages = {
        "current_password_incorrect": "Current password is incorrect.",
        "new_password_mismatch": "The two new password fields did not match.",
    }

    def validate_current_password(self, value):
        is_current_password_correct = self.instance.check_password(value)
        if not is_current_password_correct:
            self.fail("current_password_incorrect")
        return value

    def validate(self, data):
        new_password = data["new_password"]

        user = self.instance

        try:
            validate_password(new_password, user)
        except DjangoValidationError as e:
            serializer_error = serializers.as_serializer_error(e)
            raise serializers.ValidationError(
                {"new_password": serializer_error[api_settings.NON_FIELD_ERRORS_KEY]}
            )

        if new_password != data["re_new_password"]:
            self.fail("new_password_mismatch")

        return data

    def update(self, instance, validated_data):
        instance.set_password(validated_data["new_password"])
        instance.save()
        return instance
