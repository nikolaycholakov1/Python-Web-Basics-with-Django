from django import forms
from .models import Person


class PersonForm(forms.Form):
    your_name = forms.CharField(
        label='Your name: ',
        max_length=30,
        help_text='Your name',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'John doe',
                'class': 'form-control',

            }
        ),

    )
    age = forms.IntegerField(
        label='Your Age: ',
        help_text='Your age',
        initial=18,
    )

    # HOBBY_CHOICES = (
    #     (1, 'Football'),
    #     (2, 'basketball'),
    #     (3, 'baseball'),
    # )
    #
    # hobby = forms.CharField(
    #     widget=forms.RadioSelect(
    #         choices=HOBBY_CHOICES,
    #     )
    # )
