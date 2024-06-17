from django.urls import path

from . import views

urlpatterns = [
    path("",views.index,name="index"),
    path("<int:num>",views.numberchallenge),
    path("<str:month>",views.challenges,name="month-path"),

]