from django.urls import path
from Level_Up_App import views

urlpatterns = [
    path('', views.index, name='index')
]