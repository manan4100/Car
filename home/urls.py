from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path("",views.index, name='home'),
    path("about",views.about, name='about'),
    path("services",views.services, name='services'),
    path("contact",views.contact,name='contact'),
    path("luxary",views.luxary,name='luxary'),
    path("electric",views.electric,name='electric'),
    path("suv",views.suv,name='suv'),
    path("sport",views.sport,name='sport')
]