from django import template

register = template.Library()


@register.filter(name='odd')
def show_only_odd(list_numbers):
    return [x for x in list_numbers if x % 2 == 1]
