# Generated by Django 4.2.5 on 2023-10-08 09:34

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("student_management_app", "0003_student_group"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="year",
            field=models.PositiveIntegerField(),
        ),
    ]