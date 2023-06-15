from django import template
from Exam_30_October_2022.car_profile.models import Profile

register = template.Library()


@register.simple_tag
def get_user_profile():
    return Profile.objects.first()
