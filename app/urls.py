from django.contrib import admin
from django.urls import path,include
from . import views


urlpatterns = [
   path("",views.index,name='index'),
   path("insert/",views.insert, name="insert"),
   path("delete/",views.delete, name="delete"),
   path("update/",views.update, name="update"),
]