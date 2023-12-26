
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('apiapp/',include("apiapp.urls")),
    path('admin/', admin.site.urls),
]
