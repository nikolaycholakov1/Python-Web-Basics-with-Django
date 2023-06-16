import uuid

from django import forms
from django.core.exceptions import ValidationError

from forms_demo_part_2.web.model_validators import validate_max_todos
from forms_demo_part_2.web.models import Todo, Person
from forms_demo_part_2.web.validators import validate_text, ValueInRangeValidator


class TodoForm(forms.Form):
    text = forms.CharField(
        validators=(
            validate_text,
        ),
    )
    is_done = forms.BooleanField(
        required=False,
    )
    priority = forms.IntegerField(
        validators=(
            ValueInRangeValidator(1, 10),
        ),
    )
    #
    # def clean_text(self):
    #     pass
    #
    # def clean_priority(self):
    #     pass
    #
    # def clean_is_done(self):
    #     pass


class TodoCreateForm(forms.ModelForm):
    class Meta:
        model = Todo
        fields = '__all__'

    def clean(self):
        return super().clean()

    def clean_text(self):
        return self.cleaned_data['text'].lower()

    def clean_assignee(self):
        assignee = self.cleaned_data['assignee']
        try:
            validate_max_todos(assignee)
        except ValidationError:
            assignee = Person.objects.get(name='Unassigned')

        return assignee


class PersonCreateForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

    def clean_profile_image(self):
        profile_image = self.cleaned_data['profile_image']
        profile_image.name = str(uuid.uuid4())
        return profile_image

    # def clean(self):
    #     super().clean()
    #     profile_image = self.cleaned_data['profile_image']
    #     profile_image.name = self.cleaned_data['name']
