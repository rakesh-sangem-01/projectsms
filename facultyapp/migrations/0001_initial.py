# Generated by Django 5.0.7 on 2024-10-17 08:55

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("adminapp", "0005_alter_feedback_name_alter_feedback_phonenumber_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="AddCourse",
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
                    "course",
                    models.CharField(
                        choices=[
                            ("OOP", "Object Oriented Programming"),
                            ("PFSD", "Python Full Stack Development With Django"),
                            ("DSS", "Data Science and Statistics"),
                            ("DAV", "Data Analytics and Visualization"),
                            ("RAIT", "Relational Algebra and Information Technology"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "section",
                    models.CharField(
                        choices=[
                            ("S11", "Section S11"),
                            ("S12", "Section S12"),
                            ("S13", "Section S13"),
                            ("S14", "Section S14"),
                            ("S15", "Section S15"),
                        ],
                        max_length=50,
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="adminapp.studentlist",
                    ),
                ),
            ],
        ),
    ]
