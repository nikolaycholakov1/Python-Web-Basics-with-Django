from django.core.exceptions import ValidationError

from forms_demo_part_2.web.models import Todo


def validate_max_todos(assignee):
    if assignee.todo_set.count() >= Todo.MAX_TODOS_COUNT_PER_PERSON:
        raise ValidationError(f'{assignee} already has max todos assigned')
