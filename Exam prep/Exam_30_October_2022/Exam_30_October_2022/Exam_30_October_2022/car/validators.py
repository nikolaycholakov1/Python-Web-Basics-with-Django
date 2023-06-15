from django.core.exceptions import ValidationError


def valid_car_year(value):
    min_valid_year = 1980
    max_valid_year = 2049

    if not min_valid_year <= value <= max_valid_year:
        raise ValidationError(
            f"Year must be between {min_valid_year} and {max_valid_year}"
        )
