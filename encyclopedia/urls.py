from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index")
    path("", views.page, name="page") #to remove, added but ot sure.
]
