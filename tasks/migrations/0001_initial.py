# Generated by Django 5.0.13 on 2025-03-23 13:31

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Task",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=100)),
                (
                    "priority",
                    models.IntegerField(
                        choices=[
                            (1, "Highest priority"),
                            (2, "Medium priority"),
                            (3, "Lowest priority"),
                        ],
                        default=2,
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("due_date", models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
