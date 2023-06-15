from django.db import models
from django.core import validators


class Profile(models.Model):
    MAX_USERNAME_LEN = 10
    MIN_NAME_LEN = 2
    MIN_AGE = 18
    MAX_PASSWORD_LEN = 30
    MAX_FIRST_NAME_LEN = 30
    MAX_LAST_NAME_LEN = 30

    username = models.CharField(
        max_length=MAX_USERNAME_LEN,
        null=False,
        blank=False,
        validators=[
            validators.MinLengthValidator(
                MIN_NAME_LEN,
                f'The username must be a minimum of {MIN_NAME_LEN} chars'
            )
        ]
    )

    email = models.EmailField(
        null=False,
        blank=False,
    )

    age = models.PositiveIntegerField(
        null=False,
        blank=False,
        validators=[validators.MinValueValidator(18)],
    )

    password = models.CharField(
        max_length=MAX_PASSWORD_LEN,
        null=False,
        blank=False,
    )

    first_name = models.CharField(
        max_length=MAX_FIRST_NAME_LEN,
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=MAX_LAST_NAME_LEN,
        null=True,
        blank=True,
    )

    profile_picture = models.URLField(
        null=True,
        blank=False,
    )

    def get_name(self):
        if self.first_name and self.last_name:
            return f'{self.first_name} {self.last_name}'
        elif self.first_name:
            return self.first_name
        elif self.last_name:
            return self.last_name
        else:
            return ''
