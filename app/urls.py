from django.conf.urls import url, include
from django.contrib import admin
from app import views

urlpatterns = [
    url(r'^$',views.index),
    url(r'^create$',views.create)
]