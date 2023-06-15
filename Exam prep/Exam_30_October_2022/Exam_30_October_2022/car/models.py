from django.core import validators
from django.db import models

from Exam_30_October_2022.car.validators import valid_car_year


class Car(models.Model):
    CHOICES = (
        ('Sports Car', 'Sports Car'),
        ('Pickup', 'Pickup'),
        ('Crossover', 'Crossover'),
        ('Minibus', 'Minibus'),
        ('Other', 'Other'),
    )

    TYPE_MAX_LEN = 10
    MODEL_MAX_LEN = 20
    MODEL_MIN_LEN = 2

    car_type = models.CharField(
        max_length=TYPE_MAX_LEN,
        null=False,
        blank=False,
        choices=CHOICES,
    )

    car_model = models.CharField(
        max_length=MODEL_MAX_LEN,
        validators=[validators.MinLengthValidator(MODEL_MIN_LEN)],
        null=False,
        blank=False,
    )

    year = models.IntegerField(
        null=False,
        blank=False,
        validators=[valid_car_year],
    )

    imageUrl = models.URLField(
        null=False,
        blank=False,
    )

    price = models.FloatField(
        null=False,
        blank=False,
        validators=[validators.MinValueValidator(2)],
    )
