import datetime
import random

from django.shortcuts import render, redirect


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_age(self):
        return self.age


some_student = Student('Jon', 20)


def index(request):
    context = {
        'title': 'Home',
        'random_int': random.random(),
        'nested': {
            'second': 'second value',
        },
        'student': some_student.get_age(),
        'students': ['Kalin', 'Ivan', 'Pesho', 'Pesho', 'Mariya'],
        'students_second': [],
        'now': datetime.date.today(),
        'numbers': [1, 2, 3, 4, 5, 6, 7],
        'students_obj': [
            Student('Lili', 22),
            Student('Sasho', 15),
            Student('Ivan', 32),
        ],
        'logged_in': True,
    }

    return render(request, 'examples/partials/index.html', context=context)


def contact_view(request):
    return redirect('index')


def about_view(request):
    return render(request, 'examples/partials/about.html')
