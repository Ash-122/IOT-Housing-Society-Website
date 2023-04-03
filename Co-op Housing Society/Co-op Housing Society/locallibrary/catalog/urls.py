from django.conf.urls import url
from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index, name='index'),
    path('r^complaints',views.complaints, name='complaints'),
    path('r^notices',views.notices, name='notices'),
    path('r^maintenance',views.maintenance, name='maintenance'),

]

