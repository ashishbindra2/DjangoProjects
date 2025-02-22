# Generated by Django 5.1.5 on 2025-02-03 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("testApp", "0002_testapp_gender_testapp_name_alter_testapp_id"),
    ]

    operations = [
        migrations.CreateModel(
            name="EmployeeModel",
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
                ("ename", models.CharField(max_length=100, null=True)),
                ("esal", models.FloatField(max_length=100000000, null=True)),
                ("ecity", models.CharField(max_length=100, null=True)),
                ("email", models.EmailField(max_length=100, unique=True)),
            ],
        ),
    ]
