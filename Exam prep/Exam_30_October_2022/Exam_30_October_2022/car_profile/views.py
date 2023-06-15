from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileCreateForm, ProfileEditForm
from ..car.models import Car


def profile_create(request):
    form = ProfileCreateForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('catalogue')

    context = {
        'form': form
    }

    return render(request, 'car_profile/profile-create.html', context=context)


def profile_details(request):
    cars = Car.objects.all()
    total_price = sum(car.price for car in cars)
    context = {
        'total_price': total_price
    }

    return render(request, 'car_profile/profile-details.html', context=context)


def profile_edit(request):
    profile = Profile.objects.first()
    form = ProfileEditForm(request.POST or None, instance=profile)
    if form.is_valid():
        form.save()
        return redirect('profile-details')

    context = {
        'form': form
    }

    return render(request, 'car_profile/profile-edit.html', context=context)


def profile_delete(request):
    if request.method == 'POST':
        Car.objects.all().delete()
        Profile.objects.first().delete()
        return redirect('index')
    return render(request, 'car_profile/profile-delete.html')
