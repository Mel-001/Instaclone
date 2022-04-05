from django.urls import path, include
from django.contrib import admin

# app_name = "My_Gallery"
admin.autodiscover()
urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include('instagram.urls'))
]