from django.conf.urls import path, include
from . import views

urlpattern = [
    path('',views.job_list),
    path('',views.job_detail),
]