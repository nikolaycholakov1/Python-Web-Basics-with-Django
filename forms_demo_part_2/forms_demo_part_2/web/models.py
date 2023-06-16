from django.db import models

from forms_demo_part_2.web.validators import validate_text, ValueInRangeValidator


class Person(models.Model):
    MAX_NAME_LEN = 20

    name = models.CharField(
        max_length=MAX_NAME_LEN,
    )

    profile_image = models.ImageField(
        null=True,
        blank=True,
        upload_to='persons',
    )

    def __str__(self):
        return self.name


class Todo(models.Model):
    MAX_TODOS_COUNT_PER_PERSON = 3

    MAX_TEXT_LEN = 25
    text = models.CharField(
        max_length=MAX_TEXT_LEN,
        validators=(
            validate_text,
        ),
        null=False,
        blank=False,
    )

    priority = models.IntegerField(
        validators=(
            ValueInRangeValidator(1, 10),
        ),
        null=False,
        blank=False,
    )

    is_done = models.BooleanField(
        default=False,
        null=False,
        blank=False,
    )

    assignee = models.ForeignKey(
        Person,
        on_delete=models.RESTRICT,
    )
