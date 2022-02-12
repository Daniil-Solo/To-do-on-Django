from django.contrib import admin
from django.urls import path, include
from core.views import pageNotFound

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
]

handler404 = pageNotFound