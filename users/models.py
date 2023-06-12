from os.path import splitext
from uuid import uuid4

from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.db import models

from users.managers import UserManager


def profile_picture_folder(_, filename):
    _, ext = splitext(filename)
    return f"pfp/{uuid4()}{ext}"


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(unique=True)
    name = models.CharField(max_length=70)
    profile_picture = models.ImageField(
        upload_to=profile_picture_folder,
        max_length=50,
        blank=True,
        db_column="profile_picture_file_path",
    )
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    objects = UserManager()

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["name"]

    class Meta:
        db_table = "user"

    def __str__(self):
        return self.name
