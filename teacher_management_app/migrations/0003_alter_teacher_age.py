# Generated by Django 4.2.5 on 2023-10-08 09:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        (
            "teacher_management_app",
            "0002_teacher_patronnymic",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="teacher",
            name="age",
            field=models.PositiveIntegerField(),
        ),
    ]
