from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('science_groups.urls')),
    path('admin/', admin.site.urls),
]
