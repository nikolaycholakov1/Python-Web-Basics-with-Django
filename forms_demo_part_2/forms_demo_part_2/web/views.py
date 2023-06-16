from django.http import HttpResponse
from django.shortcuts import render, redirect

from forms_demo_part_2.web.forms import TodoCreateForm, PersonCreateForm
from forms_demo_part_2.web.models import Person


def index(request):
    if request.method == "GET":
        form = TodoCreateForm()
    else:
        form = TodoCreateForm(request.POST)

        if form.is_valid():
            form.save()
            return HttpResponse('All is valid')

    context = {
        'form': form,
    }

    return render(request, 'index.html', context=context)


def list_persons(request):
    context = {
        'persons': Person.objects.all(),
    }

    return render(request, 'list-persons.html', context=context)


def create_person(request):
    if request.method == "GET":
        form = PersonCreateForm()
    else:
        form = PersonCreateForm(request.POST, request.FILES)
        form.save()
        return redirect('list persons')

    context = {
        'form': form,
    }

    return render(request, 'create-person.html', context=context)
