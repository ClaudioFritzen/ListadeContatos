from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index' ),
    path('add_contact/', views.addContact, name='add_contact'),
    path('edit/<int:id>', views.editContact, name='edit' ),
]
