from django.contrib import admin
from django.urls import path, include, reverse_lazy


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
]

