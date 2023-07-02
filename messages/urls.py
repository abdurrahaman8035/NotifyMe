from django.urls import path
from messages.views import HomeView, CreateContact, UpdateContact, DeleteContact

urlpatterns = [
    path('', HomeView, name='home'),
    path('contact/new/', CreateContact.as_view(), name='contact_new'),
    path('contact/edit/<int:pk>/', UpdateContact.as_view(), name='edit_contact'),
    path('contact/delete/<int:pk>/', DeleteContact.as_view(), name='delete_contact'),
]
