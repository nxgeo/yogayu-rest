# Generated by Django 4.2.2 on 2023-06-14 15:35

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("yogaposes", "0001_initial"),
        ("yogahistories", "0001_initial"),
        ("users", "0002_yogauser"),
    ]

    operations = [
        migrations.AddField(
            model_name="yogauser",
            name="yoga_poses",
            field=models.ManyToManyField(
                through="yogahistories.YogaHistory", to="yogaposes.yogapose"
            ),
        ),
    ]
