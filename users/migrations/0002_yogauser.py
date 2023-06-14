# Generated by Django 4.2.2 on 2023-06-14 10:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("yogalevels", "0001_initial"),
        ("users", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="YogaUser",
            fields=[
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        primary_key=True,
                        related_name="yoga_user",
                        serialize=False,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                ("total_points", models.PositiveSmallIntegerField(default=0)),
                (
                    "yoga_level",
                    models.ForeignKey(
                        default=1,
                        on_delete=django.db.models.deletion.RESTRICT,
                        to="yogalevels.yogalevel",
                    ),
                ),
            ],
            options={
                "db_table": "yoga_user",
            },
        ),
    ]
