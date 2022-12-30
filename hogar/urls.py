from django.urls import path
from . import views

urlpatterns =[
    path('', views.hogar, name='hogar'),
    path('cotizado/', views.hogarCotizado, name='hogarCotizado')
]
