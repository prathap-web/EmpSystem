from django.urls import path
from . import views


urlpatterns = [
    path('', views.base, name="base"),
    path('master/', views.Administrator, name="admin"),
    path('euser/', views.euser, name="user"),
    path('registration/', views.registration, name="registration"),
    path('inlogin/', views.inlogin, name="inlogin"),
    path('passwordchanging/', views.passwordchanging, name="passwordchanging")

]
