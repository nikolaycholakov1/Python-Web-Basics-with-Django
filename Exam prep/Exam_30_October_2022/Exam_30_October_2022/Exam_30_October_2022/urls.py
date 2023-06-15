from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Exam_30_October_2022.common.urls')),
    path('car/', include('Exam_30_October_2022.car.urls')),
    path('profile/', include('Exam_30_October_2022.car_profile.urls')),
]
