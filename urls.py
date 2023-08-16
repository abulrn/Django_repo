from django.conf.urls import path, include
from django.contrib import admin

urlpattern = [
    path('admin/',admin.site.urls),
    path('jobs/',include('jobs.urls')),
]