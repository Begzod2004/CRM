# Generated by Django 4.1.5 on 2023-01-27 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("app", "0002_alter_hodim_stavka"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hodim",
            name="stavka",
            field=models.CharField(
                choices=[
                    ("0.25", "0.25"),
                    ("0.50", "0.50"),
                    ("0.75", "0.75"),
                    ("1", "1"),
                    ("1.5", "1.5"),
                ],
                max_length=123,
            ),
        ),
    ]
