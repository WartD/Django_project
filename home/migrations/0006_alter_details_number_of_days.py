# Generated by Django 4.2.7 on 2023-12-12 04:02

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0005_details_number_of_days"),
    ]

    operations = [
        migrations.AlterField(
            model_name="details",
            name="number_of_days",
            field=models.CharField(
                blank=True,
                choices=[(1, "1 день"), (3, "3 дня"), (7, "7 дней")],
                max_length=100,
                null=True,
            ),
        ),
    ]
