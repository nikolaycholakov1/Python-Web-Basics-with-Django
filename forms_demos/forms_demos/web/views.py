from django.shortcuts import render

from forms_demos.web.forms import PersonForm
from forms_demos.web.models import Person


def index(request):
    name = None

    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['your_name']

            # can create model from cleaned data
            # 1.
            # Person.objects.create(**form.cleaned_data)

            # 2.
            # new_person_from_form = Person(
            #     name=form.cleaned_data['your_name'],
            #     age=form.cleaned_data['age']
            # )
            # new_person_from_form.save()

            # 3.
            Person.objects.create(
                name=form.cleaned_data['your_name'],
                age=form.cleaned_data['age']
            )

    else:  # GET...
        form = PersonForm()
        name = None

    context = {
        'form': form,
        'name': name,
    }

    return render(request, 'web/index.html', context=context)
