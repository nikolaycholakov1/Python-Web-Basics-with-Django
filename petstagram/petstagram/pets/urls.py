from django.urls import path, include
from .views import pet_add, pet_details, pet_edit, pet_delete

urlpatterns = [
    # /pets/
    path('add/', pet_add, name='pet add'),
    path('<str:username>/pet/<slug:pet_name>/', include([
        path('', pet_details, name='pet details'),
        path('', pet_edit, name='pet edit'),
        path('', pet_delete, name='pet delete'),
    ]))
]