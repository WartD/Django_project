# models.py

from django.db import models
from django.contrib.auth.models import User


class Details(models.Model):
    class Meta:
        verbose_name_plural = "Details"

    gender_choices = [
        ("Мужчина", "Мужчина"),
        ("Женщина", "Женщина"),
    ]

    activity_choices = [
        (
            "Сидячий (мало или отсутствует физическая активность)",
            "Сидячий (мало или отсутствует физическая активность)",
        ),
        (
            "Легкая активность (1-3 дня в неделю)",
            "Легкая активность (1-3 дня в неделю)",
        ),
        (
            "Умеренная активность (3-5 дней в неделю)",
            "Умеренная активность (3-5 дней в неделю)",
        ),
        ("Очень активный (6-7 дней в неделю)", "Очень активный (6-7 дней в неделю)"),
        ("Супер активный (два раза в день)", "Супер активный (два раза в день)"),
    ]

    number_of_days_choices = [
        (1, 1),
        (3, 3),
        (7, 7),
    ]

    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name="details", null=True
    )

    name = models.CharField(max_length=100, blank=True, null=True)
    gender = models.CharField(choices=gender_choices, max_length=100)
    weight = models.IntegerField(blank=True, null=True)
    height = models.IntegerField(blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    activity = models.CharField(
        choices=activity_choices, max_length=100, blank=True, null=True
    )
    number_of_days = models.IntegerField(
        choices=number_of_days_choices, blank=True, null=True
    )

    user_photo = models.ImageField(upload_to="user_photo", blank=True)

    def __str__(self):
        return "{0} {1}".format(self.user, self.name)
