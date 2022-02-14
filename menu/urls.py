from django import views
from django.contrib import admin
from django.urls import path
from .views import menu, pizzas, index, about, addPizza, contact,blog

urlpatterns = [
    path('menu/', menu, name = 'menu'),
    path('home/', index, name = 'home'),
    path('pizzas/', pizzas, name = 'pizza'),
    path('about/', about, name = 'about'),
    path('contact/', contact, name = 'contact'),
    path('blog/', blog, name = 'blog'),
    path('addPizza<int:id>//', addPizza, name = 'addToCard'),



    # path('ingredients/', index, name = 'ingredients'),

]
