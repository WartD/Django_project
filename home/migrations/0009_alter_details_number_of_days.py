# Generated by Django 4.2.7 on 2023-12-12 04:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0008_alter_details_number_of_days"),
    ]

    operations = [
        migrations.AlterField(
            model_name="details",
            name="number_of_days",
            field=models.ImageField(
                blank=True, choices=[(1, 1), (3, 3), (7, 7)], null=True, upload_to=""
            ),
        ),
    ]