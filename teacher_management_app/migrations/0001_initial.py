# Generated by Django 4.2.5 on 2023-09-28 13:05

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Teacher",
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
                (
                    "first_name",
                    models.CharField(max_length=50),
                ),
                (
                    "surname",
                    models.CharField(max_length=50),
                ),
                ("age", models.IntegerField()),
                (
                    "subject",
                    models.CharField(max_length=100),
                ),
            ],
        ),
    ]
