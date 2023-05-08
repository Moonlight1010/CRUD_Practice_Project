from django.urls import path
from .views import home, about, read, update, delete_view

urlpatterns = [
    path('', home, name='home-page'),
    path('about/', about, name='about-page'),
    path('read/<int:id>', read, name='read-page'),
    path('update/<int:id>', update, name='update-page'),
    path('delete/<int:id>', delete_view, name='delete-page'),
]