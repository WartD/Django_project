# Generated by Django 4.2.7 on 2023-12-11 19:42

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0004_alter_details_activity_alter_details_age_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="details",
            name="number_of_days",
            field=models.CharField(
                blank=True,
                choices=[
                    ("1 день", "1 день"),
                    ("3 дня", "3 дня"),
                    ("7 дней", "7 дней"),
                ],
                max_length=100,
                null=True,
            ),
        ),
    ]
